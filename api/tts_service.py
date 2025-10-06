import requests
import base64
from io import BytesIO

def text_to_speech(text, voice="pt-BR"):
    try:
        import openai
        
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        
        audio_data = response.content
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        
        return {
            "success": True,
            "audio_base64": audio_base64,
            "format": "mp3"
        }
        
    except Exception as e:
        print(f"Erro TTS: {e}")
        return {
            "success": False,
            "error": str(e)
        }

def speech_to_text(audio_data):
    try:
        import openai
        
        audio_file = BytesIO(base64.b64decode(audio_data))
        audio_file.name = "audio.wav"
        
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        
        return {
            "success": True,
            "text": transcript.text
        }
        
    except Exception as e:
        print(f"Erro STT: {e}")
        return {
            "success": False,
            "error": str(e)
        }