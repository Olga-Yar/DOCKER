from datetime import time, timedelta

from rest_framework import serializers


def validator_execution_time(value):
    if value > timedelta(seconds=120):
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')


def validator_execution_reward(is_connect):
    if is_connect:
        reward = None
        raise serializers.ValidationError('Запрещен одновременный выбор связанной привычки и указания вознаграждения.')


def validator_connect_pleasure(is_pleasure):
    if not is_pleasure:
        is_connect = None
        raise serializers.ValidationError('В связанные привычки могут попадать только привычки '
                                          'с признаком приятной привычки.')


def validator_pleasure_reward(is_pleasure):
    if is_pleasure:
        reward = None
        is_connect = None
        raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


def validator_periodicity(value):
    if value > timedelta(hours=168):
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
