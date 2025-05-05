import runpod
import torch
import base64
from CosyVoice.inference.infer import infer_text  # AJUSTA según CosyVoice

# Cargar modelo (simulado por ahora)
model = None

def setup():
    global model
    print("Cargando CosyVoice...")
    model = "modelo_cosy_cargado"  # Aquí irá la carga real
    return

def handler(event):
    input_text = event["input"]["text"]
    
    # Simulación: se supone que el modelo genera este archivo
    audio_path = "salida.wav"  # Asegurate de que exista este archivo para la prueba

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    # Codificar en base64
    encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")

    return {
        "audio_base64": encoded_audio
    }

runpod.serverless.start({"handler": handler, "setup": setup})
