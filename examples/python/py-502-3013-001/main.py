# catalog/models.py
from django.conf import settings
from django.db import models
from django.urls import reverse

class Rubric(models.Model):
    name = models.CharField('Название', max_length=80)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'рубрика'
        verbose_name_plural = 'рубрики'

    def __str__(self):
        return self.name


class Listing(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, related_name='listings')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='listings',
    )
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:listing_detail', kwargs={'pk': self.pk})
