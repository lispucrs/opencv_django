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
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)


class FilterForm(forms.Form):
    filter_type = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.Select(
        attrs={'class': 'd-flex justify-content-center', 'id': 'padding2'}))
    image = forms.ImageField()


class ImageFiltered(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
