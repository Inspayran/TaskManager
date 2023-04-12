
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskSerializerView

router = DefaultRouter()
router.register(r'tasks', TaskSerializerView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
