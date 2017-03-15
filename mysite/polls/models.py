from django.db import models


# Create your models here.
class Player(models.Model):

    kit_num = models.IntegerField()
    name = models.CharField(max_length=40)
    pos = models.CharField(max_length=2)
    dob = models.CharField(max_length=8)
    nat = models.CharField(max_length=3)
    apps = models.CharField(max_length=10)
    goals = models.IntegerField()
    assists = models.IntegerField()
    mins = models.IntegerField()

    def __str__(self):
        return "{}: {} - {}".format(self.kit_num, self.name, self.pos)
        
