from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks.views import TaskView


router = DefaultRouter()
router.register(r'a/v1/tasks', TaskView, base_name='task')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
