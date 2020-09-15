from.import models
from django.shortcuts import render

def montgomery(request):
    return render(request, 'Montgomery.html' ,{'DataMontgomery': models.DataMontgomery})




