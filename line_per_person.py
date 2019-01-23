import csv
newname = []
with open ('cleaned_nationality.csv') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    with open ('person_per_line_dbp.csv', 'w', newline = '') as newfile: 
        writer = csv.DictWriter(newfile, fieldnames = headers)
        for line in reader:
            name = line['name']
            if name not in newname:
                newname.append(name)
                writer.writerow(line)