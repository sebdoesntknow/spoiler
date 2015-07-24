from django.db import models
from web_spoiler.spoiler_tools.tinyurl_tools import tinyurl_gen

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=100)
    sub_date = models.DateTimeField('Date Submitted')

    def __str__(self):
        return self.title_text

class Spoiler(models.Model):
    title = models.ForeignKey(Title)
    spoiler_text = models.TextField()
    pub_date =  models.DateTimeField('Date Added')
    votes = models.IntegerField(default=0)
    # on tinyurl attr we can use the tinyurl_gen in it maybe?
    tinyurl = models.URLField(max_length=50, default='None yet', blank=True)

    # Use the tinyurl generator to cache spoilers tinyurls
    # Can generate url using spoiler.title_id and spoiler.pk
    def generate_spoiler_tinyurl(self, spoiler_id):
        url = 'http://spoiler.mrcricket.me/{}'.format(spoiler_id)
        tinyurl_for_cache = tinyurl_gen(url)
        return tinyurl_for_cache

    def __str__(self):
        return self.spoiler_text
