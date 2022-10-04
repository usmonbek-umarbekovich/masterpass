from django.shortcuts import render, get_object_or_404, redirect
from .models import PassGen
import string
import random


# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get('site', None)
        if query:
            results = PassGen.objects.filter(site_name__contains=query)
            return render(request, 'password_generator/search.html', {'results': results})
    return render(request, 'password_generator/index.html')

def create(request):
    if request.method == 'POST':
        site_name = request.POST.get('site')
        if site_name == "":
            return render(request, 'password_generator/create.html')
        password_length = int(request.POST.get('length'))
        
        chars = "!@#$%^&**()_+"
        numbers = '0123456789'
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        all_chars = chars + numbers + lowercase + uppercase

        if password_length > 30:
            msg = 'Max Password Length is 30'
            context = {
                'msg': msg
            }
            return render(request, 'password_generator/create.html', context)
        else:
            password = ''.join(random.sample(all_chars, k=password_length))

        p = PassGen.objects.create(site_name=site_name, password=password)
        p.save()

        context = {
            'site_name': site_name,
            'password': password,
        }
        return render(request, 'password_generator/success.html', context)
    return render(request, 'password_generator/create.html')

def listall(request):
    context = {
        'passwords': PassGen.objects.all(),

    }
    return render(request, 'password_generator/listall.html', context)

def detail(request, pk):
    obj = get_object_or_404(PassGen, id=pk)
    return render(request, 'password_generator/detail.html', {'object': obj})

def edit(request, pk):
    # to do later
    return render(request, 'password_generator/edit.html')

def delete_password(request, pk):
    obj = get_object_or_404(PassGen, id=pk)
    obj.delete()
    return redirect('listall')

def exist(request):
    # enter an already existing password
    if request.method == 'POST':
        site_name = request.POST.get('site')
        if site_name == "":
            return render(request, 'password_generator/exist.html')
        password = request.POST.get('password')
        
        p = PassGen.objects.create(site_name=site_name, password=password)
        p.save()

        context = {
            'site_name': site_name,
            'password': password,
        }
        return render(request, 'password_generator/success.html', context)

    return render(request, 'password_generator/exist.html')