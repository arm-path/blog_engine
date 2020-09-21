from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def slugify_title(title):
    """ Метод преобразование текста в slug """
    slug_from_title = slugify(title, allow_unicode = True)
    return slug_from_title + '-'+str(int(time()))


class Post(models.Model):
    """ Модель постов """
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    slug = models.SlugField('URL', max_length=150, blank=True, unique=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True, verbose_name='Теги')
    context = models.TextField('Текст', blank=True)
    date_of_publication = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify_title(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_of_publication']


class Tag(models.Model):
    """ Модель тегов """
    title = models.CharField('Название', max_length=50)
    slug = models.SlugField('URL',max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-title']
