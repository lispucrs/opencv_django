from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template import loader
from django.core.files.base import ContentFile
from .models import FilterForm, ImageFiltered
from . import utils
from io import BytesIO
import cv2
from PIL import Image
import numpy as np



def index(request):
    if request.method == 'POST':
        form = FilterForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.cleaned_data.get('filter_type')
            img = form.cleaned_data.get('image')
            model = ImageFiltered.objects.create(image=img, action=action)
            model.save()
            p_img = Image.open(img)
            p_img = p_img.convert('RGB')  # Because we want to use  it as  a np array
            np_img = np.array(p_img)
            np_img = utils.get_filtered_image(np_img, action)
            np_img = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
            p_img = Image.fromarray(np_img)
            p_img.save(model.image.path)
            #buffer = BytesIO()
            #p_img.save(fp=buffer, format='PNG')
            #buffer.seek(0)
            #img = ContentFile(buffer.getvalue())
            context = {'form': form, 'model': model}
            return render(request, 'filter/index.html', context)
    else:
        form = FilterForm()
        context = {'form': form}
        return render(request, 'filter/index.html', context)

