import os
import uuid
import shutil
from fastapi import APIRouter, File, UploadFile, HTTPException

from src.noise_detector import procesar_video


router = APIRouter()



@router.post("/detect_songs_segments", tags=["descripcion"])
def detect_songs_segments(file: UploadFile = File(...)):

    extensiones_validas = {".mp4", ".avi", ".mov", ".mkv"}
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in extensiones_validas:
        raise HTTPException(status_code=400, detail="Formato de vídeo no válido")
    
    nombre_temp = f"{uuid.uuid4()}{extension}"
    ruta_temp = os.path.join("tmp_videos", nombre_temp)
    os.makedirs("tmp_videos", exist_ok=True)

    with open(ruta_temp, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        resultado = procesar_video(ruta_temp)
        return {"resultado": resultado}
    finally:
        if os.path.exists(ruta_temp):
            os.remove(ruta_temp)