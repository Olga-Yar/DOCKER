from django.contrib import admin

from habits.models.habit import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'place', 'time_start', 'action', 'is_pleasure', 'is_connect', 'periodic',
        'days_period', 'reward', 'execution_time', 'is_public')
