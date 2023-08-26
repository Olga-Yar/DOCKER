from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views.habit import HabitViewSet

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitViewSet.as_view({'get': 'list'})),
    path('habit/<int:pk>/', HabitViewSet.as_view({'put': 'update'})),
    path('habit/create/', HabitViewSet.as_view({'put': 'create'})),
]

router = routers.SimpleRouter()
router.register('habit', HabitViewSet)

urlpatterns += router.urls

