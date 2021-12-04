import requests
import random
import time
import webbrowser
import random
import sys
import requests
import curses

# List of 4chan boards, and dict to act as a cache for already looked up board catalogs
sfw_boards = [
    "a",
    "c",
    "w",
    "m",
    "cgl",
    "cm",
    "n",
    "jp",
    "vt",
    "v",
    "vg",
    "vm",
    "vmg",
    "vp",
    "vr",
    "vrpg",
    "vst",
    "co",
    "g",
    "tv",
    "k",
    "o",
    "an",
    "tg",
    "sp",
    "xs",
    "pw",
    "his",
    "asp",
    "int",
    "out",
    "toy",
    "po",
    "p",
    "ck",
    "lit",
    "mu",
    "vip",
    "fa",
    "3",
    "gd",
    "diy",
    "wsg",
    "qst",
    "biz",
    "trv",
    "fit",
    "x",
    "adv",
    "lgbt",
    "mlp",
    "news",
    "wsr",
]
nsfw_boards = [
    "r",
    "f",
    "i",
    "ic",
    "wg",
    "b",
    "r9k",
    "pol",
    "bant",
    "soc",
    "s4s",
    "s",
    "hc",
    "hm",
    "h",
    "e",
    "u",
    "d",
    "y",
    "t",
    "hr",
    "gif",
    "aco",
]
boards = [
    "a",
    "c",
    "w",
    "m",
    "cgl",
    "cm",
    "n",
    "jp",
    "vt",
    "v",
    "vg",
    "vm",
    "vmg",
    "vp",
    "vr",
    "vrpg",
    "vst",
    "co",
    "g",
    "tv",
    "k",
    "o",
    "an",
    "tg",
    "sp",
    "xs",
    "pw",
    "his",
    "asp",
    "int",
    "out",
    "toy",
    "po",
    "p",
    "ck",
    "lit",
    "mu",
    "vip",
    "fa",
    "3",
    "gd",
    "diy",
    "wsg",
    "qst",
    "biz",
    "trv",
    "fit",
    "x",
    "adv",
    "lgbt",
    "mlp",
    "news",
    "wsr",
    "r",
    "f",
    "i",
    "ic",
    "wg",
    "b",
    "r9k",
    "pol",
    "bant",
    "soc",
    "s4s",
    "s",
    "hc",
    "hm",
    "h",
    "e",
    "u",
    "d",
    "y",
    "t",
    "hr",
    "gif",
    "aco",
]
cache = {cache: "" for cache in boards}

# Returns random image URL, random image's thread URL
def getUrlAndThread(nsfw):
    board = random.choice(nsfw_boards) if nsfw else random.choice(sfw_boards)
    if cache[board] != "":
        data = cache[board]
    else:
        data = (requests.get("http://a.4cdn.org/" + board + "/catalog.json")).json()
        time.sleep(1)
        cache[board] = data

    threadnums = list()
    for page in data:
        for thread in page["threads"]:
            threadnums.append(thread["no"])
    thread = random.choice(threadnums)

    imgs = list()
    pd = (
        requests.get("http://a.4cdn.org/" + board + "/thread/" + str(thread) + ".json")
    ).json()
    time.sleep(1)
    for post in pd["posts"]:
        try:
            imgs.append(str(post["tim"]) + str(post["ext"]))
        except KeyError:
            pass

    image = random.choice(imgs)
    imageurl = "https://i.4cdn.org/" + board + "/" + image
    thread = "https://boards.4chan.org/" + board + "/thread/" + str(thread)
    return imageurl, thread


# functions that finds and open images with loading bar
def loadImages(stdscr, number_of_images, nsfw):
    urls = set()
    threads = list()
    for i in range(number_of_images):
        imageurl, thread = getUrlAndThread(nsfw)
        urls.add(imageurl)
        threads.append(thread)
        points = "#" * round(len(urls) / number_of_images * 50)
        stdscr.addstr(1, 0, f"{points}", curses.color_pair(1))
        stdscr.addstr(2, 0, f"{len(urls)}/{number_of_images}")
        stdscr.refresh()

    # opens all images in one batch
    for url in urls:
        webbrowser.open_new(url)

    return threads


# Initializes loading screen
def loading_screen(stdscr, number_of_images, nsfw):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Loading Images ...\n")
    stdscr.addstr("#" * 50, curses.color_pair(2))
    stdscr.addstr(f"\n0/{number_of_images}")
    stdscr.refresh()
    threads = loadImages(stdscr, number_of_images, nsfw)
    return threads


# Finds and opens images with loading bar
def main(number_of_images, nsfw=False):
    threads = curses.wrapper(loading_screen, number_of_images, nsfw)
    print("\nThreads:")
    for thread in threads:
        print(thread)


# ui to receive input in the console
def ui():
    print("\n'q' to quit")
    while True:
        inpt = input("\nNumber of random 4chan images: ")
        if inpt == "q":
            return
        nsfw = input("NSFW images (y/n): ")
        if inpt.isdigit():
            if nsfw == "y":
                main(int(inpt), nsfw=True)
            else:
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
