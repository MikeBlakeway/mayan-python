from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):

    # Fields -->
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

    # Self -->
    def __str__(self):
        return self.user.username


class Category(models.Model):

    # Fields -->
    title = models.CharField(max_length=20)
    icon = models.TextField()

    # Meta -->
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # Self -->
    def __str__(self):
        return self.title


class Post(models.Model):

    # Fields -->
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    snippet = models.TextField()
    body = models.TextField()
    thumbnail = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    comment_count = models.IntegerField(default=0)
    featured = models.BooleanField()

    # Self -->
    def __str__(self):
        return self.title
