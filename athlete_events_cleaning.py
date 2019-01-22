import csv
'''
athletes_medal = []
with open('athlete_events.csv', 'r') as athletes:
    with open('athletes_medals.csv', 'w') as file:
        for line in athletes:
            if line[-3:-1] != 'NA':
                file.write(line)
'''


with open('athletes_medals.csv', 'r') as athletes:
    reader = csv.DictReader(athletes)
    headers = reader.fieldnames
    headers.append('BirthYear')
    #print(f'headers is of type: {type(headers)}')

    with open('athletes_year.csv', 'w', newline ='') as athletesyears:
        writer = csv.DictWriter(athletesyears, fieldnames=headers)
        writer.writeheader()
        for line in reader: 
            if line['Age'] != 'NA':
                year = int(line['Year'])
                age = int(line['Age'])
                birthyear = year - age
                line['BirthYear'] = birthyear
                writer.writerow(line)


