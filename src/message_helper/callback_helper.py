
from src.constants import read_config
from src.lib.db.db_functions import set_language
from src.routes.public.help import help

def callback_set_language(update, context):
    callback = update.callback_query  
    username = update.effective_chat.username if update.effective_chat.type == "private" else update.effective_chat.title
    
    set_language(update.effective_chat.id, username, update.effective_chat.type, callback.data)
    CONFIG = read_config(callback.data)
    callback.edit_message_text(text=CONFIG["lang"])
    
    callback.answer()
    
    help(update, context)