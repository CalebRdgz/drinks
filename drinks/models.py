from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # make name label for each drink in admin page:
    def __str__(self):
        return self.name + " " + self.description