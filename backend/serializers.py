from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student


class UserSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=False, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'student']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'schoolId']

