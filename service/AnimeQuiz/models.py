from django.db import models
from django.db.models import Model


# Create your models here.
class Anime(Model):
    ANIME_TYPE = (('tv', 'TV series'),
                  ('movie', 'Movie'),
                  )

    anime_type = models.CharField(
        max_length=5,
        choices=ANIME_TYPE,
    )
    name_en = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_jp = models.CharField(max_length=100,
                               null=True,
                               )
    anime_id = models.IntegerField(primary_key=True)
    scr_exist = models.BooleanField(default=False)


class ScreenshotsInAnime(Model):
    anime = models.ForeignKey(
        "Anime",
        on_delete=models.CASCADE,
        related_name='screenshots',
    )
    order_number = models.IntegerField()
    img_path = models.CharField(max_length=4000)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['anime', 'order_number'],
                name='SIA_anime_number_uk'
            ),
        ]
