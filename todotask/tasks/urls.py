from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToTaskView 
 



router = DefaultRouter()
router.register(r'tasks', ToTaskView, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]



