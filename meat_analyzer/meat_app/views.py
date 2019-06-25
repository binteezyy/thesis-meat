from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import extcolors
import os
from django.conf import settings
# Create your views here.

from .models import *

def index(request):
    # img_path = os.path.join(settings.IMG_DIR, 'gameboy.png')
    # colors, pixel_total = extcolors.extract(img_path)
    samples = SampleMeat.objects.all()
    context = {
        "samples": samples,
    }

    return render(request, 'home.html', context)

# def upload_and_rename(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (,ext)
#     return os.path.join(settings.IMG_DIR, filename)

def meat_view(request, mid):
    sample_meat = SampleMeat.objects.get(mid=mid)
    colors = sample_meat.color.all()
    meat_photo = settings.PHOTO_MEAT_DIR + str(sample_meat.photo).split('/')[-1]
    context = {
        "colors": colors,
        "sample_meat": sample_meat,
        "meat_photo": meat_photo,
    }
    
    return render(request, 'tables.html', context)

def add_data(request):
    return HttpResponse(request.GET.get('type'))