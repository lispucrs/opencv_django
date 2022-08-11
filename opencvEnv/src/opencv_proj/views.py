from io import BytesIO

import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from PIL import Image

from . import utils
from .models import (FilterForm, FilterForm2, GenalogForm, ImageFiltered,
                     genalogPrototype)


def home(request):
    return render(request, 'home.html')


def howiw(request):
    return render(request, 'howiw.html')


def genalog(request):
    if request.method == 'POST':
        form = GenalogForm(request.POST, request.FILES)
        if form.is_valid():
            numero_documentos = form.cleaned_data.get('numero_documentos')
            template = form.cleaned_data.get('template')
            text_font = form.cleaned_data.get('text_font')
            background_color = form.cleaned_data.get('background_color')
            img = form.cleaned_data.get('image')

            model = genalogPrototype.objects.create()
            model = ImageFiltered.objects.create(image=img, action=action)
            model.save()
            p_img = Image.open(img)
            # Because we want to use  it as  a np array
            p_img = p_img.convert('RGB')
            np_img = np.array(p_img)
            np_img = utils.get_filtered_image(np_img, action)
            np_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
            p_img = Image.fromarray(np_img)
            p_img.save(model.image.path)
            #buffer = BytesIO()
            #p_img.save(fp=buffer, format='PNG')
            # buffer.seek(0)
            #img = ContentFile(buffer.getvalue())
            context = {'form': form, 'model': model,
                       'model_nofilter': model_nofilter}

            return render(request, 'genalog.html', context)
        ########

    else:
        form = GenalogForm()

        context = {'form': form}
        return render(request, 'genalog.html', context)
        ###


def index(request):
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.cleaned_data.get('filter_type')
            img = form.cleaned_data.get('image')
            model_nofilter = ImageFiltered.objects.create(
                image=img, action='NO_FILTER')
            model_nofilter.save()
            model = ImageFiltered.objects.create(image=img, action=action)
            model.save()
            p_img = Image.open(img)
            # Because we want to use  it as  a np array
            p_img = p_img.convert('RGB')
            np_img = np.array(p_img)
            np_img = utils.get_filtered_image(np_img, action)
            np_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
            p_img = Image.fromarray(np_img)
            p_img.save(model.image.path)
            #buffer = BytesIO()
            #p_img.save(fp=buffer, format='PNG')
            # buffer.seek(0)
            #img = ContentFile(buffer.getvalue())
            context = {'form': form, 'model': model,
                       'model_nofilter': model_nofilter}

            return render(request, 'filter/index.html', context)
        ########

    else:
        form = FilterForm()

        context = {'form': form}
        return render(request, 'filter/index.html', context)
        ###


def noiser(request):
    if request.method == 'POST':
        form = FilterForm2(request.POST, request.FILES)
        if form.is_valid():
            action = form.cleaned_data.get('filter_type')
            img = form.cleaned_data.get('image')
            model_nofilter = ImageFiltered.objects.create(
                image=img, action='NO_FILTER')
            model_nofilter.save()
            model = ImageFiltered.objects.create(image=img, action=action)
            model.save()
            p_img = Image.open(img)
            # Because we want to use  it as  a np array
            p_img = p_img.convert('RGB')
            np_img = np.array(p_img)
            np_img = utils.get_filtered_image(np_img, action)
            np_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
            p_img = Image.fromarray(np_img)
            p_img.save(model.image.path)
            #buffer = BytesIO()
            #p_img.save(fp=buffer, format='PNG')
            # buffer.seek(0)
            #img = ContentFile(buffer.getvalue())
            context = {'form': form, 'model': model,
                       'model_nofilter': model_nofilter}

            return render(request, 'noiser.html', context)
        ########

    else:
        form = FilterForm2()

        context = {'form': form}
        return render(request, 'noiser.html', context)
        ###
