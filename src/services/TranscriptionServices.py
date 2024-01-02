import whisper
from telegram import Update

class TranscriptionService:
    model = whisper.load_model("tiny")

    @classmethod
    async def transcribe(cls, update: Update) -> str:
        """Get text of the voice message but if something goes wrong send an error message.

        Args:
            update (Update): telegram update to get voice message.

        Returns:
            str: message to send to the user.
        """
        try:
            voice = await update.message.voice.get_file()
            result = cls.model.transcribe(voice.file_path)

            return f"✅\n\n{result['text']}"
        
        except Exception as ex:
            print(type(ex))
            print(ex)

            msg_en = "Something was wrong. Try it again."
            msg_es = "Hubo un problema. Intente de nuevo."
            return f"❌\n\n🇬🇧 {msg_en}\n\n🇪🇸 {msg_es}"