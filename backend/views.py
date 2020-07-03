from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models import Student
from backend.serializers import StudentSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def my_update(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            student = Student(**request.data)
            os = Student.objects.get(owner=self.request.user)
            student.owner = self.request.user
            student.id = os.id
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
