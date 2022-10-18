from django.shortcuts import render, redirect
from .models import PassGen
from .forms import PassForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'password_generator/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = "password_generator/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True

    success_url = reverse_lazy('index')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)


# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST.get('site', None)
        if query:
            results = PassGen.objects.filter(site_name__contains=query)
            return render(request, 'password_generator/search.html', {'results': results})
    return render(request, 'password_generator/index.html')


class PassCreate(LoginRequiredMixin, CreateView):
    form_class = PassForm
    template_name = 'password_generator/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PassCreate, self).form_valid(form)


class PasswordList(LoginRequiredMixin, ListView):
    model = PassGen
    template_name = 'password_generator/listall.html'
    context_object_name = 'passwords'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passwords'] = context['passwords'].filter(user=self.request.user)
        context['count'] = context['passwords'].count()
        
        return context


class PassDetail(LoginRequiredMixin, DetailView):
    model = PassGen
    context_object_name = 'object'
    template_name = 'password_generator/detail.html'


class PassEdit(LoginRequiredMixin, UpdateView):
    model = PassGen
    fields = ['site_name', 'password']
    template_name = 'password_generator/edit.html'
    success_url = reverse_lazy('listall')


class PassDelete(LoginRequiredMixin, DeleteView):
    model = PassGen
    context_object_name = 'password'
    success_url = reverse_lazy('index')
    template_name = 'password_generator/confirm_delete_password.html'


class PassExist(LoginRequiredMixin, CreateView):
    # enter an already existing password
    model = PassGen
    fields = ['site_name', 'password']
    template_name = 'password_generator/exist.html'
    success_url = reverse_lazy('index')