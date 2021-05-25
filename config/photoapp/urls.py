'''Photoapp URL patterns'''

from django.urls import path

from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView
)

app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),

    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),

    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),

    path('photo/create/', PhotoCreateView.as_view(), name='create'),

    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),

    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
]
