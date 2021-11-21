# Random Image Generator

Welcome to another fun waste of time.

This [program](main.py) will open random images from imgur in your browser.

**_!!! WARNING: Images may be NSFW, must be 18+ !!!_**

## Instructions

You can use it two ways:

---

**Run the python file and use the UI**

Type in the terminal:

`python rand_img_gen.py`

The UI will then prompt an input.

```
'q' to quit

 Number of random images: number_of_images
```

> Pass in the number of images wanted as a variable.

---

**Put the number of images you want to open as an argument in your terminal**

Type in the terminal:

`python rand_img_gen.py number_of_images`

> Pass in the number of images wanted as a variable.

## Import

On importing this as a module, one could either run:

`main(number_of_images)`

> Finds and opens images with loading bar.
>
> Pass in the number of images wanted as a variable.

`ui()`

> This will run the main program with a ui to input number of images

`getValidUrl()`

> This will return a valid url (one that contains an image of a sensible size).
