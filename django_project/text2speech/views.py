from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.decorators import login_required

from .forms import TextForm
from .models import MP3File
from accounts.models import CustomUser

from django.shortcuts import redirect
from django.contrib.auth import logout 

from unrealspeech import UnrealSpeechAPI, play, save
import shortuuid

import os

api_key = 'bv9xZALKkmIl5FkVPOoh7zNfNudNpN37VuCEDLbvc3UqlRT7tIUT6r'
speech_api = UnrealSpeechAPI(api_key)

# Create your views here.
@login_required(login_url="signup")
def home_page_view(request):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect("/")
            print(type(form.cleaned_data))
            print(form.cleaned_data['text'])

            text_to_speech = form.cleaned_data['text']
            timestamp_type = "sentence"  # Choose from 'sentence' or 'word'
            voice_id = "Scarlett"  # Choose the desired voice
            bitrate = "192k"
            speed = 0 
            pitch = 1.0
            audio_data = speech_api.speech(text=text_to_speech,voice_id=voice_id, bitrate=bitrate, timestamp_type=timestamp_type, speed=speed, pitch=pitch)

            id = shortuuid.ShortUUID().random(length=10)

            print(settings.BASE_DIR)
            print(settings.MEDIA_ROOT)

            audio_file_name = f"/{id}.mp3"

            print(audio_file_name)

            audio_path = settings.MEDIA_ROOT + f"/{id}.mp3"

            save(audio_data, audio_path)

            mp3_file = MP3File(name=audio_file_name,text=text_to_speech,file_location=audio_path, owner=request.user)
            mp3_file.save()

            # Deduct one token from the user
            request.user.tokens -= 1
            request.user.save()

            print("AUDIO_PATH: ")
            print(audio_path)

            context = {
                "form": form,
                "audio_path": audio_file_name
            }

            return render(request, 'home.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'home.html', {"form": form})

@login_required(login_url="signup")
def history_page_view(request):
    user_mp3_files = MP3File.objects.filter(owner=request.user)
    context = {
        'user_mp3_files': user_mp3_files
    }
    return render(request, 'history.html', context)

@login_required(login_url="signup")
def account_page_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account.html')