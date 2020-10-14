import urllib.request

url = "https://www.python.org/static/img/python-logo@2x.png"
urllib.request.urlretrieve(url, "python.png")