from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import extcolors
import os
from django.conf import settings

import datetime

import requests
import tempfile
from django.core import files
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
    meat_photo = settings.PHOTO_MEAT_DIR + \
        str(sample_meat.photo).split('/')[-1]

    context = {
        "colors": colors,
        "sample_meat": sample_meat,
        "meat_photo": meat_photo
    }

    return render(request, 'tables.html', context)


def add_data(request):
    img_path = os.path.join(settings.IMG_DIR, 'gameboy.png')
    colors, pixel_total = extcolors.extract(img_path)
    date_time = datetime.datetime.now()

    mid = int(str(date_time.year)+str(date_time.month)+str(date_time.day) +
              str(date_time.hour)+str(date_time.minute)+str(date_time.second))
    new_sample = SampleMeat(mid=mid, pixel_total=pixel_total,
                            date_taken=datetime.datetime.now())
    new_sample.save()

    # request = requests.get(img_path, stream=True)
    # file_name = img_path.split('\\')[-1]

    # lf = tempfile.NamedTemporaryFile()
    # for block in request.iter_content(1024 * 8):
    #     if not block:
    #         break
    #     lf.write(block)

    # new_sample = SampleMeat.objects.get(mid=mid)
    # new_sample.photo.save((str(file_name.split('.')[-2]) + str(mid)) + '.png', files.File((open(img_path), 'rb')).read())
    # new_sample.save()
    # new_sample = SampleMeat.objects.get(mid=mid)
    # new_sample.photo = 'meat/gameboy.png'
    # new_sample.save()

    for color_code, pixel_count in colors:
        try:
            new_R = Red.objects.get(intensity=color_code[0])
        except Red.DoesNotExist:
            add_R = Red(intensity=color_code[0])
            add_R.save()
            new_R = Red.objects.get(intensity=color_code[0])
        try:
            new_G = Green.objects.get(intensity=color_code[1])
        except Green.DoesNotExist:
            add_G = Green(intensity=color_code[1])
            add_G.save()
            new_G = Green.objects.get(intensity=color_code[1])
        try:
            new_B = Blue.objects.get(intensity=color_code[2])
        except Blue.DoesNotExist:
            add_B = Blue(intensity=color_code[2])
            add_B.save()
            new_B = Blue.objects.get(intensity=color_code[2])

        try:
            new_pixel_count = PixelCount.objects.get(count=pixel_count)
        except PixelCount.DoesNotExist:
            add_pc = PixelCount(count=pixel_count)
            add_pc.save()
            new_pixel_count = PixelCount.objects.get(count=pixel_count)

        try:
            new_color_code = ColorCode.objects.get(
                code_red=new_R, code_green=new_G, code_blue=new_B, pixels=new_pixel_count)
        except ColorCode.DoesNotExist:
            add_color_code = ColorCode(
                code_red=new_R, code_green=new_G, code_blue=new_B, pixels=new_pixel_count)
            add_color_code.save()
            new_color_code = ColorCode.objects.get(
                code_red=new_R, code_green=new_G, code_blue=new_B, pixels=new_pixel_count)

        new_sample = SampleMeat.objects.get(mid=mid)
        new_sample.color.add(new_color_code)

    return HttpResponse("OK")
