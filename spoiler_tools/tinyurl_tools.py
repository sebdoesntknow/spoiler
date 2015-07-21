import requests
# These tools are intended to be loaded from the main spoiler app

# Convert original address to tinyurl using TU API.
def tinyurl_gen(url):
    tinyurl_api = requests.get("http://tinyurl.com/api-create.php?url={}".format(url))
    return tinyurl_api.content.decode()

# This function will require the Spoiler module loaded before using it.
# Maybe this should be integrated in the main view and add a successful redirect
# if the tinyurl value gets updated.
def tinyurl_field_checker(spoiler_id):
    import re
    from ..models import Spoiler

    right_url = re.compile('http://tinyurl.com/([a-zA-Z0-9]+)')
    sp = Spoiler.objects.get(pk=spoiler_id)

    if right_url.search(sp.tinyurl) is None:
        sp.tinyurl = sp.generate_spoiler_tinyurl(sp.pk)
        sp.save()
        
    return sp.tinyurl
