from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from habits.models.habit import Habit
from habits.seriallizers.habit import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()

    def list(self, request, **kwargs):
        queryset = Habit.objects.all()
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Habit.objects.all()
        habit = get_object_or_404(queryset, pk=pk)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)
