from rest_framework  import serializers
from .models import credentials

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user_name',
            'pass_word',
            'email',
        )
        model = credentials