from django.shortcuts import render





def base(request):

    return render(request, 'perfil/base.html')

def index(request):

    return render(request, 'perfil/index.html')

def cv(request):

    return render(request, 'perfil/cv.html')
