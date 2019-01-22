import csv
with open ('demonym.csv', encoding='utf-8') as file: 
 my_dict = {} # initialize dictionary
 
 headers = file.readline()

 for line in file: # for 2nd line onward
    (Nationality, Country) = (line.strip().split(','))

    my_dict = {
        Nationality : Country
    }
    print(my_dict)