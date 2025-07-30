from django.urls import path
from .views import ToDoListView , ToDoListDetailView , ToDoListSearchView


urlpatterns = [
    path('lists' , ToDoListView.as_view()),
    path('lists/<int:pk>' , ToDoListDetailView.as_view()),
    path('lists/search' , ToDoListSearchView.as_view()),
]

