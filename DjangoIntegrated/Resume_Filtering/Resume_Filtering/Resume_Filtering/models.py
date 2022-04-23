from django.db import models

class signupuser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=500)
    umail = models.CharField(max_length=500)
    pwd = models.CharField(max_length=500)
    filename = models.CharField(max_length=500)
    filepath = models.FileField(upload_to = 'files/',null=True, verbose_name = "")
    def __str__ (self):
        return self.filename+": "+srt(self.filepath)
   
    class meta:
        db_table="signupuser"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class FileUpload(models.Model):
    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    
   
    resume = models.FileField(null=False, blank=False)
    description = models.FileField(null=False, blank=False)

    def __str__(self):
        return self.description