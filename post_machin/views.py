# from django.http import HttpResponse, request
from django.shortcuts import render
from post_machin import models

# Create your views here.
def post_machin_view(request):
    # user = request.user
    post_machines = models.PostMachin.objects.all()
    return render(request, 'post_machines.html', context={'post_machines': post_machines})


def one_post_machin_view(request, post_machin_id):

    one_post_machin = models.PostMachin.objects.get(id=post_machin_id)
    post_machin_lockes = models.Locker.objects.filter(post_machin =one_post_machin)
    # one_locker = models.Locker.objects.get(pk=1)
    return render(request, 'one_post_machin.html', context={'post_machin_lockes': post_machin_lockes})
