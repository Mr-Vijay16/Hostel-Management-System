from rest_framework import serializers

from .models import Student

from .models import Room


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    class Meta:

        model = Room

        fields = "__all__"