import pyshorteners
url=input("enter the url:")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)