from django.urls import path
from .views import ToListView , ToListViewDetails , SearchListView


urlpatterns = [
    path('lists' , ToListView.as_view()),
    path('lists/<int:pk>' , ToListViewDetails.as_view()),
    path('lists/search' , SearchListView.as_view()),
]

