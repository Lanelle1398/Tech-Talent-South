install.packages("dplyr")


#define the vectors
sex <- c("M", "F","M", "F", "M", "F", "M", "F", "M", "F", "M", "F") # saved vectors/factors as variables and used c() or rep() function to create
stage <- c("I", "II","III", "I", "II","III", "I", "II","III", "I", "II","III")
treatment <- c("A", "A","A", "A", "B","B", "B", "B","P", "P", "P","P")
myc <- c(2343, 457, 4593, 9035, 3450,3524, 958, 1053,8674, 3424, 463,5105)

#replicate the vector four times ; work on this later
# rep(stage, times=4)
# print(stage)

#print row names
meta <- data.frame(sex, stage, treatment, myc)
rownames(meta) <- paste("sample12", 1:12, sep="")
print(meta)



#simpler way to create the data frame
# data <- data.frame(sex1= c("M", "F","M", "F", "M", "F", "M", "F", "M", "F", "M", "F"),
#                    stage1= c("I", "II","III", "I", "II","III", "I", "II","III", "I", "II","III"),
#                    treatment1 = c("A", "A","A", "A", "B","B", "B", "B","P", "P", "P","P"),
#                    myc1= c(2343, 457, 4593, 9035, 3450,3524, 958, 1053,8674, 3424, 463,5105))
# data                                     # Print example data


#return only the treatment and sex columns using []:
# metaCopy<-meta[, c('treatment', 'sex')]
# print(metaCopy)

# return the treatment values for samples 5, 7, 9, and 10 using []:
metaCopy2<-meta[c(5,7,9,10), 3]

# use subset() to return all data for those samples receiving treatment P:
metaCopy5<-subset(meta, treatment == 'P')
print(metaCopy5)

#use filter()/select()to return only the stage and treatment columns for those samples with myc > 5000
#see number2.r

#remove the treatment column from the dataset using []:
meta4 <- meta[, -3 ]
print(meta4)

#remove samples 7, 8 and 9 from the dataset using []:
metaCopy6 <- meta[c(-7,-8,-9), ]
print(metaCopy6)

#keep only samples 1-6 using []:
metaCopy7 <-meta[c(1:6), ]
print(metaCopy7)

#add a column called pre_treatment to the beginning of the dataframe with the values T, F, F, F, T, T, F, T, F, F, T, T (Hint: use cbind())
pre_treatment <- c(T, F, F, F, T, T, F, T, F, F, T, T)
cbind(pre_treatment, meta)

# change the name of the columns to A,B,C,D
colnames(meta) <- c('a','b','c', 'd')
print(meta)


