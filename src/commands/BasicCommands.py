from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from src.services.TranscriptionServices import TranscriptionService

service = TranscriptionService()

async def start(update: Update, context: ContextTypes):
    msg_en = "Welcome! Now you can transcribe your voice messages with only send them to my chat."
    msg_es = "¡Bienvenido! Ya puedes transcribir tus mensajes de voz solamente enviandolos a mi chat."
    await update.message.reply_text(f"🇬🇧 {msg_en}\n\n🇪🇸 {msg_es}")

async def audio_handler(update: Update, context: CallbackContext):
    msg_en = "Getting text..."
    msg_es = "Obteniendo texto..."
    await update.message.reply_text(f"🇬🇧 {msg_en}\n\n🇪🇸 {msg_es}")

    await update.message.reply_text(await service.transcribe(update))