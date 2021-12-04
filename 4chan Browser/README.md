# 4chan Browser Python

Welcome to another fun waste of time.

This [program](4chan_browser.py) will open random images from 4chan in your browser.

**_!!! WARNING: content can be NSFW, must be 18+ to use NSFW mode !!!_**

## Instructions

You can use it two ways:

---

**Run the python file and use the UI**

Type in the terminal:

`python 4chan_browser.py`

The UI will then prompt an input.

```
'q' to quit

 Number of random images: number_of_images
 NSFW images (y/n): n
```

> Pass in the number of posts wanted as a variable.

---

**Put the number of images you want to open as an argument in your terminal**

Type in the terminal:

`python 4chan_browser.py number_of_images`

> Pass in the number of images wanted as a variable.

## Functions

`main(number_of_images, nsfw=False)`

> Finds and opens images
>
> Pass in the number of images wanted as a variable.
> Pass in True to nsfw for NSFW images

`ui()`

> This will run the main program with a ui to input number of images

`getUrlAndThread(nsfw)`

> Returns image URL and thread URL
>
> Pass in the number of images wanted as a variable.
> Pass in True to nsfw for NSFW images
