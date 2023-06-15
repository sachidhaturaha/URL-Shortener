import pyshorteners

url = input("Enter the url you want to shorten: ")

def shorten_url(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shorten_url(url)