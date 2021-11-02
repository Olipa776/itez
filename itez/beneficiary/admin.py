from django.contrib import admin
from itez.beneficiary.models import (
    Province,
    District,
    ServiceArea,
)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']


class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'district_id']


admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
