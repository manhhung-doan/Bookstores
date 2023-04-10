from django.urls import path
from .views import SignupCreateView

urlpatterns = [
    path('signup/', SignupCreateView.as_view(), name='signup'),
]
