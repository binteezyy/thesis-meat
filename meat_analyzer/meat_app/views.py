from django.shortcuts import render
from django.http import HttpResponse

import extcolors
import os
from django.conf import settings
# Create your views here.

from .models import *

def index(request):
    img_path = os.path.join(settings.IMG_DIR, 'gameboy.png')
    colors, pixel_total = extcolors.extract(img_path)

    return HttpResponse(pixel_total)

# def upload_and_rename(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" % (,ext)
#     return os.path.join(settings.IMG_DIR, filename)

def meat_view(request, mid):
    sample_meat = SampleMeat.objects.get(mid=mid)
    colors = sample_meat.color.all()
    return HttpResponse(colors)