from django.contrib import admin
from django.urls import path

import parcel.views
import post_machin.views

urlpatterns = [
    path('', post_machin.views.post_machin_view),
    path('<post_machin_id>/', post_machin.views.one_post_machin_view),

]
