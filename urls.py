from django.urls import include, path

from .views import clinic, students, teachers, researcher, Plotting_Two_Variables, tables, maps_loc, patient, physician
from django.views.generic.base import TemplateView
#from .views import graph, play_count_by_month

urlpatterns = [
    path('', clinic.home, name='home'),
    path('Plotting-Two-Variables', Plotting_Two_Variables.chart, name='chart'),
    path('maps_loc', maps_loc.chart, name='chart'),
    path('tables', tables.table, name='table'),
    path('hello', maps_loc.hello, name='hello'),


    path('patient/', include(([
        #path('', DataListView.as_view(), name='data_list'),
        path('', patient.QuizListView.as_view(), name='quiz_list'),
        #path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
    ], 'clinic'), namespace='patient')),

    path('students/', include(([
        #path('', DataListView.as_view(), name='data_list'),
        path('', students.QuizListView.as_view(), name='quiz_list'),

        #path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'clinic'), namespace='students')),


    path('teachers/', include(([
        path('', teachers.DataListView.as_view(), name='data_change_list'),
        path('spiral_list', teachers.spiralView.as_view(), name='spiral_list'),
        path('data/<int:pk>/', teachers.DataUpdateView.as_view(), name='data_change'),
        path('data/add/', teachers.DataCreateView.as_view(), name='data_add'),
    ], 'clinic'), namespace='teachers')),

    path('physician/', include(([
        path('', physician.DataListView.as_view(), name='data_change_list'),
        path('spiral_list', physician.spiralView.as_view(), name='spiral_list'),
        path('data/<int:pk>/', physician.DataUpdateView.as_view(), name='data_change'),
        path('data/add/', physician.DataCreateView.as_view(), name='data_add'),
    ], 'clinic'), namespace='teachers')),

    path('researcher/', include(([
        #path('patient_data1', TemplateView.as_view(template_name = 'patient/patient_data1.html'), name = 'patient_data1'),
        #path('graph', TemplateView.as_view(template_name = 'clinic/researcher/graph.html'), name='graph'),
        #path('api/play_count_by_month', researcher.play_count_by_month.views, name='play_count_by_month'),
        path('', researcher.DataListView.as_view(), name='data_list'),
        #path('graph/', researcher.GraphView.as_view(), name='graph_list')
    ], 'clinic'), namespace='researcher')),


]
