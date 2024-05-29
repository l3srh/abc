from django.contrib import admin
from .models import UserShareDetails,UserLogDetails
# Register your models here.
admin.site.register([UserShareDetails,UserLogDetails])
