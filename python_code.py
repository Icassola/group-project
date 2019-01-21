import csv

final_list = []
for line in medalists:
    person = []
    person.append(line[''])
    birth_date = line['']
    person.append(birth_date)
    sport = line['']
    person.append(sport)
    final_list.append(person)

#Save the final_list to a CSV file for use in R
with open('gymnasts.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    
    writer.writerow(['birth_date', 'birth_place'])

    for gymnast in final_list:
        writer.writerow(gymnast)