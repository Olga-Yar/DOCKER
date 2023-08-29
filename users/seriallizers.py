from rest_framework import serializers

from users.models import UserCustom


class UserCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustom
        fields = [
            'email', 'first_name', 'last_name', 'avatar',
            'phone', 'chat_id', 'telegram',
        ]

