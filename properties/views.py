from django.shortcuts import render
from .models import Property

def home(request):
    properties = Property.objects.filter(is_available=True).order_by('-created_at')

    context = {
        'properties': properties
    }

    return render(request, 'properties/index.html', context)