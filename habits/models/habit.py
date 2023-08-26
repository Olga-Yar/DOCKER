from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.CharField(max_length=20, verbose_name='место')
    time_start = models.TimeField(default='00:00:00', verbose_name='время старта')
    action = models.CharField(max_length=50, verbose_name='действие')
    is_pleasure = models.BooleanField(default=False, verbose_name='приятная привычка')
    is_connect = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodic = models.IntegerField(verbose_name='периодичность')
    reward = models.CharField(max_length=50, verbose_name='вознаграждение')
    execution_time = models.TimeField(default='00:00:05', verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return f'{self.user}: {self.action}, {self.execution_time}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


