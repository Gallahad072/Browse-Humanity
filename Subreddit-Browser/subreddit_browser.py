import sys
import curses
import webbrowser
import urllib.request


# Opens random subreddits
def loadSubreddits(stdscr, number_of_subreddits, nsfw):
    urls = set()
    url_end = "randnsfw" if nsfw else "random"
    url = "https://www.reddit.com/r/" + url_end
    while len(urls) != number_of_subreddits:
        req = urllib.request.Request(url=url)
        try:
            resp = urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            continue
        urls.add(resp.url)
        points = "#" * round(len(urls) / number_of_subreddits * 50)
        stdscr.addstr(1, 0, f"{points}", curses.color_pair(1))
        stdscr.addstr(2, 0, f"{len(urls)}/{number_of_subreddits}")
        stdscr.refresh()

    for url in urls:
        webbrowser.open(url)


# Initializes loading screen
def loading_screen(stdscr, number_of_subreddits, nsfw):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Loading Subreddits ...\n")
    stdscr.addstr("#" * 50, curses.color_pair(2))
    stdscr.addstr(f"\n0/{number_of_subreddits}")
    stdscr.refresh()
    loadSubreddits(stdscr, number_of_subreddits, nsfw)


# Finds and opens subreddits with loading bar
def main(number_of_subreddits, nsfw=False):
    curses.wrapper(loading_screen, number_of_subreddits, nsfw)


# ui to receive input in the console
def ui():
    print("\n'q' to quit\n")
    while True:
        inpt = input("Number of random subreddits: ")
        if inpt == "q":
            return
        nsfw = input("NSFW subreddits (y/n): ")
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
        nsfw = sys.argv[2] if len(sys.argv) == 3 else False
        if inpt.isdigit():
            if nsfw == "nsfw":
                main(int(inpt), nsfw=True)
            else:
                main(int(inpt))
        else:
            print("\n\TypeError: Value not digit\n")
    else:
        ui()
