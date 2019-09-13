from django.contrib import admin
from command.models import * 

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'git_name',
    )
    list_filter = ('create_date', 'is_active')
    list_display = ['name', 'git_name', 'is_active',] 


class UpdateItemAdmin(admin.ModelAdmin):
    search_fields = (
        'update__project__name',
    )
    list_filter = ('create_date', 'update')
    list_display = ['update', 'create_date',] 


class CommandAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'project__name',
    )
    list_display = ['project', 'name',] 


admin.site.register(Project, ProjectAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(Update)
admin.site.register(UpdateLog, UpdateItemAdmin)
