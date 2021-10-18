from django.contrib import admin
from .models import HealthAndFitnessBlog
class HealthAndFitnessBlogAdmin(admin.ModelAdmin):
  list_display = ('id','title','img','date','is_published')
  list_display_links = ('id','title','is_published')
  list_filter = ('title',)
  search_fields = ('title',)
  list_per_page = 25

admin.site.register(HealthAndFitnessBlog,HealthAndFitnessBlogAdmin)