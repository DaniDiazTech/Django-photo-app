from django.contrib import auth
from django.views.generic import CreateView

from django.contrib.auth import views, authenticate, login

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

class SignUpView(CreateView):

    template_name = 'users/signup.html'
    
    form = UserCreationForm

    success_url = reverse_lazy('photo:list')
    
    def form_valid(self, form):

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        login(self.request, user)

        return super().form_valid(form)

class CustomLoginView(views.LoginView):
    
    template_name = 'users/login.html'