dbpedia <- read.csv("data_cleaned.csv", stringsAsFactors = F, row.names = NULL)
library(maps)
library(tidyverse)
library(dplyr)
#plot for wiki dataset
ggplot()+geom_bar(data = dbpedia, mapping=aes(x=Medal))
counts_wiki <- count(dbpedia, Name)

#plot for online dataset medals
kaggle <- read.csv("athletes_year.csv", stringsAsFactors = F) 
kaggle_filteredbyyear <- filter(kaggle,  BirthYear >= 1950 & BirthYear<=1980 )
ggplot()+geom_bar(data=kaggle, mapping=aes(x=Medal))                  
counts_kaggle <- count(kaggle_filteredbyyear, Name)
#add labels to dataset to make a distinction between datasets, then merge the two
dbpedia$dataset <- 'DBPedia'
kaggle_filteredbyyear$dataset <- 'Kaggle'
dbpedia_filtered <- select(dbpedia,dataset,Medal)
medal_kaggle_filtered <- select(kaggle_filteredbyyear,dataset, Medal)

medal_filtered_merged <- rbind(medal_filtered, medal_kaggle_filtered)
# change some entries in Python, first write to csv and then reupload new file
write.csv(medal_filtered_merged, "medalfiltered.csv")
updated_medal_filtered_merged <- read.csv("medalfiltered.csv")
#make a plot that has both datasets
ggplot()+geom_bar(data = medal, mapping=aes(x=Medal), fill='darkblue') +
geom_bar(data=new_filteredbyyear, mapping=aes(x=Medal), fill='skyblue') +
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
new_filteredbyyearandsport <- filter(new_filteredbyyear, Sport=='Handball' | Sport=='Volleyball' | Sport=='Hockey' | Sport=='Ice Hockey' |Sport=='Basketball')
ggplot() + geom_bar(data=new_filteredbyyearandsport, mapping=aes(x=Sport))
sports_filtered$dataset <- 'DBPedia'
new_filteredbyyearandsport$dataset <- 'Kaggle'
a <- select(sports_filtered,dataset,Sport)
b <- select(new_filteredbyyearandsport,dataset, Sport)

c <- rbind(a,b)
write.csv(c, "sportsbydataset.csv")
d <- read.csv("sportsbydataset.csv")
#now together
ggplot() + geom_bar(data=d, mapping=aes(x=dataset, fill=Sport), position='fill') +
  scale_y_continuous(labels=scales::percent)
