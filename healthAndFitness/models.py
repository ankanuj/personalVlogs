from django.db import models

class HealthAndFitnessBlog(models.Model):
  title = models.CharField(max_length=250,blank=True)
  img = models.ImageField(upload_to='blogsPhotos/%y/%m/%d/',blank=False,)
  text = models.TextField(max_length=700)
  date = models.DateTimeField(auto_now=False, auto_now_add=True)
  is_published = models.BooleanField(default=True)

  def __str__(self):
        return self.title