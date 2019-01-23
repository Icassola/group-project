import re
import csv

all_countries = {'Soviet Union'}

with open('noc_regions.csv') as countries_file:
    next(countries_file)
    for country in countries_file:
        country_name = country.split(',')[1]
        all_countries.add(country_name)

with open ("cleaned_data.csv") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    with open("try_me_data.csv",'w') as cleaned_file:
        writer = csv.DictWriter(cleaned_file, fieldnames=headers)
        writer.writeheader()
        for line in reader:
            country = line['nationality']
            if '{' in country:
                maybe_country = re.split(' |\|', country[1:-1])
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