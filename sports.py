import csv
with open ('person_per_line_dbp.csv', 'r', encoding="utf8") as file:
    reader = csv.DictReader(file)
    
    with open('person_per_line_dbp_sports.csv', 'w', encoding='utf8', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['Name', 'Nationality', 'Sport'])
        
        for entry in reader:
            if "field hockey" in entry['sport'].lower():
                entry['sport'] = 'Field hockey'
            
            if "ice hockey" in entry['sport'].lower():
                entry['sport'] = 'Ice Hockey'
            
            if "volleyball" in entry['sport'].lower():
                entry['sport'] = 'Volleyball'
            
            if "basketball" in entry['sport'].lower():
                entry['sport'] = 'Basketball'
            
            if "handball" in entry['sport'].lower():
                entry['sport'] = 'Handball'
            writer.writerow(entry.values())
