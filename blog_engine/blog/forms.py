from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


class TagForm(forms.ModelForm):
    """ Определение формы тегов """
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('URL не может иметь название "сreate"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Поле URL должен быть уникальным')
        return new_slug


class PostForm(forms.ModelForm):
    """ Определение формы постов """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'context', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('URL не может иметь название "create"')
        return new_slug
