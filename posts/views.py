from django.views.generic import ListView
from .models import Post, Category, Author


class PostList(ListView):

    context_object_name = 'posts'
    model = Post

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        return context
