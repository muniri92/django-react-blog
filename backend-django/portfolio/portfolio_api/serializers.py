from .models import About, SkillSet, Work, Education
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):

	class Meta:
		model = About
		fields = ('title', 'description')


class EducationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Education
		fields = ('institution', 'degree', 'major', 'certificate', 'start_date', 'end_date')


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

