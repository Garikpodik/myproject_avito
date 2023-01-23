from django.db import models

# Create your models here.
class replenishment(models.Model):
    user_id = models.CharField(max_length=40,primary_key = True)
    amount_money = models.PositiveIntegerField()
