from django.db import models

# Create your models here.
class Course(models.Model):
    Cname = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.Cname

class Website(models.Model):
    Cname = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sname = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.Sname

class AccessRecord(models.Model):
    Sname = models.ForeignKey(Website, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    