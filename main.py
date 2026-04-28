import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.environ.get("8689255714:AAG6xXFdj04ayNgglqIhebHavXlvI-O3of4")

def start(update, context):
    update.message.reply_text("Bot working ✅")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
