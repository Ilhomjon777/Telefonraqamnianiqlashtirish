from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

BOT_1_TOKEN = "7687555090:AAFaGqPhqX7j3sLvYUzRqEhjYhKu1zmhQ3o"
CHAT_ID_BOT_2 = 6349583688  # Chat ID butun son bo‘lishi kerak

async def forward_to_bot_2(update: Update, context: CallbackContext) -> None:
    message = update.message
    await message.forward(chat_id=CHAT_ID_BOT_2)

def main():
    app = Application.builder().token(BOT_1_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_bot_2))
    
    app.run_polling()

if __name__ == "__main__":
    main()
