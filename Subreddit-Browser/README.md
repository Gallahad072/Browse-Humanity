# Subreddit Browser

Welcome to another fun waste of time.

This [program](subreddit_browser.py) will open random subreddits in your browser.

**_!!! WARNING: content can be NSFW, must be 18+ to use NSFW mode !!!_**

## Instructions

You can use it two ways:

---

**Run the python file and use the UI**

Type in the terminal:

`python subreddit_browser.py`

The UI will then prompt an input.

```
'q' to quit

 Number of random subreddits: number_of_subreddits
 NSFW subreddits (y/n): n
```

> Pass in the number of subreddits wanted as a variable.

---

**Put the number of subreddits you want to open as an argument in your terminal**

Type in the terminal:

`python subreddit_browser.py number_of_subreddits `

> Pass in the number of subreddits wanted as a variable.
>
> For nsfw content add the argument nsfw:

`python subreddit_browser.py number_of_subreddits nsfw`

## Import

On importing this as a module run:

`main(number_of_subreddits, nsfw=False)`

> Finds and opens subreddits
>
> Pass in the number of subreddits wanted as a variable.
> Pass in True to nsfw for NSFW subreddits

`ui()`

> This will run the main program with a ui to input number of subreddits and select nsfw
