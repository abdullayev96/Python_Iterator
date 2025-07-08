from rest_framework import serializers
from .models import User




class UserSerializer(serializers.ModelSerializer):
    total_point = serializers.IntegerField(read_only=True)
    #ranking = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'images', 'plus_ball', 'minus_ball', 'total_point')

    def get_total_point(self, obj):
        return f"{obj.plus_ball} - {obj.minus_ball} = {obj.plus_ball - obj.minus_ball}"


