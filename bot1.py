from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_1_TOKEN = "7687555090:AAFaGqPhqX7j3sLvYUzRqEhjYhKu1zmhQ3o"
CHAT_ID_BOT_2 = "6349583688"

def forward_to_bot_2(update: Update, context: CallbackContext) -> None:
    message = update.message
    message.forward(chat_id=CHAT_ID_BOT_2)

def main():
    updater = Updater(BOT_1_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_bot_2))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
