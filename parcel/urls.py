from django.contrib import admin
from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcels_view),
    # path('get_parcel', parcel.views.get_parcel),
    path('parcel_form/', parcel.views.parcel_form),
    path('<parcel_id>/', parcel.views.one_parcel_view),
    path('<parcel_id>/get_parcel/', parcel.views.get_parcel),

]
