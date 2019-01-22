medal <- read.csv("data_cleaned.csv", stringsAsFactors = F, row.names = NULL)
library(maps)
library(tidyverse)

#plot for wiki dataset
ggplot()+geom_bar(data = medal, mapping=aes(x=Medal))
counts_wiki <- count(medal, Name)

#plot for online dataset medals
online_dataset <- read.csv("athletes_year.csv", stringsAsFactors = F) 
new <- na.omit(online_dataset)
new_filteredbyyear <- filter(new,  BirthYear >= 1950 & BirthYear<=1980 )
ggplot()+geom_bar(data=new, mapping=aes(x=Medal))                  
counts_kaggle <- count(new_filteredbyyear, Name)

#include the two
ggplot()+geom_bar(data = medal, mapping=aes(x=Medal), fill='darkblue') +
geom_bar(data=new_filteredbyyear, mapping=aes(x=Medal), fill='skyblue') +
  xlab("Type of medal") + ylab("Count") +
  labs(title = "Number of medals per type", subtitle = "DBPedia n=8928 unique athletes, Kaggle n=10845 unique athletes")

#sports time, this is the dbpedia dataset
sports <- read.csv('datacleaned_sports.csv')
sports_filtered <- filter (sports, Sport=='Handball' | Sport=='Volleyball' | Sport=='Field hockey' | Sport=='Ice hockey' |Sport=='Basketball')  
ggplot() + geom_bar(data=sports_filtered, mapping=aes(x=Sport))

#now the kaggle dataset
new_filteredbyyearandsport <- filter(new_filteredbyyear, Sport=='Handball' | Sport=='Volleyball' | Sport=='Hockey' | Sport=='Ice Hockey' |Sport=='Basketball')
ggplot() + geom_bar(data=new_filteredbyyearandsport, mapping=aes(x=Sport))

#now together
