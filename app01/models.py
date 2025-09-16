# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class Crew(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)
    directors = models.CharField(max_length=255, blank=True, null=True)
    writers = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew'

        
class Name(models.Model):
    nconst = models.CharField(primary_key=True, max_length=255)
    primaryname = models.CharField(db_column='primaryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthyear = models.CharField(db_column='birthYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deathyear = models.CharField(db_column='deathYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primaryprofession = models.CharField(db_column='primaryProfession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    knownfortitles = models.CharField(db_column='knownForTitles', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'name'


class Principals(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)  # The composite primary key (tconst, nconst, ordering) found, that is not supported. The first column is selected.
    ordering = models.CharField(max_length=255)
    nconst = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    characters = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'principals'
        unique_together = (('tconst', 'nconst', 'ordering'),)


class Rating(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)
    averagerating = models.CharField(db_column='averageRating', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numvotes = models.CharField(db_column='numVotes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'


class Title(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)
    titletype = models.CharField(db_column='titleType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primarytitle = models.CharField(db_column='primaryTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isadult = models.CharField(db_column='isAdult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startyear = models.CharField(db_column='startYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='endYear', max_length=255, blank=True, null=True)  # Field name made lowercase.
    runtimeminutes = models.CharField(db_column='runtimeMinutes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genres = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'title'

class DoubanTop250(models.Model):
    tconst = models.CharField(primary_key=True, max_length=255)
    primarytitle = models.CharField(db_column='primaryTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originaltitle = models.CharField(db_column='originalTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urls = models.CharField(max_length=255, blank=True, null=True)
    pictures = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    startyear = models.CharField(max_length=255, blank=True, null=True)
    nation = models.CharField(max_length=255, blank=True, null=True)
    genres = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    scorenum = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban_top250'

class Comment(models.Model):
    tconst = models.CharField(max_length=255)
    userid = models.IntegerField()
    rating = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    commentid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'comment'

class User(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=255)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(db_column='userName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    editpermission = models.CharField(db_column='editPermission', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'