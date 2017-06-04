# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    issue_date = models.DateField(blank=True, null=True)
    title_song = models.ForeignKey('Song', blank=True, null=True, related_name='title_song')
    performer = models.ForeignKey('Performer', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'album'


class Band(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, blank=True, null=True)
    performer = models.ForeignKey('Performer', blank=True, null=True)

    class Meta:
        db_table = 'band'


class Bandmember(models.Model):
    band = models.ForeignKey(Band)
    singer = models.ForeignKey('Singer')

    class Meta:
        db_table = 'bandmember'
        unique_together = (('band', 'singer'),)


class Company(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, blank=True, null=True)
    established_time = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'company'


class Composer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'composer'


class Lyricist(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'lyricist'


class Performer(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)

    class Meta:
        db_table = 'performer'


class Singer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    performer = models.ForeignKey(Performer, blank=True, null=True)

    class Meta:
        db_table = 'singer'


class Singsong(models.Model):
    song = models.ForeignKey('Song')
    performer = models.ForeignKey(Performer)

    class Meta:
        db_table = 'singsong'
        unique_together = (('song', 'performer'),)


class SFS:
    def __init__(self,song,performers):
        self.song=song
        self.performers=performers

class Song(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    lyricist = models.ForeignKey(Lyricist, blank=True, null=True)
    composer = models.ForeignKey(Composer, blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True)

    class Meta:
        db_table = 'song'

    @classmethod
    def get_all(self):

        sql1=""" select id, name, style, issue_date, duration, lyricist_name, composer_name, album_name  
                from SongInfor
            """
        sql2=""" select 1 as id, singer_name, band_name
                from songofperformer join performername on (songofperformer.performer_id=performername.id)
                where songofperformer.song_id=%s
                """
        sfs_list=[]
        song_list=Song.objects.raw(sql1)
        for song in song_list:
            performers=Song.objects.raw(sql2%song.id)
            sfs=SFS(song,performers)
            sfs_list.append(sfs)
        return sfs_list
