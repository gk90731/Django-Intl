from rest_framework import serializers
from .models import UserProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('country', 'state', 'district', 'city', 'age', 'profession', 'latitude', 'longitude','language' )
class UserLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('language',)
