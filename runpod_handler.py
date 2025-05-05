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
    return {
        "message": f"Texto recibido: {input_text}"
    }


runpod.serverless.start({"handler": handler, "setup": setup})
