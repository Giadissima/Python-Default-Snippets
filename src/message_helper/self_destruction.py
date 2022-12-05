from src.constants import PRIVATE_SELF_DESTRUCTION_TIME, PUBLIC_SELF_DESTRUCTION_TIME




# SELF DESTRUCTION MESSAGE FUNCTIONS
def start_self_destruction(update, context, message, **kwargs):
    TIME = (PRIVATE_SELF_DESTRUCTION_TIME if update.effective_chat.type == "private" else PUBLIC_SELF_DESTRUCTION_TIME)
    if 'time' in kwargs:
        TIME = kwargs['time']

    remove_job_if_exists(str(message.message_id), context)
    context.job_queue.run_once(
        self_destruction_message,
        TIME, 
        context={
            "chat":message.chat.id, 
            "message":message.message_id
        },
        name=str(update.effective_chat.id)+'/'+str(message.message_id)
    )

def remove_job_if_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

def self_destruction_message(context):
    args = context.job.context
    context.bot.delete_message(chat_id=args['chat'], message_id=args['message'])