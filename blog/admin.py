from django.contrib import admin
from .models import Post, Comment

import reversion

class PostAdmin(reversion.VersionAdmin):
    pass

class CommentAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

