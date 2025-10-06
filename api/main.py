from flask import Flask, request, jsonify
from database import SessionLocal, Doctor, Schedule, Appointment, Patient
from datetime import datetime
from email_service import send_confirmation_email, send_cancellation_email

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "API Médica funcionando!",
        "endpoints": [
            "GET /doctors",
            "GET /doctors/{id}/schedule",
            "POST /appointments",
            "DELETE /appointments/{id}",
            "GET /payment-info"
        ]
    })

@app.route('/doctors')
def get_doctors():
    with SessionLocal() as db:
        doctors = db.query(Doctor).all()
        result = [{"id": d.id, "name": d.name, "specialty": d.specialty, "price": d.price} for d in doctors]
        return jsonify(result)

@app.route('/doctors/<int:doctor_id>/schedule')
def get_schedule(doctor_id):
    with SessionLocal() as db:
        schedules = db.query(Schedule).filter(Schedule.doctor_id == doctor_id, Schedule.available == True).all()
        result = [{"id": s.id, "datetime": s.datetime.isoformat()} for s in schedules]
        return jsonify(result)

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    with SessionLocal() as db:

        appointment = Appointment(
            patient_id=data['patient_id'],
            doctor_id=data['doctor_id'],
            datetime=datetime.fromisoformat(data['datetime'])
        )
        db.add(appointment)

        schedule = db.query(Schedule).filter(
            Schedule.doctor_id == data['doctor_id'],
            Schedule.datetime == datetime.fromisoformat(data['datetime'])
        ).first()
        if schedule:
            schedule.available = False

        db.commit()
        
        # Enviar email de confirmação
        patient = db.query(Patient).filter(Patient.id == data['patient_id']).first()
        doctor = db.query(Doctor).filter(Doctor.id == data['doctor_id']).first()
        
        if patient and doctor:
            send_confirmation_email(
                patient.email,
                doctor.name,
                data['datetime']
            )
        
        return jsonify({"message": "Consulta agendada", "id": appointment.id})

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    with SessionLocal() as db:
        appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

        if not appointment:
            return jsonify({"error": "Consulta não encontrada"}), 404

        # Liberar horário
        schedule = db.query(Schedule).filter(
            Schedule.doctor_id == appointment.doctor_id,
            Schedule.datetime == appointment.datetime
        ).first()
        if schedule:
            schedule.available = True

        # Enviar email de cancelamento
        patient = db.query(Patient).filter(Patient.id == appointment.patient_id).first()
        doctor = db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first()
        
        if patient and doctor:
            send_cancellation_email(
                patient.email,
                doctor.name,
                appointment.datetime.isoformat()
            )
        
        db.delete(appointment)
        db.commit()
        return jsonify({"message": "Consulta cancelada"})

@app.route('/payment-info')
def get_payment_info():
    return jsonify({
        "methods": ["Cartão", "PIX", "Dinheiro"],
        "installments": "Até 12x no cartão",
        "discount": "5% desconto no PIX"
    })

@app.route('/patients')
def get_patients():
    with SessionLocal() as db:
        patients = db.query(Patient).all()
        result = [{"id": p.id, "name": p.name, "email": p.email, "phone": p.phone} for p in patients]
        return jsonify(result)

@app.route('/chat', methods=['POST'])
def chat_webhook():
    data = request.json
    message = data.get('message', '')
    
    # Processar intenção
    if 'horário' in message.lower() or 'agenda' in message.lower():
        return jsonify({"intent": "schedule", "response": "Consultando horários disponíveis..."})
    elif 'agendar' in message.lower():
        return jsonify({"intent": "book", "response": "Vou agendar sua consulta..."})
    elif 'cancelar' in message.lower():
        return jsonify({"intent": "cancel", "response": "Vou cancelar sua consulta..."})
    elif 'pagamento' in message.lower() or 'valor' in message.lower():
        return jsonify({"intent": "payment", "response": "Consultando formas de pagamento..."})
    else:
        return jsonify({"intent": "general", "response": "Como posso ajudá-lo?"})

@app.route('/process-audio', methods=['POST'])
def process_audio():
    from tts_service import speech_to_text, text_to_speech
    
    data = request.json
    audio_data = data.get('audio_base64')
    
    # Converter áudio para texto
    stt_result = speech_to_text(audio_data)
    if not stt_result['success']:
        return jsonify({"error": "Erro ao processar áudio"}), 400
    
    # Processar texto
    text = stt_result['text']
    
    # Simular processamento de chat
    if 'horário' in text.lower():
        response_text = "Consultando horários disponíveis..."
        intent = "schedule"
    elif 'agendar' in text.lower():
        response_text = "Vou agendar sua consulta..."
        intent = "book"
    else:
        response_text = "Como posso ajudá-lo?"
        intent = "general"
    
    # Converter resposta para áudio
    tts_result = text_to_speech(response_text)
    
    return jsonify({
        "transcription": text,
        "response_text": response_text,
        "response_audio": tts_result.get('audio_base64'),
        "intent": intent
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)
