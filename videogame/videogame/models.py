# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    u_age = models.IntegerField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    passwords = models.IntegerField()
    class Meta:
        db_table ="User"
        
class game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=100)
    age_rest = models.IntegerField()
    rate = models.IntegerField()
    
    class Meta:
        db_table ="Game"
        
class tournament(models.Model):
    tournament_id = models.IntegerField(primary_key=True)
    tournament_name = models.CharField(max_length=100)
    tournament_type = models.CharField(max_length=100)
    prize = models.IntegerField()
    
    class Meta:
        db_table ="Tournament"
