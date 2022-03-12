from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300)
    URLSlug = models.SlugField(max_length=150, unique=True)
    summary = models.CharField(max_length=350)
    body = models.TextField()
    published = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

        def __unicode__(self):
            return u'%s' % self.title

        def __get_absolute_url__(self):
            return reverse('blog.views.post', args=[self.slug])