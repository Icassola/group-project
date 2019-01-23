import csv

#Creating a new CSV which only includes athletes that won a medal when they participated:
athletes_medal = []
with open('athlete_events.csv', 'r') as athletes:
    with open('athletes_medals.csv', 'w') as file:
        for line in athletes:
            if line[-3:-1] != 'NA':
                file.write(line)

#Keeping the file headers from this file, for use in the next file + the addition of BirthYear header.
with open('athletes_medals.csv', 'r') as athletes:
    reader = csv.DictReader(athletes)
    headers = reader.fieldnames
    headers.append('BirthYear')

#Writing a new file and calculating the the birth year of each athlete based on known year of participation and age of athlete.
    with open('athletes_year .csv', 'w', newline ='') as athletesyears:
        writer = csv.DictWriter(athletesyears, fieldnames=headers)
        writer.writeheader()
        for line in reader: 
            if line['Age'] != 'NA':
                birthyear = int(line['Year']) - int(line['Age'])
                line['BirthYear'] = birthyear
                writer.writerow(line)


