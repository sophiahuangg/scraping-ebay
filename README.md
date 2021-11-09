# scraping-ebay

### What does the ebay-dl.py file do?
In this homework, I webscraped Ebay for key terms. This file searches for the name, price, status, shipping, number sold, and status of Ebay items. This was done through using `BeautifulSoup`. The output resulted in JSON files and CSV files.

Things you may need to import:
    
    import argparse
    import requests
    from bs4 import BeautifulSoup
    import json
    import pandas as pd
    
### How do you run the ebay-dl.py file?

I ran my file using the following commands to create json files: 

    python3 ebay-dl.py 'haruki murakami'

    python3 ebay-dl.py 'peppa pig'

    python3 ebay-dl.py 'f1'

The following commands can be run to create csv files:

    python3 ebay-dl.py 'haruki murakami' --csv

    python3 ebay-dl.py 'peppa pig' --csv

    python3 ebay-dl.py 'f1' --csv
    
The general format is: 

    python3 ebay-dl.py SEARCH_TERM
    
The csv file is generated through this argument:

    parser.add_argument('--csv', action='store_true')
    
I used `pandas` to generate my csv files. Here are some helpful resources to learn how to do that:

1. [JSON To CSV In Python: How To Convert JSON To CSV by Krunal](https://appdividend.com/2020/04/26/python-json-to-csv-how-to-convert-json-string-to-csv/)
2. [Stack Overflow](https://stackoverflow.com/questions/50558077/convert-json-to-csv-with-pandas)

    

The search term is the word you want to extract information about. Note that the use of single quotes will let Python read `'basketball cards'` as one term instead of searching two separate words (which could produce an error). If you get a `[Errno 2] No such file or directory` error, make sure to check your working directory! More information on how to do that can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/week_06).

**The link to course project can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)**
