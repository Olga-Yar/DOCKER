import datetime
import logging

import requests
from django.shortcuts import get_object_or_404

from config import settings
from habits.models.habit import Habit
from users.models import UserCustom

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("log.txt")
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


def get_chat_id(telegram_username):
    """Получение id пользователя в телеграм"""

    api_telegram = f'https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/getUpdates'
    response = requests.get(api_telegram)
    data = response.json()
    if data['ok'] and data['result']:
        for update in data['result']:
            if 'message' in update and 'from' in update['message']:
                if telegram_username[1:] == update['message']['from']['username']:
                    chat_id = update['message']['from']['id']
                    return chat_id
    else:
        return None


def set_chat_id_to_user(chat_id, telegram_username):
    """Запись данных в модель пользователя"""

    user = UserCustom.objects.get(telegram=telegram_username)
    user.chat_id = chat_id
    user.save()


def send_reminder(chat_id):
    """Отправка напоминания об активностях"""

    token = settings.TELEGRAM_API_TOKEN
    user = UserCustom.objects.get(chat_id=chat_id)

    message = f'Привет, {user.telegram}! Напоминаю о твоих активностях: {activites(chat_id)}.'

    request_tg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}',)
    logger.info(f'Статус код: {request_tg.status_code}, {request_tg.text}')


def send_hello_to_new(chat_id):
    """Приветствие пользователя"""

    token = settings.TELEGRAM_API_TOKEN
    user = UserCustom.objects.get(chat_id=chat_id)

    message = f'{user.telegram}, Привет и добро пожаловать!'

    request_tg = requests.post(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    )
    logger.info(f'Новый пользователь: {user.telegram}, статус код: {request_tg.status_code}, {request_tg.text}')


def activites(chat_id):
    """Активности для сообщения"""

    now_do = datetime.datetime.now().isoweekday()
    user = get_object_or_404(UserCustom, chat_id=chat_id)
    user_habits = Habit.objects.filter(user=user)

    response = []
    for habit in user_habits:
        periodic = habit.periodic
        days = habit.days_period

        if periodic == 'daily':
            response.append(habit.user + ' - ' + habit.place + ' - ' + str(habit.time_start))
        else:
            if str(int(now_do) + 1) in days:
                response.append(habit.user + ' - ' + habit.place + ' - ' + str(habit.time_start))

    return '\n-'.join(response)


