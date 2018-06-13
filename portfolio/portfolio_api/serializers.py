from .models import About, SkillSet, Work, Education, Certificate
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):

	class Meta:
		model = About
		fields = ('title', 'description')


class EducationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Education
		fields = ('institution', 'major', 'minor', 'certificate', 'start_date', 'end_date')


class CertificateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Certificate
		fields = ('institution', 'certificate', 'start_date', 'end_date')


class SkillSerializer(serializers.ModelSerializer):
	skilltype = serializers.StringRelatedField(many=True)

	class Meta:
		model = SkillSet
		fields = ('skill', 'skilltype')


class WorkSerializer(serializers.ModelSerializer):
	workdesc = serializers.StringRelatedField(many=True)

	class Meta:
		model = Work
		fields = ('company', 'position', 'start_date', 'end_date', 'workdesc')

