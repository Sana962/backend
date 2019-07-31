from django.db import models

# Create your models here.

class Answer(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class AssignemntSimple(models.Model):
    definition = models.TextField()
    proscons = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.definition



