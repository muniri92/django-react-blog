from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import About, SkillSet, Education, Work, Certificate
from .serializers import AboutSerializer, SkillSerializer, EducationSerializer, WorkSerializer, CertificateSerializer


class AboutAPI(generics.ListAPIView):

	serializer_class = AboutSerializer
	queryset = About.objects.all()

	def get_queryset(self):
		queryset = super(AboutAPI, self).get_queryset()
		return queryset.all()


class SkillAPI(generics.ListAPIView):

	serializer_class = SkillSerializer
	queryset = SkillSet.objects.all()

	def get_queryset(self):
		queryset = super(SkillAPI, self).get_queryset()
		return queryset.all()


class WorkAPI(generics.ListAPIView):

	serializer_class = WorkSerializer
	queryset = Work.objects.all()

	def get_queryset(self):
		queryset = super(WorkAPI, self).get_queryset()
		return queryset.all()


class EducationAPI(generics.ListAPIView):

	serializer_class = EducationSerializer
	queryset = Education.objects.all()

	def get_queryset(self):
		queryset = super(EducationAPI, self).get_queryset()
		return queryset.all()

class CertificateAPI(generics.ListAPIView):

	serializer_class = CertificateSerializer
	queryset = Certificate.objects.all()

	def get_queryset(self):
		queryset = super(CertificateAPI, self).get_queryset()
		return queryset.all()
		

