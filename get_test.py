import urllib.request
with urllib.request.urlopen("https://randomuser.me/api?callback=jsonData") as res:
   html = res.read().decode("utf-8")
   print(html)
