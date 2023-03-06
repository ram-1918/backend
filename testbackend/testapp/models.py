from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length = 255, blank = False, null = True)
    password = models.CharField(max_length = 255, blank = False, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'TestModel'
