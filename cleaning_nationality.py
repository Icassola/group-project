import csv
import re

# create dictionary with cities being keys, countries - values
with open('test_csv.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    city_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (name, country, subcountry, geonameid ) = line
        city_dict[name] = country

# create dictionary with the regions/states
with open('test_csv.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    region_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (name, country, subcountry, geonameid ) = line
        region_dict[subcountry] = country

# create dictionary with the demonyms 
with open('demonym.csv', encoding='utf-8') as file: 
    reader = csv.reader(file)
    next(reader)
    demonym_dict = {} # initialize dictionary
    for line in reader: # for 2nd line onward
        (Nationality, Country) = line
        demonym_dict[Nationality] = Country
# create a set with country names 
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
            tokens = []
            for field in split_line[1:4]:
                if field != "NULL":
                    elements = field[1:-1].split('|') if '{' in field else [field]
                    for element in elements:
                        tokens.append(element)
                        if ' ' in element:
                            for word in element.split(' '):
                                tokens.append(word)
            #print(tokens)

            nationality = None
            for token in tokens:
                if token in all_countries:
                    nationality = token
                    break
            
            for ref_dict in [city_dict, demonym_dict, region_dict]:
                if nationality is None:
                    for token in tokens:
                        if token in ref_dict:
                            nationality = ref_dict[token]
                            break

            ''' 
            nationality = split_line[1] # value from birth_place column
            if nationality == "NULL": # if birth_place == NULL
                nationality = split_line[2] # replace with value from nationality column
            '''

            # remove columns: nationality, medal, labels
            del(split_line[5])
            del(split_line[4])
            del(split_line[2])

            '''
            # extract country from {..|..} format and format {eastern germany|city}
            if '{' in nationality:
                maybe_country = nationality[1:-1].split('|')
                for element in maybe_country:
                    if element in all_countries:
                        nationality = element
                        break
            if '{' in nationality:
                maybe_country = re.split(' |\|', nationality[1:-1])
                #print(maybe_country)
                for element in maybe_country:
                    if element in all_countries:
                        nationality = element
                        break
            
            # turn city names into country
            if nationality not in all_countries:
                if nationality in city_dict:
                    nationality = city_dict[nationality]
            # turn city into country for the format {city|value}
                if '{' in nationality:
                    maybe_country = nationality[1:-1].split('|')
                    for element in maybe_country:

                        if element in city_dict.keys():
                            nationality = city_dict[element]
            '''
                            
            print(nationality)
              
            split_line[1] = nationality
            writer.writerow(split_line)


# create dictionary: city->country
# create set of all countries

# starting with original file: data_for_r_1.csv (subselection of olympic medalists 1950-1980, using CLI)
# if birth_place == NULL, replace with value from nationality column
# some values of birth_place were in the format {value|value}: if either is in set all_countries, replace birth_place with this value
# sometimes birth_place was {eastern germany | city_name}, in which case split by | and ' ' to extract Germany
# sometimes birth_place is a city name. If not in all_countries, check if it is a key in city_dict, and if so, return country
# Write each row to a new (cleaned) csv file, calling birth_place column 'nationality'