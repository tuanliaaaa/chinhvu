from django.db import models
from .User import User
from .Chapter import Chapter
from django.core.validators import MaxValueValidator, MinValueValidator
class History(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,related_name="userchapter")
    Chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,related_name="chapteruser")
    WatchedTime = models.FloatField(null=True)
    Rate= models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],default=1
    )
