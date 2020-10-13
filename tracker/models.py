from django.db import models
from django.utils.text import slugify


class Field(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Well(models.Model):
    name = models.CharField(max_length=20, unique=True)
    field = models.ForeignKey(to=Field, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name


categories = [('Workover','Workover'),('Troubleshooting','Troubleshooting'),
                ('Optimization','Optimization'),('Other','Other')]
class Event(models.Model):
    well = models.ForeignKey(to=Well, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=200, choices=categories)
    event = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'Event no {self.id} for {self.well.name}'
