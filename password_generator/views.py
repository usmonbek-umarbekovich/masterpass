from django.shortcuts import render
from .models import PassGen
from .forms import PassForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get('site', None)
        if query:
            results = PassGen.objects.filter(site_name__contains=query)
            return render(request, 'password_generator/search.html', {'results': results})
    return render(request, 'password_generator/index.html')


class PassCreate(CreateView):
    form_class = PassForm
    template_name = 'password_generator/create.html'
    success_url = reverse_lazy('index')


class PasswordList(ListView):
    model = PassGen
    template_name = 'password_generator/listall.html'
    context_object_name = 'passwords'


class PassDetail(DetailView):
    model = PassGen
    context_object_name = 'object'
    template_name = 'password_generator/detail.html'


class PassEdit(UpdateView):
    model = PassGen
    fields = ['site_name', 'password']
    template_name = 'password_generator/edit.html'
    success_url = reverse_lazy('listall')


class PassDelete(DeleteView):
    model = PassGen
    context_object_name = 'password'
    success_url = reverse_lazy('index')
    template_name = 'password_generator/confirm_delete_password.html'


class PassExist(CreateView):
    # enter an already existing password
    model = PassGen
    fields = ['site_name', 'password']
    template_name = 'password_generator/exist.html'
    success_url = reverse_lazy('index')