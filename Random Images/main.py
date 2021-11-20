import webbrowser
import random
import string
import requests
from PIL import Image
from io import BytesIO


def getImages(number_of_images):
    valid_urls = set()
    while len(valid_urls) != number_of_images:
        text = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        url = f"https://www.imgur.com/{text}.png"
        img = Image.open(BytesIO(requests.get(url).content))
        if (img.width and img.height) > 100:
            valid_urls.add(url)

    for url in valid_urls:
        webbrowser.open_new(url)


def main():
    print(
        """
Welcome to another fun waste of time.

This will open random images from imgur in your browser
    
    !!! WARNING: Images may be NSFW !!!

'q' to quit
"""
    )
    while True:
        inpt = input("Number of random images: ")
        if inpt == "q":
            break
        if inpt.isdigit():
            getImages(int(inpt))
        else:
            print("\n    ERROR: Enter a valid value\n")


if __name__ == "__main__":
    main()
