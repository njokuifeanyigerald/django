from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True )
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default="this is cool")
    # yes = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return f"/render/{self.id}/"

    def get_absolute_url(self):
            return reverse('project:render_data', kwargs={"id":self.id})


