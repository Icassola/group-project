# This script was used to clean the nationality variable for each athlete and to get unique entrances only

import csv
import re

# create dictionary with cities being keys, countries - values
# the all cities csv can be found here: https://github.com/datasets/world-cities
with open('all_cities.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    city_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (name, country, subcountry, geonameid ) = line
        city_dict[name] = country

# create dictionary with the regions/states
with open('all_cities.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    region_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (name, country, subcountry, geonameid ) = line
        region_dict[subcountry] = country

# create dictionary with the demonyms 
# The demonym.csv can be found here: https://github.com/knowitall/chunkedextractor/blob/master/src/main/resources/edu/knowitall/chunkedextractor/demonyms.csv
with open('demonym.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    demonym_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (Nationality, Country) = line
        demonym_dict[Nationality] = Country
# create a set with country names 
# The noc_regions.csv can be found here: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results
all_countries = {'Soviet Union'} # Initialize with Soviet Union, as it is not in list of countries
with open('noc_regions.csv') as countries_file:
    next(countries_file)
    for country in countries_file:
        country_name = country.split(',')[1]
        all_countries.add(country_name)

#  line['name'] = line['name'].split('(')[0].strip()  

# find nationality of people and correct in a new csv file     
with open ('data_for_r_1.csv', "r") as file:
    with open('cleaned_nationality.csv', "w") as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['name', 'nationality', 'sport']) # write headers of new csv file
        next(file) # skip header row of input file
        for line in file.readlines(): 
            split_line = line.split(',')
            nationality_elements = []
            for field in split_line[1:4]:
                if field != "NULL":
                    elements = field[1:-1].split('|') if '{' in field else [field]
                    for element in elements:
                        nationality_elements.append(element)
                        if ' ' in element:
                            for word in element.split(' '):
                                nationality_elements.append(word)
            #print(tokens)

            nationality = None
            for token in nationality_elements:
                if token in all_countries:
                    nationality = token
                    break
            
            for ref_dict in [city_dict, region_dict, demonym_dict]:
                if nationality is None:
                    for token in nationality_elements:
                        if token in ref_dict:
                            nationality = ref_dict[token]
                            break
            # remove columns: nationality, medal, labels
            del(split_line[5])
            del(split_line[4])
            del(split_line[2])              
            #print(nationality)
              
            split_line[1] = nationality
            writer.writerow(split_line)

# get rid of duplicates in names ., one line per athlete

newname = []
with open ('cleaned_nationality.csv') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    with open('person_per_line_dbp.csv', 'w', newline = '') as newfile: 
        writer = csv.DictWriter(newfile, fieldnames = headers)
        writer.writeheader()
        for line in reader:
            name = line['name']
            if name not in newname:
                newname.append(name)
                writer.writerow(line)