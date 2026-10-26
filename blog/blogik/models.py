from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    """создаем конкретно-прикладной менеджер"""
    def get_queryset(self):
        return super().get_queryset()\
                .filter(status=Post.Status.PUBLISHED)

class OooManager(models.Manager):
    """создан как эксперимент для проверки себя"""
    def get_queryset(self):
        return super().get_queryset()\
                .filter(title__startswith="Who")

class Post(models.Model):
    """создаем модель для хранения постов"""

    class Status(models.TextChoices):
        """класс для управления статусами постов блога"""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)#поле для упр-я постов
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blogik_posts')


    objects = models.Manager()
    published = PublishedManager()
    ooo = OooManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title