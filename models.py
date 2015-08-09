from django.db import models
from web_spoiler.spoiler_tools.tinyurl_tools import tinyurl_gen
from django.utils import timezone

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=100)
    sub_date = models.DateTimeField('Date Submitted')

    # Create some random titles for testing
    # Also creates spoilers for each Title
    # because having a spoilerless title makes no sense :)
    @staticmethod
    def insert_titles(title_amount=5, spoiler_amount=5):
        """
        Insert random Titles into the database.
        WARNING: Only to be used in Development environment!
        """
        import forgery_py
        for i in range(0, title_amount):
            t = Title(title_text=forgery_py.lorem_ipsum.title(), sub_date=timezone.now())
            t.save()
            for s in range(0, spoiler_amount):
                t.spoiler_set.create(spoiler_text=forgery_py.lorem_ipsum.words(), pub_date=timezone.now())

    def __str__(self):
        return self.title_text

class Spoiler(models.Model):
    title = models.ForeignKey(Title)
    spoiler_text = models.TextField()
    pub_date =  models.DateTimeField('Date Added')
    votes = models.IntegerField(default=0)
    # on tinyurl attr we can use the tinyurl_gen in it maybe?
    tinyurl = models.URLField(max_length=50, default='None yet', blank=True)

    @staticmethod
    def random_spoiler():
        from random import randint
        min = Spoiler.objects.earliest('id').pk
        max = Spoiler.objects.latest('id').pk
        return Spoiler.objects.filter(id__gte=randint(min, max))[0]

    # Use the tinyurl generator to cache spoilers tinyurls
    # Can generate url using spoiler.title_id and spoiler.pk
    def generate_spoiler_tinyurl(self, spoiler_id):
        url = 'http://spoiler.mrcricket.me/{}'.format(spoiler_id)
        tinyurl_for_cache = tinyurl_gen(url)
        return tinyurl_for_cache

    def __str__(self):
        return self.spoiler_text
