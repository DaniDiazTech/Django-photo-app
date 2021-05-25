'''Photo app generic views'''

from django.shortcuts import get_object_or_404

from django.http import HttpResponseNotAllowed

from django.urls.resolvers import get_resolver

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import Photo

from .forms import CreatePhotoForm, UpdatePhotoForm

class PhotoListView(ListView):
    
    model = Photo     

    template_name = 'photoapp/list.html'

    context_object_name = 'photos'


class PhotoTagListView(ListView):
    
    model = Photo
    
    template_name = 'photoapp/taglist.html'
    
    context_object_name = 'photos'


    # Custom function
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return Photo.objects.filter(tag__slug_in=[self.get_tag()])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context
     

class PhotoDetailView(DetailView):

    model = Photo

    context_object_name = 'photo'

    template_name = 'photoapp/detail.html'


class PhotoCreateView(LoginRequiredMixin, CreateView):

    template_name = 'photoapp/create.html'
    
    model = Photo
    
    form =  CreatePhotoForm

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):

        form.user = self.request.user
        form.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
        return super().form_valid(form)

class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))
    
    def test_func(self):
        
        if self.request.user.is_authenticated():
            return self.request.user is self.get_photo().submitter
        else:
            raise HttpResponseNotAllowed('Sorry you are not allowed here')

class PhotoUpdateView(UserIsSubmitter, UpdateView):
    
    template_name = 'photoapp/update.html'

    model = Photo

    form = UpdatePhotoForm
    
    success_url = reverse_lazy('photo:list')

class PhotoDeleteView(UserIsSubmitter, DeleteView):
    
    template_name = 'photoapp/delete.html'

    model = Photo

    success_url = reverse_lazy('photo:list')