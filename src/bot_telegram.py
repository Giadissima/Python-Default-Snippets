from logging import INFO, basicConfig

from telegram import Bot
from telegram.error import (BadRequest, ChatMigrated, NetworkError,
                            TelegramError, TimedOut, Unauthorized)
from telegram.ext import (CommandHandler, Updater)

from src.constants import TOKEN
from src.routes import start

def main():
    # Bot from telegram lib
    bot = Bot(TOKEN)
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # set logging configuration
    basicConfig(
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = INFO)

    # who am i?
    print(bot.get_me(), "\n\n")

    ''' HANDLERS '''
    # TODO specificare la funzione start
    start_handler = CommandHandler('start', start)

    # dispatchers
    dispatcher.add_error_handler(error_callback) # add error handler
    dispatcher.add_handler(start_handler)

    # starting to listen
    updater.start_polling()
    updater.idle()

# when an error occourred
def error_callback(update, context):
    try:
       raise context.error
    except Unauthorized as e:
        # remove update.message.chat_id from conversation list
        print("Unauthorized", e)
    except BadRequest as e:
        # handle malformed requests - read more below!
        print("BadRequest", e)
    except TimedOut as e:
        # handle slow connection problems
        print("TimedOut", e)
    except NetworkError as e:
        # handle other connection problems
        print("NetworkError", e)
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        print("ChatMigrated", e)
    except TelegramError as e:
        # handle all other telegram related errors
        print("TelegramError", e)
