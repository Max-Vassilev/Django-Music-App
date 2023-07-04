from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from exam_prep.web.validators import alpha_num


class Profile(models.Model):
    username = models.CharField(
        validators=[MinLengthValidator(2), MaxLengthValidator(15), alpha_num], null=True)

    email = models.EmailField()

    age = models.PositiveIntegerField(blank=True, null=True)


class Album(models.Model):
    GENRE_CHOICES = [
        ("pop", "Pop Music"),
        ("jazz", "Jazz Music"),
        ("rnb", "RnB Music"),
        ("rock", "Rock Music"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hip-hop", "Hip-hop Music"),
        ("other", "Other Music")
    ]

    album_name = models.CharField(unique=True, max_length=30)

    artist = models.CharField(max_length=30)

    genre = models.CharField(choices=GENRE_CHOICES)

    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)])

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
