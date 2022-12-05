from src.lib.message_helper.send_message import send_message
from telegram.error import BadRequest


def delete_message(update, context, message_id):
    try:
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message_id)
    except BadRequest as e:
        if (str(e) == "Message can't be deleted"):
            send_message(update, context, command='error_delete')
