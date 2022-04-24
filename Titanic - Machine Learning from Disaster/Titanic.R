dataset = read.csv("train.csv")
View(dataset)
dataset = dataset[, c(2,3,5,6,7,8,10,12)]

# replacing na with mean value
dataset$Age = ifelse(is.na(dataset$Age), mean(dataset$Age, na.rm = TRUE), dataset$Age)
# Label encoding
dataset$Sex = factor(dataset$Sex, levels = c("female", "male"), 
               labels = c(0,1))
dataset$Embarked = factor(dataset$Embarked, levels = c("C", "Q", "S"), 
                    labels = c(0,1,2))
#Normalisation
dataset$Fare = scale(dataset$Fare)

#Logistic regression model training
classifier = glm(formula = Survived~., family = binomial, data = dataset)
summary(classifier)


# Model fitting
test = read.csv("test.csv")
copy = test
test = test[, c(1,2,4,5,6,7,9,11)]
test$Age = ifelse(is.na(test$Age), mean(test$Age, na.rm = TRUE),test$Age)
test$Sex = factor(test$Sex, levels = c("female", "male"), 
                     labels = c(0,1))
test$Embarked = factor(test$Embarked, levels = c("C", "Q", "S"), 
                          labels = c(0,1,2))
test$Fare = scale(test$Fare)



pred = predict(classifier, type = 'response', newdata = test)
y_pred = ifelse(pred > 0.5, 1,0)
result = data.frame(copy$PassengerId, y_pred)


