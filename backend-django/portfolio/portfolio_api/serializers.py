from .models import About, Skill, Work, Education
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):

	class Meta:
		model = About
		fields = ('title', 'description')


class SkillSerializer(serializers.ModelSerializer):

	class Meta:
		model = Skill
		fields = ('skill', 'image', 'proficieny')


class EducationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Education
		fields = ('institution', 'degree', 'start_date', 'end_date')


class WorkSerializer(serializers.ModelSerializer):
	workdesc = serializers.StringRelatedField(many=True)

	class Meta:
		model = Work
		fields = ('company', 'position', 'start_date', 'end_date', 'workdesc')

