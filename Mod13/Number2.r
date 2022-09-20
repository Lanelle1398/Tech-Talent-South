
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
meta1 <- data.frame(sex, stage, treatment, myc)
rownames(meta1) <- paste("sample12", 1:12, sep="")
print(meta1)
# 
filter(meta1, myc > 5000) %>% select(stage, treatment)


