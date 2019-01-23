#Start with reading in the datasets for DBpedia and Kaggle and packages
dbpedia <- read.csv("data_cleaned.csv", stringsAsFactors = F, row.names = NULL)
kaggle <- read.csv("athletes_year.csv", stringsAsFactors = F) 
library(maps)
library(tidyverse)
library(dplyr)

#exploratory plot for wiki dataset
ggplot()+geom_bar(data = dbpedia, mapping=aes(x=Medal))
counts_wiki <- count(dbpedia, Name)

#exploratory plot for Kaggle dataset medals
kaggle_filteredbyyear <- filter(kaggle,  BirthYear >= 1950 & BirthYear<=1980 )
ggplot()+geom_bar(data=kaggle, mapping=aes(x=Medal))                  
counts_kaggle <- count(kaggle_filteredbyyear, Name)

#add labels to dataset to make a distinction between datasets, then merge the two
dbpedia$dataset <- 'DBPedia'
kaggle_filteredbyyear$dataset <- 'Kaggle'
dbpedia_filtered <- select(dbpedia,dataset,Medal)
medal_kaggle_filtered <- select(kaggle_filteredbyyear,dataset, Medal)

medal_filtered_merged <- rbind(dbpedia_filtered, medal_kaggle_filtered)

#I changed some entries in Python, so i wrote to csv and then reuploaded a new file
#write.csv(medal_filtered_merged, "medalfiltered.csv")
updated_medal_filtered_merged <- read.csv("medalfiltered.csv")
#make a plot that has both datasets
ggplot()+geom_bar(data = dbpedia, mapping=aes(x=Medal), fill='darkblue') +
geom_bar(data=kaggle_filteredbyyear, mapping=aes(x=Medal), fill='skyblue') +
  xlab("Type of medal") + ylab("Count") +
  labs(title = "Number of medals per type", subtitle = "DBPedia n=8928 unique athletes, Kaggle n=10845 unique athletes")

ggplot()+geom_bar(data=updated_medal_filtered_merged, mapping=aes(x=dataset, fill=Medal), position='fill') + 
  scale_y_continuous(labels=scales::percent)

#is there a difference in the average count of medals per athlete?
average_medal_kaggle <- sum(counts_kaggle$n)/10845
average_medal_dbpedia <- sum(counts_wiki$n)/8928

#boxplot medals per athlete
counts_kaggle$dataset <- "Kaggle"
counts_wiki$dataset <- "DBpedia"
merged_counts <- rbind(counts_kaggle, counts_wiki)
ggplot(data=merged_counts, aes(x=dataset, y=n)) + 
  geom_boxplot() + 
  scale_y_continuous(name="Medals per athlete", limits=c(1, 15))

#sports time, this is the dbpedia dataset
sports <- read.csv('datacleaned_sports.csv')
sports_filtered <- filter (sports, Sport=='Handball' | Sport=='Volleyball' | Sport=='Field hockey' | Sport=='Ice hockey' |Sport=='Basketball')  

ggplot() + geom_bar(data=sports_filtered, mapping=aes(x=Sport, fill=Sport))

#now the kaggle dataset
kaggle_filteredbyyearandsport <- filter(kaggle_filteredbyyear, Sport=='Handball' | Sport=='Volleyball' | Sport=='Hockey' | Sport=='Ice Hockey' |Sport=='Basketball')
ggplot() + geom_bar(data=kaggle_filteredbyyearandsport, mapping=aes(x=Sport))
sports_filtered$dataset <- 'DBPedia'
kaggle_filteredbyyearandsport$dataset <- 'Kaggle'
a <- select(sports_filtered,dataset,Sport)
b <- select(kaggle_filteredbyyearandsport,dataset, Sport)

c <- rbind(a,b)
#again I wrote to csv and changed some entries in Python, then reuploaded the new file
#write.csv(c, "sportsbydataset.csv")

d <- read.csv("sportsbydataset.csv")
#now the sports for both datasets in one graph
ggplot() + geom_bar(data=d, mapping=aes(x=dataset, fill=Sport), position='fill') +
  scale_y_continuous(labels=scales::percent)
