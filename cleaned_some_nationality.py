# curly stuff

import csv
all_countries = {'Soviet Union'}

with open('noc_regions.csv') as countries_file:
    next(countries_file)
    for country in countries_file:
        country_name = country.split(',')[1]
        all_countries.add(country_name)

#print(all_countries)
#print(f'Is Mozambique a country? {"Mozambique" in all_countries}')

people = []
with open ("new_data.csv") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    with open("cleaned_data.csv",'w') as cleaned_file:
        writer = csv.DictWriter(cleaned_file, fieldnames=headers)
        writer.writeheader()
        for line in reader:
            #name = line['name']
            #new_name = (name.split('(')[0].strip())
            line['name'] = line['name'].split('(')[0].strip()      
            #people.append(new_name)
            country = line['nationality']
            if '{' in country:
                maybe_country = country[1:-1].split('|')
                for element in maybe_country:
                    if element in all_countries:
                        line['nationality'] = element
                        #people.append(line)
                        break
                

            elif country != 'NULL':
                if country in all_countries:
                    line['nationality'] = country
                    #people.append(line)
            writer.writerow(line)

                    
#print(people)
                
#print(people)

        #print(country)
        #split_nationality = line.split(',')[1]
        #if '{' in split_nationality:
        #    country = split_nationality[1:-1].split('|')[0]
        #print(country)'''

#entry = 'Mária Vadász,{Hungary|Környe},Hungarian handball player'

#split_entry = entry.split(',')[1]

#if '{' in split_entry:
    #country = split_entry[1:-1].split('|')[0]

#print(country)

#lets find countries in {} in the column nationality 
# I have a csv file with the second column being a country
# have to split the line 
# get rid of {}
# magic
# then check if one of the values is equal to the country name in the csv document then keep only that one 
# magic
