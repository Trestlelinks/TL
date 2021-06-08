from django.contrib import admin
from company.models import Company,Companyuser,BenchResource

# Register your models here.
admin.site.register(Company)
admin.site.register(Companyuser)
admin.site.register(BenchResource)