from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
)

from secretos.telegram_settings import get_telegram_settings
from api.telegram_handlers import recibir_video


telegram_settings = get_telegram_settings()
TOKEN = telegram_settings.token






app = ApplicationBuilder().token(TOKEN).build()

# Añadimos el handler para recibir audios
app.add_handler(MessageHandler(filters.AUDIO, recibir_video))

app.run_polling()