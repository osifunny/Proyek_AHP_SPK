from django.forms import ModelForm
from AHPSPK.models import *
from django import forms
class FormLaptop(ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        widgets={
           'Laptop': forms.TextInput({'class':'form-control'}),
           'Harga': forms.NumberInput({'class':'form-control'}),
           'RAM': forms.NumberInput({'class':'form-control'}),
           'Processor':forms.Select({'class':'form-control'}),
           'Storage': forms.NumberInput({'class':'form-control'}),
            'Berat': forms.NumberInput({'class':'form-control'}),
        }


class FormKriteria(ModelForm):
    class Meta:
        model = kriteria_nilai
        fields = '__all__'
