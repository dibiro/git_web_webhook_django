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

admin.site.register(Project, ProjectAdmin)
admin.site.register(Command)
admin.site.register(Update)
admin.site.register(UpdateLog)
