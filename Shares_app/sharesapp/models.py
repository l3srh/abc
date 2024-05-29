from django.db import models

from django.db import models
from django.contrib.auth.models import User        #-- build in django user application

class UserShareDetails(models.Model):

    s_id=models.BigAutoField(auto_created=True,primary_key=True)
    date=models.DateField(auto_now=True)
    companyshare=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.BigIntegerField()
    user_id=models.ForeignKey(User,related_name='UserShare',on_delete=models.CASCADE)

class UserLogDetails(models.Model):
    log_id=models.BigAutoField(auto_created=True,primary_key=True)
    uid=models.IntegerField()
    time=models.DateTimeField(auto_now=True)
    remark=models.CharField(max_length=250)
    changes=models.CharField(max_length=250)
