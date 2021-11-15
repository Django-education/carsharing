from django.db import models


class Car(models.Model):

    title = models.CharField(max_length=200)
    picture = models.FileField(upload_to='pictures/')
    dor = models.IntegerField()
    seat = models.IntegerField()
    transmission = models.TextField(max_length=50)
    engine = models.FloatField(max_length=50)

    def __str__(self) -> str:
        return str(self.title)
