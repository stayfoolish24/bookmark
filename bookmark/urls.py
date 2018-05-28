from django.urls import path, re_path
#from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDetailView
from .views import *

app_name = 'bookmark'
urlpatterns = [
    # http://localhost:8000/bookmark/
    path('', BookmarkListView.as_view(), name='index'),
    path('create/', BookmarkCreateView.as_view(), name="create"),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name="update"), #내부적으로 pk가 정해져 있다. int형식이고 pk기준으로 update하겠다
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name="delete"),
]
