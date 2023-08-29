from rest_framework import serializers

from habits.models.habit import Habit
from habits.validators import validator_execution_time, validator_periodicity


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    execution_time = serializers.TimeField(validators=[validator_execution_time])
    periodic = serializers.IntegerField(validators=[validator_periodicity])

    class Meta:
        model = Habit
        fields = [
            'user', 'place', 'time_start', 'action',
            'is_pleasure', 'is_connect', 'periodic',
            'reward', 'execution_time', 'is_public',
        ]
