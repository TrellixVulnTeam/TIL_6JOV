# 1. 데이터 확인

train <- read.csv('train.csv',na.strings = '')
test <- read.csv('test.csv',na.strings = '')

train
summary(train)
str(train)

##결측값 확인
install.packages("Rcpp")
library(Amelia)
missmap(train,col = c('red','grey'))  #Cabin, Age,Embarked 에 결측값 존재
missmap(test,col = c('red','grey'))   #Cabin,Age, Fare 에 결측값 존재


# 2. Feature Engineering


## 2-1 Sex 남:0 여:1
#성별 남 -> 0 ,여 -> 1
train$Sex<- ifelse(train$Sex=='male',0,1)
train


## 2-2 name2 컬럼 생성

name2 <-unlist(strsplit(train$Name,split=' '))
name2<-grep('^[A-Z][a-z]+[.]',name2,value=TRUE)
table(name2)

miss <-c("Mlle.", "Ms.", "Lady.", "Dona.",'Miss.')
mrs <-c('Mme.','Mrs.')
officer<-c("Capt.", "Col.", "Major.", "Dr.", "Rev.", "Don.",  "Sir.", "the Countess.", "Jonkheer.")
mr<-c('Mr.')
train$name2<-0
train[name2 %in% miss,]$name2 <-1
train[name2 %in% mrs,]$name2 <-2
train[name2 %in% officer,]$name2 <-3
train[name2 %in% mr,]$name2 <-4




str(train)


## 2-3 Pclass 1>2>3

train$Pclass <- factor(train$Pclass,order=TRUE,levels=c(3,2,1))



## 2-4 Embarked 결측값 채우기
sum(is.na(train$Embarked)) # 2
y<-table(train$Embarked)

train[is.na(train$Embarked),]$Embarked <-names(y)[which(y==max(y))]

train$Embarked[train$Embarked=='S']<-1
train$Embarked[train$Embarked=='C']<-2
train$Embarked[train$Embarked=='Q']<-3


## 2-5 FamilySize

train$FamilySize <-train$SibSp+train$Parch

## 2-6 유클리디안 거리 이용해서 Age 결측값 채우기
scaled <- data.frame(sapply(train[,c('Pclass', 'SibSp', 'Parch', 'Fare','name2','Embarked','FamilySize','Sex')], as.numeric))
scaled <-apply(scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
scaled
age.naidx <-which(is.na(train$Age))
age.naidx
#cor(a,b) ->a와 b의 상관관계
cor(scaled[-age.naidx,],train[-age.naidx,]$Age)




# Pclass      0.36922602
# SibSp      -0.30824676
# Parch      -0.18911926
# Fare        0.09606669
# name2       0.36994581
# Embarked    0.01017065
# FamilySize -0.30191396
# Sex        -0.09325358

# Pclass, SibSp,name2,familysize와 유클리디안 거리 가까운 데이터 10개 선택

for (i in age.naidx){
  eu.dis<-sqrt(colSums((t(scaled[,c('Pclass','SibSp','name2','FamilySize')])-scaled[i,c('Pclass','SibSp','name2','FamilySize')])^2))
  top10.idx<-order(eu.dis)[1:10]
  train$Age[i]<-mean(train[top10.idx,'Age'],na.rm=T)
}



# 3. Survived 예측(유클리디안 거리 이용)



train.scaled <- data.frame(sapply(train[,c('Pclass', 'SibSp', 'Parch', 'Fare','name2','Embarked','FamilySize','Age','Sex')], as.numeric))
train.scaled <-apply(train.scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
train.scaled

cor(train.scaled,train$Survived)

# Pclass      0.33848104
# SibSp      -0.03532250
# Parch       0.08162941
# Fare        0.25730652
# name2      -0.51646413
# Embarked    0.10681139
# FamilySize  0.01663899
# Age        -0.04485145
# Sex         0.54335138


train$Predictions <-NA

for (i in seq(nrow(train))){
  eu.dis<-sqrt(colSums((t(scaled[,c('Sex','name2','Pclass','Fare')])-scaled.all[i,c('Sex','name2','Pclass','Fare')])^2))
  top10.idx<-order(eu.dis)[1:10]
  pred<-mean(train[top10.idx,'Survived'])
  train$Predictions[i]<-round(pred)
  print(train$Predictions[i])
}

train



#4. train 정확도 확인
sum(train$Survived==train$Predictions) #757
sum(train$Survived==train$Predictions)/nrow(titanic) # 0.8496072






#5. test set에 적용


#성별
test$Sex<- ifelse(test$Sex=='male',0,1)


#name2
name2 <-unlist(strsplit(test$Name,split=' '))
name2<-grep('^[A-Z][a-z]+[.]',name2,value=TRUE)
table(name2)

miss <-c("Mlle.", "Ms.", "Lady.", "Dona.",'Miss.')
mrs <-c('Mme.','Mrs.')
officer<-c("Capt.", "Col.", "Major.", "Dr.", "Rev.", "Don.",  "Sir.", "the Countess.", "Jonkheer.")
mr<-c('Mr.')
test$name2<-0
test[name2 %in% miss,]$name2 <-1
test[name2 %in% mrs,]$name2 <-2
test[name2 %in% officer,]$name2 <-3
test[name2 %in% mr,]$name2 <-4


str(test)




#Pclass 
test$Pclass <- factor(test$Pclass,order=TRUE,levels=c(3,2,1))



#Embarked

test$Embarked[test$Embarked=='S']<-1
test$Embarked[test$Embarked=='C']<-2
test$Embarked[test$Embarked=='Q']<-3


#FamilySize
test$FamilySize<-test$SibSp+test$Parch

#Fare 결측값 채우기
sum(is.na(test$Fare)) #1
test$Pclass<-sapply(test[,'Pclass'], as.numeric)

###Fare, Pclass상관관계가 높고, Fare 범위가 넓기때문에 Pclass==1의 중앙값으로 대체
cor(test[!(is.na(test$Fare)),'Pclass'],test[!(is.na(test$Fare)),]$Fare) #0.5771473

which(is.na(test$Fare))# 153
test[153,'Pclass'] #1

median(test[test$Pclass==1,]$Fare,na.rm = T)
test[153,'Fare']<-7.8958




#Age
scaled.testAge <- data.frame(sapply(test[,c('Pclass', 'SibSp', 'Parch', 'Fare','name2','Embarked','Sex','FamilySize')], as.numeric))
scaled.testAge <-apply(scaled.testAge,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
nrow(scaled.testAge)
age.naidx <-which(is.na(test$Age))
age.naidx
round(cor(scaled.testAge[-age.naidx,],test[-age.naidx,]$Age),2)

# Pclass      0.49
# SibSp      -0.09
# Parch      -0.06
# Fare        0.33
# name2       0.31
# Embarked    0.11
# Sex         0.00
# FamilySize -0.09

for (i in age.naidx){
  eu.dis<-sqrt(colSums((t(scaled.testAge[,c('Pclass','SibSp','name2','FamilySize')])-scaled.test[i,c('Pclass','SibSp','name2','FamilySize')])^2))
  top10.idx<-order(eu.dis)[1:10]
  test$Age[i]<-mean(test[top10.idx,'Age'],na.rm=T)
}





# 5. test$Survived 



test.scaled <- data.frame(sapply(test[,c('Pclass', 'SibSp', 'Parch', 'Fare','name2','Embarked','FamilySize','Age','Sex')], as.numeric))
test.scaled <-apply(test.scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
test.scaled



test$Survived <-NA
for (i in seq(nrow(test))){
  eu.dis<-sqrt(colSums((t(train.scaled[,c('Sex','name2','Pclass','Fare')])-test.scaled[i,c('Sex','name2','Pclass','Fare')])^2))
  top10.idx<-order(eu.dis)[1:10]
  pred<-mean(train[top10.idx,'Survived'])
  test$Survived[i]<-round(pred)
  print(test$Survived[i])
}

test





submissions2<-test[,c("PassengerId","Survived")]
submissions2
write.csv(submissions,file='submissions2.csv',row.names = F)








