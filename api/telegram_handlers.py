from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)
from pathlib import Path

from src.noise_detector import procesar_video

ruta_video = Path("blob/Ensayo.aac")



async def recibir_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.audio

    if not video:
        await update.message.reply_text("No he recibido ningún vídeo.")
        return

    await update.message.reply_text("Vídeo recibido. Lo estoy descargando...")

    archivo = await video.get_file()
    check_video_path(ruta_video)
    await archivo.download_to_drive(ruta_video)

    await update.message.reply_text("Vídeo descargado. Ahora lo proceso...")

    resultado = procesar_video(ruta_video)

    await update.message.reply_text(f"Resultado: {resultado}")


def check_video_path(ruta_video: Path) -> bool:
    """Comprueba si la ruta del video es válida y crea las carpetas necesarias para que la ruta sea valida
    """
    if not ruta_video.parent.exists():
        ruta_video.parent.mkdir(parents=True, exist_ok=True)
    return ruta_video.exists()