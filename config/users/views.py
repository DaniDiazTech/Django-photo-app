from django.views.generic import CreateView

from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

class SignUpView(CreateView):

    template_name = 'users/signup.html'
    
    form_class = UserCreationForm

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):
        to_return = super().form_valid(form)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        login(self.request, user)

        return to_return
    
class CustomLoginView(LoginView):
    
    template_name = 'users/login.html'