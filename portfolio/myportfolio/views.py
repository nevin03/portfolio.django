from django.shortcuts import render
from .models import nevin

# Create your views here.
def index(request):

    dictionary={
        "key":nevin.objects.all()
    }

    return render(request,"index.html",dictionary)

