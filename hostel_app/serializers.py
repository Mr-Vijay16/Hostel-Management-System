from rest_framework import serializers

from .models import Student

from .models import Room

from .models import Complaint

from .models import RoomAllocation

from .models import Fee


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    class Meta:

        model = Room

        fields = "__all__"

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:

        model = Complaint

        fields = "__all__"

class RoomAllocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = RoomAllocation

        fields = "__all__"


class FeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Fee

        fields = "__all__"