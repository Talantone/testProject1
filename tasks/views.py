from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Task
from .permissions import IsOwner
from .serializers import TasksSerializer





class TasksAPIList(generics.ListCreateAPIView): #API for create and get Task objects

    serializer_class = TasksSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(user=self.request.user)
        return owner_queryset

class TasksAPIUpdate(generics.UpdateAPIView): #API for update Task objects
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsOwner,)

