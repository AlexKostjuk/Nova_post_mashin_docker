import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from parcel import models, forms
from parcel.forms import ParcelForm
from parcel.models import Parcel


# Create your views here.

def parcels_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, 'parcels.html', context={'parcels':parcels})


def get_parcel(request,parcel_id):
    if request.method == 'POST':
        parcel = models.Parcel.objects.get(pk=parcel_id)
        parcel.status = True
        parcel.open_date_time = datetime.datetime.now()
        if parcel.order_date_time is None:
            parcel.order_date_time = datetime.datetime.now()
        if parcel.update_date_time is None:
            parcel.update_date_time = datetime.datetime.now()
        parcel.save()
        parcel.locker.status = True
        parcel.locker.save()
        return redirect ('/parcel/')



def one_parcel_view(request, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)

    return render(request, 'one_parcel.html', context={'parcel': result})

@login_required(login_url='/login')
def parcel_form(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form.save()')
        else:
            # form = ParcelForm()
            form = ParcelForm(initial={'sender': request.user.username})

            return render(request, 'parcel_form.html', context={'form': form})
            # return HttpResponse('not form.save()')
    # form = ParcelForm()
    form = ParcelForm(initial={'sender': request.user.username})
    return render(request, 'parcel_form.html', context={'form':form})
