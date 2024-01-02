from telegram.ext import Application, CommandHandler, MessageHandler, filters
from decouple import config

from src.commands import BasicCommands

def main():
    app = Application.builder().token(config("API_KEY")).build()

    app.add_handler(CommandHandler('start', BasicCommands.start))
    app.add_handler(MessageHandler(filters.VOICE, BasicCommands.audio_handler))

    app.run_polling()

if __name__ == "__main__":
    main()