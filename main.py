import webbrowser
import random
import string
from PIL import Image
import requests
from io import BytesIO


def getUrls(reps):
    urls = set()
    for i in range(reps):
        text = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        urls.add(f"https://www.imgur.com/{text}.png")
    return urls


def getValidUrls(urls):
    valid_urls = set()

    for url in urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        not_found = Image.open("404.png")

        if img == not_found:
            continue
        else:
            valid_urls.add(url)

    return valid_urls


def openImages(reps):
    urls = getUrls(reps)
    valid_urls = getValidUrls(urls)
    for url in valid_urls:
        webbrowser.open_new(url)


print(
    """
Welcome to another fun waste of time.

This will open random images from imgur in your browser
    
    !!! WARNING: Images may be NSFW !!!

'q' to quit
"""
)
while True:
    reps = input("Number of urls to search: ")
    if reps == "q":
        break
    if reps.isdigit():
        openImages(int(reps))
    else:
        print("\n    ERROR: Enter a valid value\n")
