import webbrowser
import random
import string

# This is a very primitve version of getting random images

#  gets random lightshot pics


def prnt():
    text = "".join(random.choices(string.ascii_lowercase, k=2))
    ints = random.randint(0, 10000)
    url = f"www.prnt.sc/{text}{ints:04d}"
    webbrowser.open(url)


for i in range(10):
    prnt()
