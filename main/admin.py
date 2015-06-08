from django.contrib import admin
from main.models import Fire, FireType

class FireTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rule')

class FireAdmin(admin.ModelAdmin):
    list_display = (
                    'l_people_day', 
                    'l_people_machine',
                    'l_people_other',
                    'm_people_day',
                    'm_people_machine',
                    'm_people_other',
                    'd_people_day',
                    'd_people_machine',
                    'd_people_other',
                    'type',
                    )
    list_filter = ('type',)



admin.site.register(Fire, FireAdmin)
admin.site.register(FireType, FireTypeAdmin)
