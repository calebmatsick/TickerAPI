from django.db import models

class stock(models.Model):
    ticker=models.CharField(max_length=4)
    exchange=models.CharField(max_length=4)

    def __str__(self):
        return