import runpod
import torch
from CosyVoice.inference.infer import infer_text  # AJUSTA según CosyVoice

# Aquí cargas el modelo CosyVoice
model = None

def setup():
    global model
    print("Cargando CosyVoice...")
    # Acá pones tu lógica real para cargar el modelo
    model = "modelo_cosy_cargado"
    return

def handler(event):
    input_text = event["input"]["text"]
    
    # Generación (ajústalo a tu pipeline real)
    audio_path = "salida.wav"  # Reemplaza con la ruta real generada por Cosy
    with open(audio_path, "rb") as f:
        audio = f.read()

    return {
        "audio_base64": audio.encode("base64")  # o usa base64.b64encode
    }

runpod.serverless.start({"handler": handler, "setup": setup})
