from django.db import models
from django.contrib.auth.models import User
from isbn_field import ISBNField

class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class Rating(models.Model):
    #ISBN = ISBNField(max_length=13)
    ISBN = models.CharField(max_length=13)
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    ratingnum = MinMaxFloat(min_value=0.0, max_value=5.0,max_length=1)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    on_delete = models.DO_NOTHING,
    related_name = "rating"


class Meta:
    verbose_name_plural = "ratings"


def __str__(self):
    return f'{self.ISBN}' #to see the ISBN on each post

