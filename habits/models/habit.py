from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    PERIODIC_CHOICE = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    DAYS_CHOICE = [
        ('1', "Monday"),
        ('2', "Tuesday"),
        ('3', "Wednesday"),
        ('4', "Thursday"),
        ('5', "Friday"),
        ('6', "Saturday"),
        ('7', "Sunday"),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.CharField(max_length=20, verbose_name='место')
    time_start = models.TimeField(default='00:00:00', verbose_name='время старта')
    action = models.CharField(max_length=50, verbose_name='действие')
    is_pleasure = models.BooleanField(default=False, verbose_name='приятная привычка')
    is_connect = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodic = models.CharField(choices=PERIODIC_CHOICE, default='daily', verbose_name='периодичность')
    days_period = models.CharField(choices=DAYS_CHOICE, default='1', verbose_name='день недели')
    reward = models.CharField(max_length=50, verbose_name='вознаграждение', default=None)
    execution_time = models.TimeField(default='00:01:00', verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return f'{self.user}: {self.action}, {self.execution_time}'

    def save(self, *args, **kwargs):
        if not self.is_pleasure and self.is_connect:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

        elif self.is_pleasure and self.reward is not None:
            raise ValidationError('Запрещен одновременный выбор связанной привычки и указания вознаграждения.')

        elif self.is_connect and self.reward is not None:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


