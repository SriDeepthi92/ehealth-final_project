from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
#from ..forms import StudentInterestsForm
from ..decorators import student_required
from ..forms import StudentSignUpForm, TakeQuizForm
from ..models import Quiz, patient, TakenQuiz, User, AllData
from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from ..fusioncharts import FusionCharts
from ..fusioncharts import FusionTable
from ..fusioncharts import TimeSeries
import requests
from django_tables2 import SingleTableView

from django.views.generic import ListView
#from .tables import DataTable
from django.shortcuts import render



def chart(request):

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-two-variable-measures-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-two-variable-measures-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{
								text: 'Cariaco Basin Sampling'
							  }""")

    timeSeries.AddAttribute("subcaption", """{
                                    text: 'Analysis of O₂ Concentration and Surface Temperature'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
											plot: [{
											  value: 'O2 concentration',
											  connectNullData: true
											}],
											min: '3',
											max: '6',
											title: 'O₂ Concentration (mg/L)'
										  }, {
											plot: [{
											  value: 'Surface Temperature',
											  connectNullData: true
											}],
											min: '18',
											max: '30',
											title: 'Surface Temperature (°C)'
                                        }]""");

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return  render(request, 'index.html', {'output' : fcChart.render(),'chartTitle': "Plotting two variables (measures)"})


class PatientSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('patient:quiz_list')

class QuizListView(ListView):
    model = Quiz
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'clinic/patient/quiz_list.html'

    def get_queryset(self):
        student = self.request.user.student
        #student_interests = student.interests.values_list('pk', flat=True)
        taken_quizzes = student.quizzes.values_list('pk', flat=True)
        queryset = Quiz.objects.filter(subject__in=student_interests) \
            .exclude(pk__in=taken_quizzes) \
            .annotate(questions_count=Count('questions')) \
            .filter(questions_count__gt=0)
        return queryset
