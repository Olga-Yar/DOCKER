from celery import shared_task

from habits.services import get_chat_id, set_chat_id_to_user, send_hello_to_new, logger, send_reminder
from users.models import UserCustom


@shared_task
def getUpdate_bot():
    users = UserCustom.objects.filter(is_active=True, chat_id__isnull=True)

    if users:
        for user in users:
            telegram_username = user.telegram
            chat_id = get_chat_id(telegram_username)
            if chat_id:
                set_chat_id_to_user(chat_id, telegram_username)
                send_hello_to_new(chat_id)
                logger.info(f'Новый пользователь {user.telegarm} с id {chat_id}')


@shared_task
def send_reminders():
    users = UserCustom.objects.filter(is_active=True, chat_id__isnull=False)

    if users:
        for user in users:
            chat_id = user.chat_id
            send_reminder(chat_id)
            logger.info(f'{user.telegarm}, {user.chat_id} - отправлено.')
