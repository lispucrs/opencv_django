from distutils.command.upload import upload
from io import BytesIO

import numpy as np
from django import forms
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

from .utils import get_filtered_image

# Create your models here.


ACTION_CHOICES = (

    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

ACTION_CHOICES_ = (

    ('CAUCASIAN_GRADIENT', '*caucasian gradient*'),
    ('FOLD', '*fold*'),
    ('BOOK_BINDING', '*book binding*'),
    ('DRUMROLL', '*drumroll*'),
)


# class="btn btn-danger dropdown-toggle
class FilterForm2(forms.Form):
    filter_type = forms.ChoiceField(choices=ACTION_CHOICES_, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    image = forms.ImageField()


class FilterForm(forms.Form):
    filter_type = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    image = forms.ImageField()


class GenalogForm(forms.Form):
    numero_documentos = forms.ChoiceField(choices=ACTION_CHOICES_, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    template = forms.ChoiceField(choices=ACTION_CHOICES_, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    text_font = forms.ChoiceField(choices=ACTION_CHOICES_, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    background_color = forms.ChoiceField(choices=ACTION_CHOICES_, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))


class genalogPrototype(models.Model):
    numero_documentos = models.CharField(max_length=50)
    template = models.CharField(max_length=50)
    text_font = models.CharField(max_length=50)
    background_color = models.CharField(max_length=50)


class ImageFiltered(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
