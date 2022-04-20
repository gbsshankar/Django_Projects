from django.db import models

class kmt(models.Model):
    Server=models.CharField(max_length=100);
    Location=models.CharField(max_length=100);
    Contact=models.CharField(max_length=100);
    Path=models.CharField(max_length=100)
    
