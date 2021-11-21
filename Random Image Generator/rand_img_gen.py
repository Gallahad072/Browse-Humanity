import sys
import webbrowser
import random
import string
import requests
from PIL import Image
from io import BytesIO
import curses


# Returns a single valid url
def getValidUrl():
    while True:
        text = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        url = f"https://www.imgur.com/{text}.png"
        img = Image.open(BytesIO(requests.get(url).content))
        # filters out images with a width or hieght less than 100
        if (img.width and img.height) > 100:
            return url


# functions that finds and open images with loading bar
def loadImages(number_of_images, stdscr):
    urls = set()
    for i in range(number_of_images):
        urls.add(getValidUrl())
        points = "#" * round(len(urls) / number_of_images * 50)
        stdscr.addstr(1, 0, f"{points}", curses.color_pair(1))
        stdscr.addstr(2, 0, f"{len(urls)}/{number_of_images}")
        stdscr.refresh()

    # opens all images in one batch
    for url in urls:
        webbrowser.open_new(url)


# Initializes loading screen
def loading_screen(stdscr, number_of_images):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Loading Images ...\n")
    stdscr.addstr("#" * 50, curses.color_pair(2))
    stdscr.addstr(f"\n0/{number_of_images}")
    stdscr.refresh()
    loadImages(number_of_images, stdscr)


# Finds and opens images with loading bar
def main(number_of_images):
    curses.wrapper(loading_screen, number_of_images)


# ui to receive input in the console
def ui():
    print("\n'q' to quit\n")
    while True:
        inpt = input("Number of random images: ")
        if inpt == "q":
            break
        if inpt.isdigit():
            main(int(inpt))
        else:
            print("\n\TypeError: Value not digit\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inpt = sys.argv[1]
        if inpt.isdigit():
            main(int(inpt))
        else:
            print("\n\TypeError: Value not digit\n")
    else:
        ui()
