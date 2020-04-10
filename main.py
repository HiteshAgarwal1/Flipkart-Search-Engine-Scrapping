from bs4 import BeautifulSoup
import urllib
import json
import ssl
import re

# Ignore SSL Certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask Prouct to Search
product = input("Enter Product For Search: ")
product.replace(' ','+')

# Try to fetch data
try:
    print("Trying to fetch data...")
   
    # Fetch data
    fhand = urllib.request.urlopen('https://www.flipkart.com/search?q='+product, context=ctx).read()
   
    # Transform our code in well understand format
    soup = BeautifulSoup(fhand, 'html.parser')
    
    #Extract Price
    price=soup.find_all('div', attrs={"class" : "_1vC4OE"})
    #Extract Price
    rate=soup.find_all('div', attrs={"class" : "hGSR34"})
    img=soup.find_all('div', attrs={"class" : "_3togXc"})
    
    # Extracting the Script
    final=soup.find('script', type="application/ld+json")
   
    print("Recommended Products on",product.replace('+',' '))
   
    # Parsing Code into json structure and iterrate through each item found
    for i,item in enumerate(json.loads(final.text)['itemListElement']):
        print(i+1,item['name'], price[i].text, rate[i].text)
        

except:
    print("Error in fetching the data. Try Again!")
