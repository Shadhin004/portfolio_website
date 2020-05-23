from django.contrib import admin
from .models import experience


class experienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration')


admin.site.register(experience, experienceAdmin)




