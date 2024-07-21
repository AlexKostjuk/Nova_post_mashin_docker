from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from parcel import models, forms
from parcel.forms import ParcelForm


# Create your views here.
def home(request):

    return render(request, 'home.html')


