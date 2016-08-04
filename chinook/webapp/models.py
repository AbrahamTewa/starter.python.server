from django.db import models


class Album(models.Model):
    id = models.IntegerField(primary_key=True,
                             db_column="AlbumId")

    title = models.CharField(db_column="Title",
                             max_length=120)

    artist = models.ForeignKey("Artist",
                               db_column="ArtistId")


class Artist(models.Model):
    id = models.IntegerField(primary_key=True,
                             db_column="ArtistId")

    name = models.CharField(db_column="Name",
                            max_length=120)


class Genre(models.Model):
    id = models.IntegerField(primary_key=True,
                             db_column="GenreId")

    name = models.CharField(db_column="Name",
                            max_length=120)


class MediaType(models.Model):
    id = models.IntegerField(primary_key=True,
                             db_column="MediaTypeId")

    name = models.CharField(db_column="Name",
                            max_length=120)


class Track(models.Model):
    id = models.IntegerField(primary_key=True,
                             db_column="TrackId")

    name = models.CharField(db_column="Name",
                            max_length=120)

    album = models.ForeignKey("Album",
                              db_column="AlbumId",
                              blank=True,
                              null=True)

    mediaType = models.ForeignKey("MediaType",
                                  db_column="MediaTypeId")

    genre = models.ForeignKey("Genre",
                              db_column="GenreId",
                              blank=True,
                              null=True)

    composer = models.CharField(db_column="Composer",
                                max_length=220,
                                blank=True,
                                null=True)

    milliseconds = models.IntegerField(db_column="Milliseconds")

    bytes = models.IntegerField(blank=True,
                                null=True)

    unitPrice = models.DecimalField(decimal_places=2,
                                    max_digits=12)
