install.packages("dplyr")
library(dplyr)
install.packages("AER")
library(AER)
install.packages("readr")
library(readr)
install.packages("tidyverse")
library(tidyverse)

#List all example files available with the readr library.
list.files()

#Read the mtcars.csv file.
download.file("https://raw.githubusercontent.com/Lanelle1398/Tech-Talent-South/main/Importing%20and%20transforming%20data/mtcars.csv","mtcars.csv")
df<-read.csv("mtcars.csv")
head(df,10)

###Instructor said to skip these below ############

# Exercise 4
# Read the example.log file.
# 
# Exercise 5
# List all sheets in readxl_example("datasets.xlsx").
# 
# Exercise 6
# Read data from the last sheet.

###################################################

# Exercise 7
# Load the dplyr package. Install and load the AER package and run the command data("Fertility") which loads the dataset Fertility to your workspace. Take a glimpse() at the data.
install.packages("dplyr")
library(dplyr)

data("Fertility")
head(Fertility)

# Exercise 8 Select rows 35 to 50 and print to console its age and work entry
Fertility[35:50, c(4,8)]

#Exercise 9 Select the last row in the dataset and print to console.
tail(Fertility, n = 1)

# Exercise 10: Count how many women proceeded to have a third child.
Fertility %>% group_by(morekids) %>% tally()
# Exercise 11: There are four possible gender combinations for the first two children. Which is the most common?
Fertility %>% group_by(gender1,gender2) %>% tally()
