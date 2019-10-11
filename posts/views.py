from django.views.generic import ListView
from .models import Post, Category


class PostList(ListView):

    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
        })
        return context

    # queryset = Post.objects.filter(featured=True)
