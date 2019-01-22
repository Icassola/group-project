import csv
with open ('data_cleaned.csv', 'r', encoding="utf8") as file:
    reader = csv.DictReader(file)
    
    with open('datacleaned_sports.csv', 'w', encoding='utf8', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['Year', 'Name', 'Birthplace', 'Nationality', 'Sport','Labels', 'Medal'])
        
        for entry in reader:
            if "field hockey" in entry['Sport'].lower():
                entry['Sport'] = 'Field hockey'
            
            if "ice hockey" in entry['Sport'].lower():
                entry['Sport'] = 'Ice hockey'
            
            if "volleyball" in entry['Sport'].lower():
                entry['Sport'] = 'Volleyball'
            
            if "basketball" in entry['Sport'].lower():
                entry['Sport'] = 'Basketball'
            
            if "handball" in entry['Sport'].lower():
                entry['Sport'] = 'Handball'
            writer.writerow(entry.values())
