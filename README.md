# scraping-ebay

### What does the `ebay-dl.py` file do?
In this homework, I webscraped Ebay for key terms. This file searches for the name, price, status, shipping, number sold, and status of Ebay items. This was done through using `BeautifulSoup`. The output resulted in JSON files.

### How do you run the `ebay-dl.py` file?

I ran my file using the following commands: 

`python3 ebay-dl.py 'baketball cards'`

`python3 ebay-dl.py 'octopus'`

`python3 ebay-dl.py 'beans'`

The general format is `python3 ebay-dl.py SEARCH_TERM`. The search term is the word you want to extract information about. Note that the use of single quotes will let Python read `'basketball cards'` as one term instead of searching two separate words (which could produce an error). If you get a `[Errno 2] No such file or directory` error, make sure to check your working directory! More information on how to do that can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/week_06).

**The link to course project can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)**
