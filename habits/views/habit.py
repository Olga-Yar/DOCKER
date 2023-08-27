from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from habits.models.habit import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsModerator, IsOwner
from habits.seriallizers.habit import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        if self.action == 'create':
            permissions_classes = [IsAuthenticated]  # создавать могут только авторизованные пользователи
        elif self.action == 'update' or self.action == 'delete':
            permissions_classes = [IsModerator | IsOwner]   # редактировать или удалять могут только модератор или владелец
        else:
            if Habit.objects.filter('is_public'):
                permissions_classes = [AllowAny]  # если привычка опубликована, то смотреть может любой пользователь
            else:
                permissions_classes = [IsOwner]

        return [permission() for permission in permissions_classes]

    def list(self, request, **kwargs):
        """Отображение списка привычек"""
        queryset = Habit.objects.all()
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение одной привычки"""
        queryset = Habit.objects.all()
        habit = get_object_or_404(queryset, pk=pk)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)
