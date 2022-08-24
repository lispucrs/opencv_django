from distutils.command.upload import upload
from io import BytesIO
from logging import PlaceHolder

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

TEMPLATES_CHOICES = (

    ('COLUMNS', 'columns'),
    ('COLUMNS_2', 'columns_2'),
    ('IEEE', 'ieee'),
    ('IEEE_COLUMNS', 'ieee_columns'),
)

TEXTFONT_CHOICES = (

    ('TIMES_NEW_ROMAN', 'times new roman'),
    ('ARIAL', 'arial'),
    ('HELVETICA', 'helvetica'),
    ('CALIBRI', 'calibri'),
)

FONTCOLOR_CHOICES = (

    ('BLACK', 'black'),
    ('GREY', 'grey'),
    ('NAVY', 'navy'),
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
    numero_documentos = forms.IntegerField(label='Número de documentos', widget=forms.NumberInput(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    template = forms.ChoiceField(choices=TEMPLATES_CHOICES, label='Template', widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    text_font = forms.ChoiceField(choices=TEXTFONT_CHOICES, label='Fonte do texto', widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))
    font_color = forms.ChoiceField(choices=FONTCOLOR_CHOICES, label='Cor da fonte', widget=forms.Select(
        attrs={'class': 'btn btn-secondary dropdown-toggle'}))


class genalogPrototype(models.Model):
    numero_documentos = models.IntegerField(max_length=50)
    template = models.CharField(max_length=50)
    text_font = models.CharField(max_length=50)
    font_color = models.CharField(max_length=50)


class ImageFiltered(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)


class GenalogCollection(models.Model):
    id = models
    images = []
