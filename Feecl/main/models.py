from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField('schoolName', max_length=50)
    def __str__(self):
        return "학교 : " + self.school_name