from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import UserCustom
from users.permissions import IsModerator
from users.seriallizers import UserCustomSerializer


class UserCustomViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsAuthenticated, IsModerator]


