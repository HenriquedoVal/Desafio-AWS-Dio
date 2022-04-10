from django.db import models
import datetime

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    type =  models.IntegerField(verbose_name='Type')
    episodes = models.IntegerField(null=True, verbose_name='Episodes')
    curr_ep = models.IntegerField(null=True, verbose_name='Current Ep')
    last_view = models.DateTimeField(verbose_name='Last View')

    class Meta:
        db_table = 'Movie'

    def get_data(self):
        return self.last_view.strftime('%a, %b, %y')