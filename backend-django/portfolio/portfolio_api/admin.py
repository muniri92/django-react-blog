from django.contrib import admin

from .models import About, SkillSet, SkillType, Education, Work, WorkDesc
# Register your models here.

admin.site.register(About)
admin.site.register(SkillSet)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(WorkDesc)
admin.site.register(SkillType)

