from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from .views import TaskViewsets

router = DefaultRouter()

router.register('task', TaskViewsets)

urlpatterns = [
    path('', include(router.urls))
]
