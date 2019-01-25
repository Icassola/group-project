#Start with reading in the datasets for DBpedia and Kaggle and packages
dbpedia <- read.csv("person_per_line_dbp.csv", stringsAsFactors = F, row.names = NULL)
kaggle <- read.csv("person_per_line_kaggle.csv", stringsAsFactors = F) 
library(maps)
library(tidyverse)
library(dplyr)
library(scales)

#PLEASE IGNORE MEDAL PART, CODE IS NECESSARY TO RUN CERTAIN PARTS LATER ON
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
geom_bar(data=kaggle_filteredbyyear, mapping=aes(x=Medal), fill='skyblue') 
  xlab("Type of medal") + ylab("Count") +
  labs(title = "Number of medals per type", subtitle = "DBPedia n=8928 unique athletes, Kaggle n=10845 unique athletes")
ggplot()+geom_bar(data=updated_medal_filtered_merged, mapping=aes(x=Medal, fill=dataset), position='dodge')
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

#SPORTS, this is the dbpedia dataset
cbPalette <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")

sports <- read.csv('person_per_line_dbp_sports.csv')
sports_filtered <- filter (sports, Sport=='Handball' | Sport=='Volleyball' | Sport=='Field hockey' | Sport=='Ice Hockey' |Sport=='Basketball')  

ggplot() + geom_bar(data=sports_filtered, mapping=aes(x=Sport, fill=Sport)) + 
  scale_fill_manual(values=cbPalette) +
  ggtitle("Frequency of entries in DBpedia per sport")

#now the kaggle dataset
kaggle_filteredbyyearandsport <- filter(kaggle_filteredbyyear, Sport=='Handball' | Sport=='Volleyball' | Sport=='Hockey' | Sport=='Ice Hockey' |Sport=='Basketball')
#because there are some values that are not the same in both data sets (e.g. hockey and field hockey) I wrote to csv and uploaded the cleaned file (changed manually in Python)

ggplot() + geom_bar(data=kaggle_filteredbyyearandsport, mapping=aes(x=Sport, fill=Sport)) +
  scale_fill_manual(values=cbPalette) +
  ggtitle("Frequency of entries in Kaggle per sport")
sports_filtered$dataset <- 'DBPedia'
kaggle_filteredbyyearandsport$dataset <- 'Kaggle'
a <- select(sports_filtered,dataset,Sport)
b <- select(kaggle_filteredbyyearandsport,dataset, Sport)

c <- rbind(a,b)
#again I wrote to csv and changed some entries in Python, then reuploaded the new file
write.csv(c, "sportsbydataset.csv")

#make graphs
d <- read.csv("sportsbydataset_new.csv")
kaggle_sportsfinal <- filter(d, dataset == "Kaggle")
ggplot() + geom_bar(data=kaggle_sportsfinal, mapping=aes(x=Sport, fill=Sport)) +
  scale_fill_manual(values=cbPalette) +
  ggtitle("Frequency of entries in Kaggle per sport")
#now the sports for both datasets in one graph
ggplot() + geom_bar(data=d, mapping=aes(x=dataset, fill=Sport), position='fill') +
  scale_y_continuous(labels=scales::percent) +
  scale_fill_manual(values=cbPalette) +
  ggtitle("Relative count of entries per sport")
ggplot() + geom_bar(data=d, mapping=aes(x=dataset, fill=dataset)) +
  facet_wrap(~Sport) +
  coord_flip()+
  scale_fill_manual(values=cbPalette) +
  ggtitle("Absolute count of entries per sport")

#make a plot with percentages for sports
counts_d <- count(d, Sport, dataset)
pct_bas <- counts_d[1,3]/counts_d[2,3]
pct_fiho <- counts_d[3,3]/counts_d[4,3]
pct_han <- counts_d[5,3]/counts_d[6,3]
pct_ice <- counts_d[7,3]/counts_d[8,3]
pct_vol <- counts_d[9,3]/counts_d[10,3]

percentages_sports<- rbind(pct_bas, pct_fiho, pct_han, pct_ice, pct_vol)
percentages_sports$Sport <- c("Basketball", "Field hockey", "Handball", "Ice hockey", "Volleyball")
percentages_sports$percentage <- percent(round(percentages_sports$n, digits = 3))

ggplot(data=percentages_sports, mapping=aes(x=reorder(Sport,n), y=n))+geom_bar(fill='lightblue', stat='identity') +
   xlab('Sport') +ylab ("Percentage") +
  scale_y_continuous(labels= percent) +
  ggtitle("Percentage of athletes in Kaggle dataset that has an entry in DBPedia") +
  geom_text(data= percentages_sports, mapping=aes(label=percentage))

#make a table
attach(d)
  
mytable <- table(Sport, dataset)

d_numbers <- d %>%
  group_by(Sport, dataset) %>%
  summarize(
    entries = n()
  ) %>%
  spread(dataset, entries)

d_numbers_total <- d_numbers %>%
  ungroup() %>%
  summarize(
    DBPedia = sum(DBPedia),
    Kaggle = sum(Kaggle)
  ) %>%
  mutate(
    Sport = "Total"
  )

d_totals <- bind_rows(d_numbers, d_numbers_total) %>%
  mutate(
    Total_Sport = sum(DBPedia, Kaggle)
  )
install.packages('xtable')
library(xtable)
xtable(d_totals)
