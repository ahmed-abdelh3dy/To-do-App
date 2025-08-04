from django.urls import path, include
from .views import TaskDetailView , TaskListCreateView ,TaskSearchView

urlpatterns = [
    path('lists/<int:list_pk>/tasks/' , TaskListCreateView.as_view()),
    path('lists/<int:list_pk>/tasks/<int:pk>/' , TaskDetailView.as_view()),
    path('lists/<int:list_pk>/tasks/search/' ,  TaskSearchView.as_view()),


]





























# from .views import ToTaskView 
 



# router = DefaultRouter()
# router.register(r'tasks', ToTaskView, basename='tasks')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
