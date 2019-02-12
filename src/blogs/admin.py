from django.contrib import admin

from blogs.models import Post, Author, Upvote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('uuid', 'heading', 'is_published')
    list_filter = ('is_published', 'is_deleted')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('author_name', 'is_author')
    list_filter = ('is_author', )

    def author_name(self, object):
        return "%s %s" % (object.user.first_name, object.user.last_name),
        author_name.short_description = 'Name'


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):

    list_display = ('post', 'fingerprint', 'is_upvoted')
