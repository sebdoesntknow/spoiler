import requests

def tinyurl_gen(url):
    tinyurl_api = requests.get("http://tinyurl.com/api-create.php?url={}".format(url))
    return tinyurl_api.content.decode()
