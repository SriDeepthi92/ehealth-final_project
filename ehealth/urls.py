from django.urls import include, path

from clinic.views import clinic, students, teachers, researcher, patient ,physician

urlpatterns = [
    path('', include('clinic.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', clinic.SignUpView.as_view(), name='signup'),
    path('accounts/signup/researcher/', researcher.ResearcherSignUpView.as_view(), name='researcher_signup'),
    path('accounts/signup/patient/', patient.PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/signup/physician/', physician.PhysicianSignUpView.as_view(), name='physician_signup'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
