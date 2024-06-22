from django.urls import path
from .views import RegisterView, LoginView, ContentListCreateView, ContentDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('contents/', ContentListCreateView.as_view(), name='content-list-create'),
    path('contents/<int:pk>/', ContentDetailView.as_view(), name='content-detail'),
]
