from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id',
            'titulo',
            'email',
            'descripcion',
            'fecha_vencimiento'
        ]
        read_only_fields = [
            'id'
        ]

    def create(self, validated_data):
        auth_user = self.context['request'].user

        # ASSIGN THE AUTH USER TO usuario FIELD IN SERVICE MODEL
        validated_data['user'] = auth_user

        return Task.objects.create(**validated_data)


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'titulo',
            'descripcion',
            'fecha_vencimiento'
        ]
