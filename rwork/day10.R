train<-read.csv('train.csv',na.strings = '')
test<-read.csv('test.csv',na.strings = '')

train$Prediction<-ifelse(train$Sex=='male',0,1)
head(train)

#train 정확도

sum(train$Survived==train$Prediction)
sum(ifelse(train$mysurvived == train$Survived, 1, 0)) / nrow(train)  # 0.7867565

#test 적용
test$Survived<-ifelse(test$Sex=='male',0,1)
head(test)
submissions<-test[,c('PassengerId',"Survived")]
submissions


write.csv(submissions,file='submissions.csv',row.names = F)


#2

mpc<-mean(titanic$Pclass)
mna<-mean(titanic$Name)

head(titanic)
