from django.contrib import admin

from .models import About, Skill, Education, Work
# Register your models here.

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Work)

