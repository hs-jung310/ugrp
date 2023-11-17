# fileupload/views.py
# from .models import FileUpload
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from datetime import datetime
# import time
from django.shortcuts import render, redirect
from .forms import FileUploadForm
import torch, gc
from diffusers import StableDiffusionPipeline

import io
def fileUpload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form = FileUploadForm(request.POST, request.FILES)
            content = request.POST['content']
            upimg = request.FILES["imgfile"]
            context = {
                'fileuploadForm': form,
                'img': upimg,
                'content' : content
            }
            # return redirect('loading/',request)
            return loading(request,context)
        else:
            form = FileUploadForm(request.POST, request.FILES)
            upimg = request.FILES["imgfile"]
            context = {
                'form' : form,
                'img' :upimg,
            }
            return render(request, 'generate.html', context)
    else:
        fileuploadForm = FileUploadForm

        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'fileupload.html', context)

def generate(request):
    return render(request, 'generate.html')


def loading(request,context):
    print("yes")
    content = context['content']
    upimg = context['img']
    # content = request.POST['content']
    # upimg = request.FILES["imgfile"]
    gc.collect()
    torch.cuda.empty_cache()
    prompt = content
    pipeline = StableDiffusionPipeline.from_single_file('C:/Users/anen0310/Downloads/logo0602.ckpt')
   # pipeline.to("cuda")
    pipeline.safety_checker = None
    hgight = 512
    width = 512
    num_inference_steps = 20
    guidance_scale = 8.5
    negative_prompt = ""
    num_images_per_prompt = 1
    eta = 0.0
    # generator = None
    # latents = None
    # prompt_embeds = None
    # negative_prompt_embeds = None
    # output_type = "pil"
    # return_dict = True
    # callback = None
    # callback_steps = 1
    # cross_attention_kwargs = None
    # guidance_rescale = 0.0
    images = pipeline(prompt, hgight, width, num_inference_steps, guidance_scale, negative_prompt,
                      num_images_per_prompt, eta, )
    for i in range(len(images.images)):
        images.images[i].save(('C:/Users/anen0310/Desktop/ugrproj/media/result.png'),
                              'png')
        # images.images[i].save(datetime.now().strftime('/home/mercury/django/stdtest/teststd/expimg/%Y%m%d%H%M%S%F.png'),'png')
    img = images.images[0]

    # fileupload = FileUpload(
    #     content=content,
    #     imgfile=upimg,
    # )
    # fileupload.save()

    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_data = img_io.getvalue()
    img_io.close()
    image ={'img' : img_data }
    return render(request,'result.html',image)

def result(request,context):
	return render(request,'result.html',context)
