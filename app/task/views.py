from drf_spectacular.utils import extend_schema

from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    viewsets,
    mixins
)

from .serializers import TaskSerializer, UpdateTaskSerializer
from .models import Task


@extend_schema(tags=['Task'])
class TaskViewsets(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Task.objects.filter(user=self.request.user)
        return Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return UpdateTaskSerializer
        return TaskSerializer