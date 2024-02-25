from django.db import models

# Create your models here.
class Circuit(models.Model):
  name = models.CharField(max_length = 100, verbose_name = "Track Name")
  image = models.FileField(upload_to="media/static/img", null=True)
  gif = models.FileField(upload_to="media/static/gif", null=True)


  def __str__(self):
      return self.name
  
  
  def save(self, *args,**kwargs):
      super().save(*args,**kwargs)
    
  
