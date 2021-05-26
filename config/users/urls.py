from django.urls import path

from django.contrib.auth.views import LogoutView

from .views import SignUpView, CustomLoginView

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]