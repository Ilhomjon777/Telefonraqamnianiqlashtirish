import asyncio
import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Loglar uchun sozlamalar
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# .env faylni yuklash
load_dotenv()

# Token va chat ID ni olish
BOT_1_TOKEN = os.getenv("7687555090:AAFaGqPhqX7j3sLvYUzRqEhjYhKu1zmhQ3o")
CHAT_ID_BOT_2 = int(os.getenv("6349583688"))  # Chat ID butun son bo‘lishi kerak

async def forward_to_bot_2(update: Update, context: CallbackContext) -> None:
    """Kelgan xabarlarni 2-botga yo‘naltirish"""
    message = update.message
    if message:
        try:
            await context.bot.forward_message(
                chat_id=CHAT_ID_BOT_2,
                from_chat_id=message.chat_id,
                message_id=message.message_id,
            )
            logger.info(f"Xabar {CHAT_ID_BOT_2} ga yo‘naltirildi.")
        except Exception as e:
            logger.error(f"Xatolik yuz berdi: {e}")

def main():
    """Botni ishga tushirish"""
    if not BOT_1_TOKEN or not CHAT_ID_BOT_2:
        logger.error("BOT_1_TOKEN yoki CHAT_ID_BOT_2 topilmadi. Iltimos, .env faylni to‘ldiring.")
        return

    app = Application.builder().token(BOT_1_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_bot_2))

    logger.info("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
