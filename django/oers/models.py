from django.db import models

class oersTest(models.Model):
    oer_name = models.CharField(max_length=200)
    oer_url = models.CharField(max_length=200)