from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import ListView
from django.urls import include, path
from django.shortcuts import render
from ..forms import ResearcherSignUpForm
from ..models import User, Data, Play
from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView



class ResearcherSignUpView(CreateView):
    model = User
    form_class = ResearcherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'researcher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('researcher:data_list')

class DataListView(ListView):
    model = Data
    ordering = ('name', )
    #context_object_name = 'qjuizzes'
    template_name = 'clinic/researcher/data_list.html'
