from telegram import InlineKeyboardMarkup
from src.constants import read_config

from src.lib.db.conf import connection
from src.lib.db.user_DAO import select_lang
from src.lib.message_helper.self_destruction import start_self_destruction


def send_video(update, context, video, **kwargs):
    text = ""
    message_sent = None

    reply = None
    buttons = None
    self_destruct = False
    self_destruct_time = None

    if 'reply' in kwargs:
        reply = kwargs['reply']

    if 'self_destruct' in kwargs:
        self_destruct = kwargs['self_destruct']

    if 'self_destruct_time' in kwargs:
        self_destruct_time = kwargs['self_destruct_time']

    if 'buttons' in kwargs:
        buttons = InlineKeyboardMarkup(kwargs['buttons'])

    if 'command' in kwargs:
        # query and connection
        conn = connection()
        cur = conn.cursor()
        lang = select_lang(cur, update.effective_chat.id).fetchall()[0][0]
        
        CONFIG = read_config(lang)
        text = CONFIG[kwargs['command']]

        # closing db connection
        cur.close()
        conn.close()

    elif 'text' in kwargs:
        text = kwargs['text']

    otherArgs = {}  
    if reply:
        otherArgs['reply_to_message_id'] = reply

    if buttons and text == '':
        message_sent = context.bot.send_video(
            chat_id=update.effective_chat.id, 
            video=video,
            reply_markup=buttons
        )
    elif buttons and text != '':
        message_sent = context.bot.send_video(
            chat_id=update.effective_chat.id, 
            video=video,
            caption=text,
            reply_markup=buttons
        )
    elif not buttons and text == '':
        message_sent = context.bot.send_video(
            chat_id=update.effective_chat.id, 
            video=video,
        )
    elif not buttons and text != '':
        message_sent = context.bot.send_video(
            chat_id=update.effective_chat.id, 
            video=video,
            caption=text,
        )

    if self_destruct:
        if self_destruct_time:
            start_self_destruction(update, context, message_sent, time = self_destruct_time)
        else:
            start_self_destruction(update, context, message_sent) 
