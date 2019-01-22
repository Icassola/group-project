import csv

athletes_medal = []
with open('athlete_events.csv', 'r') as athletes:
    with open('athletes_medals.csv', 'w') as file:
        for line in athletes:
            if line[-3:-1] != 'NA':
                file.write(line)


