from telegram.ext import Application, CommandHandler, MessageHandler, filters
from decouple import config

def main():
    app = Application.builder().token(config("API_KEY")).build()

    app.run_polling()