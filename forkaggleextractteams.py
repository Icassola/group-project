import csv
with open('athletes_year.csv') as file:
    reader = csv.DictReader(file)
    for entry in reader:
        if 'Great Britain' in entry['Team']:
            

#if 'United States' in entry['Team']
#if 'Russia' in entry['Team']
       # if 'China' in entry['Team']