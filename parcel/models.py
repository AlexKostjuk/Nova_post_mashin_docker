from datetime import datetime
import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from post_machin.models import PostMachin, Locker
logger = logging.getLogger(__name__)

# Create your models here.
class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machin = models.ForeignKey(PostMachin, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    order_date_time = models.DateTimeField('date published',default=datetime.now)
    update_date_time = models.DateTimeField('date published',default=datetime.now)
    open_date_time = models.DateTimeField('date published', null=True, blank=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id} {self.sender} {self.recipient} {self.post_machin.adress} {self.locker} '

    def __repr__(self):
        return f'{self.id} {self.sender} {self.recipient} {self.post_machin.adress} {self.locker} '


@receiver(post_save, sender=Parcel)
def update_status_on_parcel_to_locker(sender, instance, created, **kwargs):
    print(instance)
    if instance.status == False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = False
            parcel_locker.save()
            logger.info(f"updated locker status for parcel {instance}")