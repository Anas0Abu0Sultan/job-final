from django.contrib import admin
from .models import category, freelancer, job, customer

admin.site.register(category)
admin.site.register(freelancer)
admin.site.register(customer)
admin.site.register(job)