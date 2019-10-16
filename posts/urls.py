from django.urls import path
from django.views.generic import TemplateView

from .views import PostListView, PostDetailView, CategoryListView

urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/', CategoryListView.as_view(), name="category-list"),

]
