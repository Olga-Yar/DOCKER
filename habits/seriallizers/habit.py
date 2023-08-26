from rest_framework import serializers

from habits.models.habit import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = [
            'user', 'place', 'time_start', 'action',
            'is_pleasure', 'is_connect', 'periodic',
            'reward', 'execution_time', 'is_public',
        ]
