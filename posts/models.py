from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class SocialMedia(models.Model):

    # Fields -->
    facebook_url = models.URLField(default='')
    facebook_icon = models.TextField(default='fa fa-facebook')
    instagram_url = models.URLField(default='')
    instagram_icon = models.TextField(default='fa fa-instagram')
    dribble_url = models.URLField(default='')
    dribble_icon = models.TextField(default='fa fa-dribble')
    linkdin_url = models.URLField(default='')
    linkdin_icon = models.TextField(default='fa fa-linkdin')
    github_url = models.URLField(default='')
    github_icon = models.TextField(default='fa fa-github')


class Author(models.Model):

    # Choices -->
    MD = 'Managing Director'
    OD = 'Operations Director'
    TD = 'Technical Director'
    DEFAULT_ROLE = 'DR'
    JOB_ROLES = [
        (MD, 'Managing Director'),
        (OD, 'Operations Director'),
        (TD, 'Technical Director'),
        (DEFAULT_ROLE, 'Guest Author'),
    ]

    # Fields -->
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField()

    facebook_url = models.URLField(default='')
    instagram_url = models.URLField(default='')
    dribble_url = models.URLField(default='')
    linkdin_url = models.URLField(default='')
    github_url = models.URLField(default='')

    author_bio = models.TextField(max_length=300, default='')
    job_role = models.CharField(max_length=50,
                                choices=JOB_ROLES,
                                default=DEFAULT_ROLE,)

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
    published = models.BooleanField(default=False)

    # Self -->
    def __str__(self):
        return self.title
