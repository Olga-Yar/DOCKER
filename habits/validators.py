from datetime import time, timedelta

from rest_framework import serializers


def validator_execution_time(value):
    if value > timedelta(seconds=120):
        raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')


def validator_periodicity(value):
    if value > timedelta(hours=168):
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
