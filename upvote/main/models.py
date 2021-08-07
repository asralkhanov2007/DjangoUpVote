from django.db import models

# Create your models here.


class Upvote(models.Model):
    title = models.CharField('Title...', max_length=150)
    slug = models.SlugField('*',unique=True, max_length=150)
    image = models.ImageField('Image...', upload_to='media/UpVoteImages/')
    body = models.TextField('Body....')
    author = models.CharField('Author...', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Upvote'
        verbose_name_plural = 'Upvotes'