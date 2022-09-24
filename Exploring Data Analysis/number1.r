library(tidyverse)
library(modelr)

# Exercise 1 Familiarize yourself with the heights data set provided with the modelr package.
summary(heights)
head(heights,10)

#Exercise 2#########################################
# Create a list of formulas for modeling income with:
# *height
# *height * weight
# *linear combination of all variables

list_of_formulas <- formulas(~income,
                  height_formula = ~height,
                  HeightWeight = ~height*weight,
                  everything_in_datset= ~.)
list_of_formulas

# Exercise 3##########################################
# From the data, remove rows containing NA’s. Fit the linear model with the formulas from exercise 2.

heights_removed <- na.omit(heights) 

#wrong
# linear_model <- lm(list_of_formulas, data=heights_removed)
#fit_with(lm,list_of_formulas )

fit_linear_model <- heights_removed %>% fit_with(lm, list_of_formulas)

# Exercise 4 For each fit, calculate RMSE. ###########
fit_linear_model %>% map(rmse, data = heights_removed)

#Exercise 5 For each model, add residuals to the data and plot their distribution. (Hint: use lift_dl().)

fit_linear_model%>% lift_dl()
heights_removed %>%
lift_dl(gather_residuals)(data = ., fit_linear_model) %>% ggplot(aes(resid, color = model)) +  geom_density(size = 1)


