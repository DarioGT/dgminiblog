from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField( default=timezone.now )
    published_date = models.DateTimeField(blank=True, null=True)

    sm_upd_date = models.DateTimeField( auto_now= True )
    sm_add_date = models.DateTimeField( auto_now_add= True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title