from django.contrib.auth.models import User
from django.db import models
from hashlib import md5
from django.conf import settings

# Create your models here.
class Url(models.Model):

    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    @classmethod
    def create(self, long_url, user):

        tmp = md5(long_url.encode()).hexdigest()[:6]
        tmp = '127.0.0.1:8000' + '/' + tmp
   
        try:
            obj = self.objects.create(long_url=long_url, short_url=tmp, user=user)
        except BaseException:
            obj = self.objects.get(long_url=long_url, user=user)
        return obj
