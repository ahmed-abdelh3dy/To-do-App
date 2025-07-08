from django.urls import path, include
from .views import ToTaskView , ToTaskDetailView

urlpatterns = [
    path('lists/<int:list_pk>/tasks' , ToTaskView.as_view()),
    path('lists/<int:list_pk>/tasks/<int:pk>' , ToTaskDetailView.as_view())

]





























# from .views import ToTaskView 
 



# router = DefaultRouter()
# router.register(r'tasks', ToTaskView, basename='tasks')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
