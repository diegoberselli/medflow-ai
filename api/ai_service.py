import openai
import json

def process_with_ai(message, context=None):
    """Process message with AI to extract intent and parameters"""
    
    system_prompt = """
    You are a medical assistant that helps patients with:
    1. Check available schedules
    2. Book appointments
    3. Cancel appointments
    4. Get payment information
    
    Respond in JSON format:
    {
        "intent": "schedule|book|cancel|payment|general",
        "parameters": {...},
        "response": "friendly response in Portuguese"
    }
    
    Always respond in Portuguese to the user.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.3
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
        
    except Exception as e:
        return {
            "intent": "general",
            "parameters": {},
            "response": "Desculpe, não consegui processar sua solicitação."
        }

def generate_response(intent, data=None):
    """Generate response based on intent and data"""
    
    responses = {
        "schedule": f"Horários disponíveis encontrados: {len(data) if data else 0}",
        "book": "Consulta agendada com sucesso! Você receberá um email de confirmação.",
        "cancel": "Consulta cancelada com sucesso!",
        "payment": "Formas de pagamento: Cartão, PIX, Dinheiro. Desconto de 5% no PIX.",
        "general": "Como posso ajudá-lo hoje?"
    }
    
    return responses.get(intent, "Como posso ajudá-lo?")