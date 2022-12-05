# sending messages
from src.constants import read_config
from src.lib.db.conf import connection
from src.lib.db.user_DAO import select_lang
from telegram import InlineKeyboardMarkup, ParseMode


def send_message(update, context, **kwargs):
    text = ""

    reply = None
    buttons = None

    if 'reply' in kwargs:
        reply = kwargs['reply']


    if 'buttons' in kwargs:
        buttons = InlineKeyboardMarkup(kwargs['buttons']) 

    elif 'text' in kwargs:
        text = kwargs['text']
    else:
        raise RuntimeError("Invalid kwargs for edit_message, missing text or command arguments")

    otherArgs = {}
    if reply:
        otherArgs['reply_to_message_id'] = reply

    if buttons:
        message_sent = context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=text, 
            parse_mode=ParseMode.HTML,
            reply_markup = buttons,
            api_kwargs = otherArgs
        )
    else:
        message_sent = context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=text, 
            parse_mode=ParseMode.HTML,
            api_kwargs = otherArgs
        )