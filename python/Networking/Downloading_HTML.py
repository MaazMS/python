import urllib.request
from  urllib import error
try:
	url = urllib.request.urlopen("https://wiki.python.org/moin/BeginnersGuide/Programmers ")
	content = url.read()
	url.close()

except urllib.error.HTTPError:
	print("not found")
	exit()

f = open("python.html", 'wb')
f.write(content)
f.close()