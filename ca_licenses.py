# Went thru manually and just saved each page of records as an html
# Collect page on one performance
import urllib
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re
from datetime import datetime
import pandas as pd
import os

# Create a BeautifulSoup object
# Had to re-do this and re-save due to weird CA pharma board stuff
# Wanted to keep track of how many I was getting for each thing just in case?
# Actually don't know why I did this, not really necessary but OH WELL

# For Alameda Fresno 648
# For Glenn to Lassen 232

# Los Angeles Acton to Bell 83
# Los Angeles Bell Gardens to Cerritos 143
# Los Angeles LA 395
# Los Angeles CHATSWORTH to El Monte 118
# Los Angeles El Segundo to Hawthorne 187
# Los Angeles Hermosa Beach to Lakewood 247
# Los Angeles Lancaster to Marina Del Rey 133
# Los Angeles Maywood to North Hills 60
# Los Angeles North Hollywood to Pasadena 164
# Los Angeles Pearblossom to Rowland Heights 99
# Los Angeles San Dimas to Sierra Madre 129
# Los Angeles Signal Hill to Tarzana 67
# Los Angeles Temple City to Van Nuys 116
# Los Angeles Venice to Winnetka 84
# Los Angeles Woodland Hills 20

# Madera to Nevada 224
# Orange 681
# Placer to San Benito 707
# San Bernandino to San Diego 796
# San Francisco to Santa Clara 733
# Santa Cruz to Trinity 340

# First series of things to see how this all works
# Read in the html
soup = BeautifulSoup(open("/Users/katelyons/Documents/Insight/cdc/pharms/pharma_glenn_lassen.htm", encoding = 'utf-8'), "html.parser")

# Can be illustrative to look at data directly (not really in this case)
# soup

# Thanks to Abhilash, we know 'article' is where all of our info is so let's take a note of all of those tags
articles = soup.find_all('article')

# We'll access each entry by its index, so just want to see how big this thing is to know what I can/can't index
len(articles)

# Let's look at a random one
firstBigTag = soup.find_all('article')[100]
# Get name
name = firstBigTag.li.text
name
# Get license type
license_type = firstBigTag.li.find_next('li').find_next('li').text

# Get city name and other geo factors like county and zip
city_code = firstBigTag.find_all('span')
city = city_code[1].text

# Did this to see what we have
city_code

geo_stuff = firstBigTag.find_all('strong')
county = geo_stuff[7].nextSibling
zip = geo_stuff[8].nextSibling

# Will this work for other entries? (Test to see how iteration might work)
nextATag = soup.find_all('article')[101] # Just changed the index
nextATag.li.text
nextATag.li.find_next('li').find_next('li').text
next_code = nextATag.find_all('span')
next_code[1].text
geo_stuff_next = nextATag.find_all('strong')
geo_stuff_next[7].nextSibling
geo_stuff_next[8].nextSibling

# Yep seems to work!

# Put this into a big loop
name = []
license_type = []
city =[]
zip = []
county = []
i = 0

# How many of these do we have? We want to just increase that index, that will get us all the entries we want
# Or if we get a nothing... just keep going
# Go through to each htm file
# Give it the base directory
directory_address = '/Users/katelyons/Documents/Insight/cdc/pharms'
directory = os.fsencode(directory_address)

# Tell it to work thru the directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".htm"):
        soup = BeautifulSoup(open(directory_address+'/'+filename, encoding = 'utf-8'), "html.parser")
        articles = soup.find_all('article')
        while i < len(articles): # This way we'll hopefully avoid an Index Error, but we have the try statement down there just in case
            firstBigTag = soup.find_all('article')[i] # This will go thru all of our entries
            # Get name
            try:
                name_temp = firstBigTag.li.text # Get name
                name.append(name_temp)
                # Get license type
                license_type_temp = firstBigTag.li.find_next('li').find_next('li').text
                license_type.append(license_type_temp)
                # Get city name and other geo factors like county and zip
                city_code = firstBigTag.find_all('span')
                city_temp = city_code[1].text
                city.append(city_temp)
                geo_stuff = firstBigTag.find_all('strong')
                county_temp = geo_stuff[7].nextSibling
                county.append(county_temp)
                zip_temp = geo_stuff[8].nextSibling
                zip.append(zip_temp)
            except IndexError: # In case something happens where we try to index something that doesn't exit
                continue
            i += 1 # Increase our counter
        pharms = pd.DataFrame({'name': name, # Make our data frame
                           'license_type': license_type,
                           'city': city,
                           'county': county,
                           'zip': zip})
pharms
