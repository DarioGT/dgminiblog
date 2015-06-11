from django.db import models
from django.utils import timezone

from jsonfield2.fields import JSONField

from taggit.managers import TaggableManager
from audit_log.models.managers import AuditLog

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    sm_upd_date = models.DateTimeField(auto_now=True)
    sm_add_date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager( blank=True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    audit_log = AuditLog()
    
    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text


# =======================================================

class JsonModel(models.Model):
    code = models.CharField(blank=False, null=False, max_length=20)
    status = models.CharField(blank=True, null=True, max_length=20)

    info = JSONField(default={})

#     objects = models.Manager()
#     jsondata = JSONAwareManager(json_fields = ['info'])

    def __str__(self):
        return self.code


