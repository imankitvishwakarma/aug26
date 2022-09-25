from django.contrib import admin
from demo.models import service
class serviceAdmin(admin.ModelAdmin):
    service_data=('service_icon','service_heading','service_details')
admin.site.register(service,serviceAdmin)

# Register your models here.
