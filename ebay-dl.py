import argparse
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# Extra credit: accepts a new command line flag --csv. 
# Whenever this flag is specified, the output file should be saved in csv format instead of json format
# Generate 3 csv files in addition to the 3 json files and include them in your repo
# Modify your README.md file to include instructions and examples on how to use the --csv flag.
def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string.

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''

    numbers=''
    for char in text:
        if char in '1234567890':
            numbers+=char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0


def parse_status(text):
    '''
    Takes as input a string and returns the status of the item, as specified in the string.

    >>> parse_status('Brand New')
    'Brand New'
    >>> parse_status('Refurbished')
    'Refurbished'
    >>> parse_status('Pre-Owned')
    'Pre-Owned'
    '''

    status=''
    if 'Brand New' in text: 
        status='Brand New'
        return status
    elif 'Refurbished' in text:
        status='Refurbished'
        return status
    elif 'Pre-Owned' in text:
        status='Pre-Owned'
        return status
    else:
        return 0

def parse_shipping(text):
    '''
    Takes as input a string and returns the price of shipping the item in cents, stored as an integer.

    >>> parse_shipping('Free 3 day shipping')
    0
    >>> parse_shipping('+$12.00 shipping')
    1200
    >>> parse_shipping('+$6.91 shipping')
    691
    >>> parse_shipping('Free shipping')
    0
    '''
 
    shipping=''
    for char in text:
        if char in '1234567890':
            shipping+=char
    if '$' in text: 
        return int(shipping)     
    else:
        return 0
  

def parse_price(text):
    '''
    Takes as input a string and returns the price of shipping the item in cents, stored as an integer.

    >>> parse_price('$10.69')
    1069
    >>> parse_price('$24.58 to $142.30')
    2458
    >>> parse_price('$18.95 to $19.95')
    1895
    >>> parse_price('$9.99')
    999
    '''
    
    price=''
    if '$' not in text:
        return 0
    if ' ' in text:
        new=text.split()
        text=new[0]
    for char in text:
        if char in '1234567890' :
            price+=char
    return int(price)
  

# this if statement says only run the code below when the python file is run "normally"
# where normally means not in the doctests
if __name__ =='__main__':
    # get command line arguments
    parser=argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)

    #parser=argparse.ArgumentParser(description='Download information from ebay and convert to CSV.')
    parser.add_argument('--csv', action='store_true')

    args = parser.parse_args()
    print('args.search_term=', args.search_term)


    #list of all items found in all ebay webpages
    items=[]

    #loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):

        #build the url
        url='https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url+= args.search_term
        url+= '&_sacat=0&LH_TitleDesc=0&_pgn='
        url+= str(page_number)
        url+='&rt=nc'
        print('url=',url)

        #download the html
        r=requests.get(url)
        status=r.status_code
        print('status=', status)
        html=r.text

        # process the html
        soup=BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items= soup.select('.s-item')
        for tag_item in tags_items:
            
            name=None
            tags_name= tag_item.select('.s-item__title')
            for tag in tags_name:
                name=tag.text

            freereturns=False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns=True
            
            items_sold = None
            tags_itemssold = tag_item.select( '.s-item__hotness')
            for tag in tags_itemssold:
                items_sold=parse_itemssold(tag.text)
                print('tag=', tag)


            shipping=None
            tags_shipping = tag_item.select( '.s-item__shipping')
            for tag in tags_shipping:
                shipping=parse_shipping(tag.text)
                print('tag=', tag)


            price=None
            tags_price = tag_item.select( '.s-item__price')
            for tag in tags_price:
                price=parse_price(tag.text)
                print('tag=', tag)

            status=None
            tags_status=tag_item.select('.SECONDARY_INFO')
            for i in tags_status:
                status=i.text
            
            item={
                'name':name,
                'freereturns': freereturns,
                'items_sold': items_sold,
                'shipping': shipping,
                'price': price,
                'status': status
            }
            items.append(item)


            
        
        print('len(tags_items)=', len(tags_items))
        print('len(items)=',len(items))

        # write the json to a file
        filename=args.search_term+'.json'
        with open(filename, 'w', encoding='ascii') as f:
            f.write(json.dumps(items))


        
        # write the csv to a file
        if args.csv:
            df = pd.read_json(filename)
            filename1=args.search_term+'.csv'
            df.drop([0],inplace=True)
            df=df.convert_dtypes('Int64')
            df.to_csv(filename1, index = False)
            
               
