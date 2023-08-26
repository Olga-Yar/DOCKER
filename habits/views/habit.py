from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from habits.models.habit import Habit
from habits.permissions import IsModerator, IsOwner
from habits.seriallizers.habit import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        # Проверка разрешения для разных методов
        if self.action == 'create':
            permissions_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'delete':
            permissions_classes = [IsModerator | IsOwner]
        else:
            permissions_classes = [AllowAny]

        return [permission() for permission in permissions_classes]

    def list(self, request, **kwargs):
        queryset = Habit.objects.all()
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Habit.objects.all()
        habit = get_object_or_404(queryset, pk=pk)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)
