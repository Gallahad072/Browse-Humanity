import webbrowser
import random
import string


def prnt():
    text = "".join(random.choices(string.ascii_lowercase, k=2))
    ints = random.randint(0, 10000)
    url = f"www.prnt.sc/{text}{ints:04d}"
    webbrowser.open(url)


def imgur():
    text = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    url = f"www.imgur.com/{text}"
    webbrowser.open(url)


for i in range(10):
    prnt()
    # imgur()
