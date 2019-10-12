from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, Category, Author


class PostList(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.filter(published=True).order_by('-created_date')

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        context['featured'] = Post.objects.filter(published=True,
                                                  featured=True).order_by('-created_date')[0:3]
        context['latest'] = Post.objects.order_by('-created_date')[0:3]
        return context
