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
    ('CAUCASIAN_GRADIENT', '*caucasian gradient*'),
    ('FOLD', '*fold*'),
    ('BOOK_BINDING', '*book binding*'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)


# class="btn btn-danger dropdown-toggle

class FilterForm(forms.Form):
    filter_type = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    image = forms.ImageField()


class ImageFiltered(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
