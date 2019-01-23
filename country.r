kaggle <-read.csv("person_per_line_kaggle.csv")
library(tidyverse)
library(scales)
#select countries
kaggle_year<- filter(kaggle, BirthYear >= 1950 & BirthYear <= 1980)
kaggle_countryyear <- filter(kaggle_year, Team == "United States" |Team == "China" |Team == "Canada" | Team == "Australia" | Team == "Japan" | Team=='South-Korea')

#bar plot for medals per country
ggplot()+geom_bar(data=kaggle_countryyear, mapping=aes(x=BirthYear, fill=Team))

#DBPedia dataset
dbpedia <- read.csv('person_per_line_dbp.csv')
dbpedia_country <- filter(dbpedia, nationality== "United States" | nationality== "China" | nationality == "Canada" | nationality == "Australia" | nationality == "Japan" | nationality=='South-Korea')

#plot medals per country
ggplot()+geom_bar(data=dbpedia_country, mapping=aes(x=nationality))

#put the two datasets together and make one graph
dbpedia_country$dataset <- 'DBPedia'
kaggle_countryyear$dataset <- 'Kaggle'
names(kaggle_countryyear)[7]<-"nationality"
kaggle_select <- select(kaggle_countryyear, Name, nationality, Sport, dataset)
names(kaggle_select)[1] <- 'name'
names(kaggle_select)[3] <- 'sport'
merged_data <- rbind(dbpedia_country, kaggle_select)

ggplot()+geom_bar(data=merged_data, mapping=aes(x=dataset, fill=nationality), position='fill')

#to put things into perspective, i want to get the percentage of people for the different countries that has a wiki page
counts_merged_data <- count(merged_data, nationality, dataset)
pct_aus <- counts_merged_data[1,3]/counts_merged_data[2,3]
pct_can <- counts_merged_data[3,3]/counts_merged_data[4,3]
pct_chi <- counts_merged_data[5,3]/counts_merged_data[6,3]
pct_jap <- counts_merged_data[7,3]/counts_merged_data[8,3]
pct_usa <- counts_merged_data[9,3]/counts_merged_data[10,3]

percentages <- rbind(pct_aus, pct_can, pct_chi, pct_jap, pct_usa)
percentages$Country <- c("Australia", "Canada", "China", "Japan", "United States")
percentages$percent <- percent(round(percentages$n, digits = 3))
ggplot(data=percentages, mapping=aes(x=reorder(Country,n), y=n))+geom_bar(fill='pink', stat='identity') +
scale_y_continuous(labels= percent) + xlab('Country') +ylab ("Percentage") +
  geom_text(data= percentages, mapping=aes(label=percent)) +
  ggtitle("Percentage of athletes in Kaggle dataset that has an entry in DBPedia")
