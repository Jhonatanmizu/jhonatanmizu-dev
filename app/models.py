from django.db import models


class MenuLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    target_blank = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title
