from django.contrib import admin

from .models import About, Skill, Education, Work, WorkDesc
# Register your models here.

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(WorkDesc)

