from django.shortcuts import render
import os


# Create your views here.
def home(request):
    google_maps_api = os.environ.get('Google_Maps_Api')
    context = {
        'google_maps_api': google_maps_api,
    }
    return render(request, 'store/home.html', context)
