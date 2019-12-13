from django.db import models
from django.urls import reverse
# Create your models here.
class ClassApp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100000)
    summary = models.TextField()
    remember = models.BooleanField(default=False)


    def get_absolute_url(self):
            return reverse("class_app:class_detail", kwargs={"pk":self.pk})


