import sys
import webbrowser
import random
import string
import requests
from PIL import Image
from io import BytesIO


# functions that finds and open images
def getImages(number_of_images):
    valid_urls = set()
    while len(valid_urls) != number_of_images:
        text = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        url = f"https://www.imgur.com/{text}.png"
        img = Image.open(BytesIO(requests.get(url).content))
        # filters out images with a width or hieght less than 100
        if (img.width and img.height) > 100:
            valid_urls.add(url)

    # opens all images in one batch
    for url in valid_urls:
        webbrowser.open_new(url)


# ui to receive input in the console
def main():
    print("\n'q' to quit\n")
    while True:
        inpt = input("Number of random images: ")
        if inpt == "q":
            break
        if inpt.isdigit():
            getImages(int(inpt))
        else:
            print("\n\TypeError: Value not digit\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inpt = sys.argv[1]
        if inpt.isdigit():
            getImages(int(inpt))
        else:
            print("\n\TypeError: Value not digit\n")
    else:
        main()
