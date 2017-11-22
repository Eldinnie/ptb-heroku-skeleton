import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.effective_message.reply_text("Hi!")


def echo(bot, update):
    update.effective_message.reply_text(update.effective_message.text)


if __name__ == "__main__":
    TOKEN = "Your token from @Botfather"
    TOKEN = os.environ.get('TOKEN')
    NAME = "The name of your app on Heroku"
    NAME = os.environ.get('NAME')

    port = os.environ.get('PORT')

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(port),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
