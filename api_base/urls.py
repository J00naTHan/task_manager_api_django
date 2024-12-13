from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task.views import TaskViewSet
from user.views import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r'', UserViewSet, basename='user')

task_router = routers.DefaultRouter()
task_router.register(r'', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/users/', include(user_router.urls)),
    path('api/tasks/', include(task_router.urls)),
]
