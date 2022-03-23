from .views import MainView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post'),
]