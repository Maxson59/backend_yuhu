from django.db import models

from core.models import CommonMoves
from user.models import User
from datetime import date


class Task(CommonMoves):
    titulo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    email = models.EmailField(
        null=False
    )
    descripcion = models.TextField(
        blank=True
    )
    fecha_vencimiento = models.DateField(
        null=False,
        default=date(2024, 10, 29)
    )

    # * RELATIONSHIPS
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'task'
        verbose_name = 'tasks'
        ordering = ['creado']
