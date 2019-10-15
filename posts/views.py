from django.shortcuts import get_object_or_404

from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, TemplateView, DetailView

from .models import Post, Category, Author


def get_category_count():
    category_count = Post.objects.values(
        'categories__title').annotate(Count('categories'))
    return category_count


class PostListView(ListView):
    model = Post
    template_name = "articles/"
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.filter(published=True).order_by('-created_date')
    category_count = get_category_count()

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['category_count'] = self.category_count
        context['authors'] = Author.objects.all()
        context['featured'] = Post.objects.filter(published=True,
                                                  featured=True).order_by('-created_date')[0:3]
        context['latest'] = Post.objects.order_by('-created_date')[0:3]
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj


class CategoryView(TemplateView):
    template_name = 'posts/category.html'
