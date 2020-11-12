# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fulltext(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.IntegerField()
    fulltext = models.CharField(db_column='fullText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)
    fullrepeat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fulltext'


class Paragraphtext(models.Model):
    id = models.IntegerField(primary_key=True)
    textid = models.IntegerField(db_column='textId')  # Field name made lowercase.
    paragraph = models.CharField(max_length=255, blank=True, null=True)
    repeat = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paragraphtext'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
