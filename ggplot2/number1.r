library(ggplot2)
econData2 <- read.csv("/Users/lanellephillips/Downloads/EconomistData.csv")
head(econData2)

##part 1 #########################################
#Create a scatter plot with CPI on the x axis and HDI on the y axis.
ggplot(econData2, aes(x=CPI, y=HDI)) +geom_point()
#Color the points blue.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(color="blue")
#Map the color of the the points to Region.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color=Region))
#Make the points bigger by setting size to 2
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color=Region), size=2)
#Map the size of the points to HDI.Rank
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color=Region, size=HDI.Rank))


#part 2###############################################
# Re-create a scatter plot with CPI on the x axis and HDI on the y axis (as you did in the previous exercise).
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point()
# Overlay a smoothing line on top of the scatter plot using geom_smooth.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point()+geom_smooth()
# Overlay a smoothing line on top of the scatter plot using geom_smooth, but use a linear model for the predictions. Hint: see ?stat_smooth.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point()+geom_smooth(method = "lm", se = FALSE)
# Overlay a smoothing line on top of the scatter plot using geom_line. Hint: change the statistical transformation.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point()+geom_line(stat="smooth")
# BONUS: Overlay a smoothing line on top of the scatter plot using the default loess method, but make it less smooth. Hint: see ?loess.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point()+ geom_smooth(span=0.1)

#part 3 ##############################################
#Create a scatter plot with CPI on the x axis and HDI on the y axis. Color the points to indicate region.
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color=Region))
#Modify the x, y, and color scales so that they have more easily-understood names (e.g., spell out “Human development Index” instead of “HDI”).
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color=Region))+ labs(y = "Corruption Perception  Index", x = "Human Development Index")+ scale_color_discrete(name = "World Regions")
#Modify the color scale to use specific values of your choosing. Hint: see ?scale_color_manual
ggplot(econData2, aes(x=CPI, y=HDI)) + geom_point(aes(color = Region)) + scale_colour_manual(values = c("red", "blue", "green", "yellow", "black", "pink"))
                                                  
