# Went thru manually and just saved each page of records as an html
# Collect page on one performance
import urllib
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import re
from datetime import datetime
import pandas as pd
import os

# Extracing clinic information
# Doing one file at a time -- I just replaced the html file in the first beautiful soup line
name = []
license_type = []
city =[]
zip = []
county = []
i = 0
soup = BeautifulSoup(open("/Users/katelyons/Documents/Insight/cdc/clinics_counties/clinic_sonoma_yuba.html", encoding = 'utf-8'), "html.parser")
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
clinic_sonoma_yuba = pd.DataFrame({'name': name, # Make our data frame
                   'license_type': license_type,
                   'city': city,
                   'county': county,
                   'zip': zip})

# Save for later just in case
clinic_sonoma_yuba.to_csv('clinic_sonoma_yuba.csv')

# Combine all of these
# Was able to do this with enviro variables because I created them before -- if you are doing this anew you'll have to load in those csvs
allclinics = pd.concat([clinic_alameda_fresno, clinic_glenn_madera, clinic_marin_nevada,clinic_orange_sanfrancisco,clinic_sanjoaquin_solano,clinic_sonoma_yuba])
# Then we will group by COUNTY and create a new data frame of those groupings
clinicxcounty = allclinics.groupby('county')
clinics_per_county = clinicxcounty['name'].nunique().sort_values(ascending=False).reset_index()
clinics_per_county
clinics_per_county.to_csv('clinics_per_county.csv')


# Stich everything together
# Reading in pharmacy files we scraped earlier
pharm1 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_acton_bell.csv')
pharm2 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_alameda_fresno.csv')
pharm3 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_bellgarden_cerritos.csv')
pharm4 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_chatsworth_elmonte.csv')
pharm5 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_elsegundo_hawthorne.csv')
pharm6 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_glenn_lassen.csv')
pharm7 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_hermosabeach_lakewood.csv')
pharm8 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_la_lacity.csv')
pharm9 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_lancaster_marinadelray.csv')
pharm10 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_madera_nevada.csv')
pharm11 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_maywood_northhills.csv')
pharm12 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_northhollywood_pasadena.csv')
pharm13 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_orange.csv')
pharm14 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_pearblossom_rowlandheights.csv')
pharm15 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_placer_sanbenito.csv')
pharm16 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_sanbernardino_sandiego.csv')
pharm17 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_sandimas_sierramadre.csv')
pharm18 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_santacruz_trinity.csv')
pharm19 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_sf_santaclara.csv')
pharm20 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_signalhill_tarzana.csv')
pharm21 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_templecity_vannuys.csv')
pharm22 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_tulare_yuba.csv')
pharm23 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_venice_winnetka.csv')
pharm24 = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/pharm_data/pharma_woodlandhills.csv')

allpharms = pd.concat([pharm1, pharm2, pharm3, pharm4, pharm5, pharm6, pharm7, pharm8, pharm9, pharm10, pharm11, pharm12, pharm13, pharm14, pharm15, pharm16, pharm17, pharm18, pharm19, pharm20, pharm21, pharm22, pharm23, pharm24])

# Sometimes county has city instead because of formatting changes when a pharmacy has a complaint

# When county says the complain type it's in mixed case, so we can filter it out this way
test = allpharms[allpharms['county'].str.istitle()]

# Keep all ones that are correct
test2 = allpharms[allpharms['county'].str.isupper()]

# Fix the previous one so we have county stuff
test['county'] = test['city']

# Make a new pharmacy df
allpharms = pd.concat([test,test2])

counties = clinics_per_county['county']
type(counties)
counties_df = counties.to_frame()
allpharms

# Do a group by to get counts per county and zip
pharmaxcounty = allpharms.groupby('county')
pharma_per_county = pharmaxcounty['name'].nunique().sort_values(ascending=False).reset_index()
pharma_per_county

# We still have cities listed instead of county, so filter these out by joining with a df that has just counties
pharma_per_county2 = pd.merge(pharma_per_county,counties_df, how = 'inner', on = 'county')
pharma_per_county = pharma_per_county2
pharma_per_county.to_csv('pharma_per_county.csv')

# Hospital
# This data is from the CA open data project so we can just load in the CSV and group by
hospital = pd.read_csv('/Users/katelyons/Documents/Insight/cdc/cdc_dc/licensed-healthcare-facility-listing-june-30-2018.csv')

hospital.head(5)
# COUNTY_NAME
hospitalxcounty = hospital.groupby('COUNTY_NAME')
hospital_per_county = hospitalxcounty['FACILITY_NAME'].nunique().sort_values(ascending=False).reset_index()
hospital_per_county
hospital_per_county.to_csv('hospital_per_county.csv')


# Zip codes
# Same thing for zip codes
pharmaxzip = allpharms.groupby('zip')
pharma_per_zip = pharmaxzip['name'].nunique().sort_values(ascending=False).reset_index()
pharma_per_zip.to_csv('pharma_per_zip.csv')

clinicxzip = allclinics.groupby('zip')
clinics_per_zip = clinicxzip['name'].nunique().sort_values(ascending=False).reset_index()
clinics_per_zip
clinics_per_zip.to_csv('clinics_per_zip.csv')
#
hospitalxzip = hospital.groupby('DBA_ZIP_CODE')
hospital_per_zip = hospitalxzip['FACILITY_NAME'].nunique().sort_values(ascending=False).reset_index()
hospital_per_zip
hospital_per_zip.to_csv('hospital_per_zip.csv')


# Combine these all together
len(hospital_per_zip)
len(clinics_per_zip)
len(pharma_per_zip)

# Do pharmacies first then hospitals then clinics
hospital_per_zip['DBA_ZIP_CODE'] = hospital_per_zip['DBA_ZIP_CODE'].astype(str)

hospital_per_zip['DBA_ZIP_CODE']=hospital_per_zip['DBA_ZIP_CODE'].str.replace(" ","")
clinics_per_zip['zip']=clinics_per_zip['zip'].str.replace(" ","")

pharma_per_zip['zip'] = pharma_per_zip['zip'].astype(str)
pharma_per_zip['zip'] = pharma_per_zip['zip'].str.replace(" ","")

merge1 = pd.merge(pharma_per_zip, hospital_per_zip, how = 'left', on = 'zip')
hospital_per_zip.columns
pharma_per_zip.columns

# So we can merge, rename
hospital_per_zip.rename(columns={'DBA_ZIP_CODE':'zip','FACILITY_NAME': 'no_facilities'},inplace=True)

merge1 = pd.merge(pharma_per_zip, hospital_per_zip, how = 'left', on = 'zip')
merge1

merge2 = pd.merge(merge1, clinics_per_zip, how = 'left', on = 'zip')

# Get rid of NaNs so we can merge
all_facilities = merge2.fillna(0)
all_facilities.head(2)

all_facilities['total_facils'] = all_facilities['name_x']+all_facilities['no_facilities']+all_facilities['name_y']
all_facilities.columns
all_facilities_by_zip = all_facilities[['zip','total_facils']]
all_facilities_by_zip

# Add on pop info
# Got this from a CA demographics website
# We can just read it in!
zip_population = pd.read_csv('/Users/katelyons/Documents/Insight/cdc2/zip_population.csv')

zip_population.head(5)
zip_population['zip'] = zip_population['zip'].astype(str)

zip_per_cap = pd.merge(all_facilities_by_zip,zip_population, how = "left", on = "zip")

zip_per_cap.population.isnull().value_counts()

len(all_facilities_by_zip)
len(zip_per_cap)

# Again, formatting changes so we can add things up
zip_per_cap['population'] = zip_per_cap['population'].str.replace(",","")
zip_per_cap = zip_per_cap.fillna(0)
zip_per_cap['population'] = zip_per_cap['population'].astype(int)


zip_per_cap['per_capita'] = zip_per_cap['total_facils']/zip_per_cap['population']

zip_per_cap

zip_per_cap.to_csv('zip_per_cap.csv')
