import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirmation_email(patient_email, doctor_name, appointment_time):
    """Enviar email de confirmação de consulta"""
    
    # Configuração SMTP (Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "seu-email@gmail.com"  # Configurar
    sender_password = "sua-senha-app"     # Configurar
    
    # Criar mensagem
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = patient_email
    message["Subject"] = "Confirmação de Consulta Médica"
    
    body = f"""
    Olá!
    
    Sua consulta foi agendada com sucesso:
    
    Médico: {doctor_name}
    Data/Hora: {appointment_time}
    
    Atenciosamente,
    Clínica Médica
    """
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Conectar e enviar
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, patient_email, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False

def send_cancellation_email(patient_email, doctor_name, appointment_time):
    """Enviar email de cancelamento de consulta"""
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "seu-email@gmail.com"
    sender_password = "sua-senha-app"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = patient_email
    message["Subject"] = "Cancelamento de Consulta Médica"
    
    body = f"""
    Olá!
    
    Sua consulta foi cancelada:
    
    Médico: {doctor_name}
    Data/Hora: {appointment_time}
    
    Atenciosamente,
    Clínica Médica
    """
    
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, patient_email, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        return False