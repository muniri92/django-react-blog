from django.urls import path
from django.views.generic import TemplateView
from .views import AboutAPI, SkillAPI, WorkAPI, EducationAPI

urlpatterns = [
	path('about', AboutAPI.as_view()),
	path('skill', SkillAPI.as_view()),
	path('education', EducationAPI.as_view()),
	path('work', WorkAPI.as_view()),
]