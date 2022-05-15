from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    '''model that will be used to store
       images retrieved from different sites.'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)   # Database indexes improve query performance.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        '''Automatically generates a flug field
           based on the value of the title'''
        if not self.slug:
            self.slug = slugify(self.tltle)
        super().save(*args, **kwargs)