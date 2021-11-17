from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Subject_1(models.Model):
    subject_name = models.CharField('Title', max_length=50)
    subject_teacher = models.CharField('Teacher', max_length=50)
    subject_star = models.FloatField('Star',default=0, null=True)
    subject_credit = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "과목 : " + self.subject_name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

class Comment_1(models.Model):
    comment_text = models.CharField('Text', max_length=400)
    comment_star = models.PositiveBigIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment_starWidth = models.PositiveIntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    subject_id = models.ForeignKey('Subject_1',on_delete=models.CASCADE)
    writer_id = models.PositiveIntegerField(default=1)
    writer_generation = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '별점 : ' + str(self.comment_star)