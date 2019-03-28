import requests
from PIL import Image
import json
import urllib.request
api_key = 'Tc41S7q6R90bBSNdzEOe6JXaXFCGHgTfF1syNFpM'
date = input("enter a date ex. yyyy-mm-dd:\n ")
api_key= f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

r = requests.get(api_key, params={"date": date})

api = r.json()

image = api['url']
with urllib.request.urlopen(image) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')

img.show()