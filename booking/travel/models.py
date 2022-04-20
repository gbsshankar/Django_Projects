from django.db import models
# Create your models here.

class credentials(models.Model):
    user_name=models.CharField(max_length=15)
    pass_word=models.CharField(max_length=15)
    email=models.EmailField()
    class Meta:
        db_table="credentials"
    
