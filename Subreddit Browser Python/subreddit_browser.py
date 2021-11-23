import sys
import webbrowser
import urllib.request


# Opens random subreddits
def main(number_of_subreddits, nsfw=False):
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

    for url in urls:
        webbrowser.open(url)


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
