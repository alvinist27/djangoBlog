from .views import MainView, PostDetailView, SignUpView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post'),
    path('signup/', SignUpView.as_view(), name='signup'),
]