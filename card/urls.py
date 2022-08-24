from django.urls import path
from .views import index_page, detail_post

urlpatterns = [
    path('', index_page),
    path('detail/<int:pk>/', detail_post, name='detail'),
]