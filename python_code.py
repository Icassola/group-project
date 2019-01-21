import json
import csv

final_list = []
for line in gymnasts:
    y = []
    y.append(line['year'])
    x = 
    y.append(x)
    final_list.append(y)

#Save the final_list to a CSV file for use in R
with open('gymnasts.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    
    writer.writerow(['birth_date', 'birth_place'])

    for gymnast in final_list:
        writer.writerow(gymnast)