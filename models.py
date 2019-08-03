from django.db import models
from django.contrib.auth.models import User

#user=models.ForeignKey(User,on_delete=models.CASCADE)
#
#user=models.OneToOneField(
#        User,
#        on_delete=models.CASCADE,
#        primary_key=True,
#    )
# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

class Step(models.Model):
    step_text=models.CharField(max_length=400)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)

class Ingredient(models.Model):
    text=models.CharField(max_length=200)
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
