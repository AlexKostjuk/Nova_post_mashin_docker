from django.forms import ModelForm
from parcel.models import Parcel

class ParcelForm(ModelForm):
    class Meta:
        model = Parcel
        # fields = '__all__'
        fields = ['sender', 'recipient', 'size', 'post_machin']  # замените на имена полей вашей модели
