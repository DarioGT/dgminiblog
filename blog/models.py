from django.db import models
from django.utils import timezone

from jsonfield2.fields import JSONField

from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    sm_upd_date = models.DateTimeField(auto_now=True)
    sm_add_date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

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



class JSONFieldTestModel(models.Model):
    json = JSONField("test", null=True, blank=True)

    class Meta:
        app_label = 'jsonfield2'


class JSONFieldWithDefaultTestModel(models.Model):
    json = JSONField(default={"sukasuka": "YAAAAAZ"})

    class Meta:
        app_label = 'jsonfield2'


class BlankJSONFieldTestModel(models.Model):
    null_json = JSONField(null=True)
    blank_json = JSONField(blank=True)

    class Meta:
        app_label = 'jsonfield2'


class CallableDefaultModel(models.Model):
    json = JSONField(default=lambda: {'x': 2})

    class Meta:
        app_label = 'jsonfield2'
