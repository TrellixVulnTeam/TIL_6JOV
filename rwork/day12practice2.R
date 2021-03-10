# 1. iris 데이터에 대해 knn 적용하여 분류 모델 작성
# -set.seed(1234)로 통일할 것
data(iris)
set.seed(1234)
# -iris 데이터를 7:3의 비율로 나눈다(sample함수 적용)
index<-sample(1:nrow(iris),nrow(iris)*0.7) # 행번호 1:150 중 5개
train.iris<-iris[index,]
test.iris<-iris[-index,]


str(train.iris)
str(test.iris)


# -트레인 데이터로 knn 모델 생성


iris_train_labels<-train.iris[,5]
iris_test_labels<-test.iris[,5]


library(class)

normalize<-function(x){
  return ( (x-min(x) )/( max(x)-min(x) ) )
  
}

iris_train<-as.data.frame(lapply(train.iris[,c(1:4)],normalize))
iris_test<-as.data.frame(lapply(test.iris[,c(1:4)],normalize))

accuracy<-c()
for (i in seq(from=1,to=25,by=2)){
  
  iris_test_pred<-knn(train=iris_train,test=iris_test,
                      cl=iris_train_labels,k=i)
  accuracy<-c(accuracy,sum(iris_test_pred==iris_test_labels))
}
print(which.max(accuracy)*2-1)  #k=9 또는 21일때 최대


iris_test_pred<-knn(train=iris_train,test=iris_test,
                    cl=iris_train_labels,k=21)


# -테스트 데이터로 테스트(타깃 컬럼 : species)
iris_test_pred #예측

iris_test_labels #정답

sum(iris_test_pred==iris_test_labels)/nrow(iris_test) #0.9333333
# 2. 타이타닉 문제에 다양한 조건식 적용(오전)
# #연습문제 마지막 문제
# #생존 조건식 : 성별, 나이(구간별), 승선항구, 운임

# #생존여부판단 조건식: w1*성별+w2*운임+w3*나이+w4*항구=결과값 >임계치=>생존, 아니면 사망

train <- read.csv('train.csv',na.strings = '')
test <- read.csv('test.csv',na.strings = '')

train$Sex
#Sex
train$Sex<- ifelse(train$Sex=='male',0,1)
train

#Embarked
sum(is.na(train$Embarked)) # 2 결측값
y<-table(train$Embarked)
train[is.na(train$Embarked),]$Embarked <-names(y)[which(y==max(y))]

train$Embarked[train$Embarked=='S']<-1
train$Embarked[train$Embarked=='C']<-2
train$Embarked[train$Embarked=='Q']<-3

head(train)
#Age
scaled <- data.frame(sapply(train[,c('Pclass', 'SibSp', 'Parch', 'Fare','Embarked','Sex')], as.numeric))
scaled <-apply(scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})

age.naidx <-which(is.na(train$Age))
age.naidx
#cor함수: 상관계수 ->두 변수 사이에 상관성을 수치로, 하나의 변수의 값의 변화에 따라 다른 변수가 어떻게 변하는지 (+1~-1)
#절대값이 0.7정도 이상이면 강한 상관관계,
#Age열과 가장 상관관계가 높은 것 
cor(scaled[-age.naidx,],train[-age.naidx,]$Age)


# Pclass   -0.36922602
# SibSp    -0.30824676
# Parch    -0.18911926
# Fare      0.09606669
# Embarked  0.01017065
# Sex      -0.09325358


head(scaled[,c('Pclass','SibSp','Parch')]-scaled[i,c('Pclass','SibSp','Parch')])
head(t(scaled[,c('Pclass','SibSp','Parch')])-scaled[i,c('Pclass','SibSp','Parch')])
#Age결측값 대체
for (i in age.naidx){
  eu.dis<-sqrt(colSums((t(scaled[,c('Pclass','SibSp','Parch')])-scaled[i,c('Pclass','SibSp','Parch')])^2))
  top10.idx<-order(eu.dis)[1:10]
  train$Age[i]<-mean(train[top10.idx,'Age'],na.rm=T)
}


sum(is.na(train$Age))




#모델링

scaled <- data.frame(sapply(train[,c('Age', 'Fare','Embarked','Sex')], as.numeric))
scaled <-apply(scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
scaled<-as.data.frame(scaled)

#abcd 가중치
model1 <-function(a,b,c,d){
  scaled <-scaled %>% 
    mutate(Predictions =Sex*a+Fare*b+Age*c+Embarked*d)
  return(scaled)
  
}


#이 값을 얼마로 설정하느냐(임계치 값을 얼마로 설정할건지)
#sigmoid함수
scaled<-model1(0.5,0.3,0.1,0.1)
train_pred <-round(scaled$Predictions)
train_pred

sum(train$Survived==train_pred)
sum(train$Survived==train_pred)/nrow(train)  #0.7867565



#test set에 적용


#Sex
test$Sex<- ifelse(test$Sex=='male',0,1)
test

#Embarked
sum(is.na(test$Embarked)) # 2

test$Embarked[test$Embarked=='S']<-1
test$Embarked[test$Embarked=='C']<-2
test$Embarked[test$Embarked=='Q']<-3


#Fare 결측값 채우기
sum(is.na(test$Fare)) #1
test$Pclass<-sapply(test[,'Pclass'], as.numeric)

###Fare, Pclass상관관계가 높고, Fare 범위가 넓기때문에 Pclass==1의 중앙값으로 대체
cor(test[!(is.na(test$Fare)),'Pclass'],test[!(is.na(test$Fare)),]$Fare) #-0.5771473
#or
cor(test[!(is.na(test$Fare)),'Pclass'],test[!(is.na(test$Fare)),'Fare']) #-0.5771473




which(is.na(test$Fare))# 153
test[153,'Pclass'] #3

median(test[test$Pclass==3,]$Fare,na.rm = T)
test[153,'Fare']<-7.8958



#Age (유클리디안 거리로 결측값 채우기)
scaled <- data.frame(sapply(test[,c('Pclass', 'SibSp', 'Parch', 'Fare','Embarked','Sex')], as.numeric))
scaled <-apply(scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
scaled
age.naidx <-which(is.na(test$Age))

for (i in age.naidx){
  eu.dis<-sqrt(colSums((t(scaled[,c('Pclass','SibSp','Parch')])-scaled[i,c('Pclass','SibSp','Parch')])^2))
  top10.idx<-order(eu.dis)[1:10]
  test$Age[i]<-mean(test[top10.idx,'Age'],na.rm=T)
}

#모델링
scaled <- data.frame(sapply(test[,c('Age', 'Fare','Embarked','Sex')], as.numeric))
scaled <-apply(scaled,2,function(x){(x-min(x,na.rm=T))/(max(x,na.rm=T)-min(x,na.rm=T))})
scaled<-as.data.frame(scaled)



model1 <-function(a,b,c,d){
  scaled <-scaled %>% 
    mutate(Predictions =Sex*a+Fare*b+Age*c+Embarked*d)
  return(scaled)
  
}

scaled<-model1(0.5,0.3,0.1,0.1)
test_pred <-round(scaled$Predictions)

test_pred

submission <- as.data.frame(cbind(test$PassengerId,test_pred))
submission
colnames(submission)[1] <- 'PassengerId'
colnames(submission)[2] <- 'Survived'

write.csv(submission,file='submission_model1.csv',row.names = F)








#3. Decision Tree
# # 만약에 성별이 남자이면{
# #   만약에 나이가 20세 미만이면{
# #     생존
# #   }
# #   아니면{
# #     운임이 100 이상이면{
# #       생존
# #     }
# #     아니면{
# #       사망
# #     }
# #     ...
# #   }
# # }
# 


#Age

#2번에서 결측값 채운 데이터 이용
train$Age



train$ages <-cut(train$Age,
                 breaks=c(0,10,20,30,40,50,max(titanic$Age,na.rm = T)+1),
                 right=FALSE,
                 labels=c(0:5)
)
train$ages


#Pclass
train$Pclass <- factor(train$Pclass,order=TRUE,levels=c(3,2,1))
train$Pclass

#Sex
train$Sex<-ifelse(train$Sex=='male',0,1)
train$Sex

#나이X생존률
proportions(table(train[,c('ages','Survived')]),1)

# ages  0         1
# 0 0.3870968 0.6129032
# 1 0.5980392 0.4019608
# 2 0.6500000 0.3500000
# 3 0.5628743 0.4371257
# 4 0.6179775 0.3820225
# 5 0.6351351 0.3648649

#성별x생존률
proportions(table(train[,c('Sex','Survived')]),1)
# Sex    0         1
# 0 0.8110919 0.1889081
# 1 0.2579618 0.7420382

#등급X생존률
proportions(table(train[,c('Pclass','Survived')]),1)

# Survived
# Pclass         0         1
# 1 0.3703704 0.6296296
# 2 0.5271739 0.4728261
# 3 0.7576375 0.2423625

# 성별X등급X생존률
with(train,aggregate(Survived,list(sex=Sex,pclass=Pclass),mean))

#    sex pclass         x
# 1   0      1 0.3688525
# 2   1      1 0.9680851
# 3   0      2 0.1574074
# 4   1      2 0.9210526
# 5   0      3 0.1354467
# 6   1      3 0.5000000
# -> Pclass 3일때, 여자도 생존률 낮음


# 성별X나이X생존률
with(train,aggregate(Survived,list(sex=Sex,age=ages),mean))
#     sex age         x
# 1    0   0 0.5135135
# 2    1   0 0.5277778
# 3    0   1 0.1206897
# 4    1   1 0.7391304
# 5    0   2 0.1440678
# 6    1   2 0.7196262
# 7    0   3 0.2155172
# 8    1   3 0.8529412
# 9    0   4 0.2179487
# 10   1   4 0.7142857
# 11   0   5 0.1346154
# 12   1   5 0.9090909

#age=0일때, 남자 생존률 높음

with(train,aggregate(Survived,list(sex=Sex,age=ages,pclass=Pclass),mean))

#     sex age pclass          x
# 1    0   0      1 1.00000000
# 2    1   0      1 0.00000000
# 3    0   1      1 0.40000000
# 4    1   1      1 1.00000000
# 5    0   2      1 0.50000000
# 6    1   2      1 0.93750000
# 7    0   3      1 0.52173913
# 8    1   3      1 1.00000000
# 9    0   4      1 0.31111111
# 10   1   4      1 1.00000000
# 11   0   5      1 0.20689655
# 12   1   5      1 0.93333333
# 13   0   0      2 1.00000000
# 14   1   0      2 1.00000000
# 15   0   1      2 0.10000000
# 16   1   1      2 1.00000000
# 17   0   2      2 0.00000000
# 18   1   2      2 0.88000000
# 19   0   3      2 0.12500000
# 20   1   3      2 0.94736842
# 21   0   4      2 0.12500000
# 22   1   4      2 0.90000000
# 23   0   5      2 0.07692308
# 24   1   5      2 0.83333333
# 25   0   0      3 0.30769231
# 26   1   0      3 0.40740741
# 27   0   1      3 0.09302326
# 28   1   1      3 0.52000000
# 29   0   2      3 0.13157895
# 30   1   2      3 0.60606061
# 31   0   3      3 0.15094340
# 32   1   3      3 0.43750000
# 33   0   4      3 0.08000000
# 34   1   4      3 0.00000000
# 35   0   5      3 0.00000000
# 36   1   5      3 1.00000000

# 남자 & 10대이하(age=0)이 생존률 높은 것을 위에서 확인했지만, 3등급의 경우 해당하지 않음
# 여자 전체 생존률이 0.74이지만, 3등급 여자 생존률은 약 0.5
# 남자& 10대이하 & 2등급 전원 생존


#모델링
#1.성별이 가장 중요한 변수이므로 ,Survived 남:0 , 여:1 로 설정
#2. 10대 이하 남자(3등급 제외)는 Survived 1로 수정
#3. 3등급 남녀 모두 Survived 0으로 수정

library(dplyr)

train<-train %>% 
  mutate(Pred=ifelse(Sex==0,0,1))


for(i in seq(1:nrow(train))){
  if( train$ages[i]==0&train$Pclass[i]%in%c(1,2) ){
    train$Pred[i]<-1
  }
  else if(train$Pclass[i]==3){
    train$Pred[i]<-0
  }
}


sum(train$Pred==train$Survived)/nrow(titanic)



#test set에 적용
#Age
test$Age
test$ages <-cut(test$Age,
                breaks=c(0,10,20,30,40,50,max(titanic$Age,na.rm = T)+1),
                right=FALSE,
                labels=c(0:5)
)
test$ages


#Pclass
test$Pclass <- factor(test$Pclass,order=TRUE,levels=c(3,2,1))
test$Pclass

#Sex

test$Sex


test<-test%>% 
  mutate(Survived=ifelse(Sex==0,0,1))


for(i in seq(1:nrow(test))){
  if( test$ages[i]==0&test$Pclass[i]%in%c(1,2) ){
    test$Survived[i]<-1
  }
  else if(test$Pclass[i]==3){
    test$Survived[i]<-0
  }
}

tail(test,5)

submission_model2<-test[,c('PassengerId','Survived')]
submission_model2

write.csv(submission_model2,file='submission_model2.csv',row.names = F)

# 3. 타이타닉 문제에 대해 knn 적용
# set.seed(1234)
# idx<-sample(1:nrow(train),nrow(train)*0.8) 
# train<-train[idx,]
# train<-train[-idx,]

library(class)

normalize<-function(x){
  return ( (x-min(x) )/( max(x)-min(x) ) )
  
}

train_num <- data.frame(sapply(train[,c('Pclass', 'SibSp', 'Parch', 'Fare','Embarked','Sex','Age')], as.numeric))
train_n<-as.data.frame(lapply(train_num,normalize))



test_num<-data.frame(sapply(test[,c('Pclass', 'SibSp', 'Parch', 'Fare','Embarked','Sex','Age')], as.numeric))
test_n<-as.data.frame(lapply(test_num,normalize))

titanic_train_labels <-train[,'Survived']


titanic_test_pred<-knn(train=train_n,test=test_n,cl=titanic_train_labels,k=5)

titanic_test_pred#예측


submission_model3<-as.data.frame(cbind(test$PassengerId,titanic_test_pred))

colnames(submission_model3)[1] <- 'PassengerId'
colnames(submission_model3)[2] <- 'Survived'
submission_model3$Survived<-ifelse(submission_model3$Survived==1,0,1)
submission_model3


write.csv(submission_model3,file='submission_model3.csv',row.names = F)



########다른 방법######3


train <- read.csv('./titanic/train.csv', na.strings = "")
test <- read.csv('./titanic/test.csv', na.strings = "")

#### train ####
tr.copy <- train[,-c(1,4,9,11)] # Id, Name, Ticket, Cabin 삭제

# Embarked NA 있는 행 삭제
tr.copy <- tr.copy[!is.na(tr.copy$Embarked),]

# train Age NA 대체 (3번)
tr.copy$Age <- train.copy$Age

# train Age level 나누기 
tr.age.lvl <- cut(tr.copy$Age, 
                  breaks = c(0,10,20,30,40,50,80),
                  labels = c(1:6)
)
tr.copy$age.lvl <- tr.age.lvl

#### train set sampling ####
set.seed(1234)
idx <- sample(1:nrow(tr.copy), nrow(tr.copy)*0.8)
tr_train <- tr.copy[idx,]
tr_test <- tr.copy[-idx,]

tr_train_cl <- tr.copy[idx,1]
tr_test_cl <- tr.copy[-idx,1]

# 조건식 (sex, age.lvl, SibSp, Parch, Pclass)
tr_pred <- with(tr_train, 
                ifelse(Sex=='female',1,0)) # 0.782

tr_pred <- with(tr_train, 
                ifelse(Sex=='female',1,
                       ifelse(Pclass==1,1,0))) # 0.757

tr_pred <- with(tr_train, 
                ifelse(fe.class==1,1,
                       ifelse(Sex=='female'& age.lvl %in% c(1,2,3),1,0 ))) # 0.647

tr_pred <- with(tr_train, 
                ifelse(fe.class==1,1,
                       ifelse(Sex=='female'& age.lvl %in% c(1,2,3),1,
                              ifelse(Sex=='male' & age.lvl %in% c(1) & Pclass %in% c(1),1,0)))) # 0.65

tr_pred <- with(tr_train, 
                ifelse(Sex=='female' & Pclass==1,1,
                       ifelse(Sex=='female'& age.lvl %in% c(1,2,3),1,
                              ifelse(Sex=='male' & age.lvl %in% c(1) & Pclass %in% c(1),1,0)))) # 0.774

round(sum(tr_pred==tr_train_cl)/length(tr_pred), digits=3)



#test 데이터 
ts.copy <- test[,-c(1,3,8,10)] # Id, Name, Ticket, Cabin 삭제

# test NA 대체 (3번문제)
ts.copy$Age <- ts_n$Age
ts.copy$Fare <- ts_n$Fare

nrow(test)
str(ts.copy)

# test Age level 나누기 
ts.age.lvl <- cut(ts.copy$Age, 
                  breaks = c(0,10,20,30,40,50,80),
                  labels = c(1:6)
)
ts.copy$age.lvl <- ts.age.lvl

# 모델
ts_pred <- with(ts.copy, 
                ifelse(Sex=='female',1,
                       ifelse(Pclass==1,1,0))) # 0.70574

ts_pred <- with(ts.copy, 
                ifelse(Sex=='female' & Pclass==1,1,
                       ifelse(Sex=='female'& age.lvl %in% c(1,2,3),1,
                              ifelse(Sex=='male' & age.lvl %in% c(1) & Pclass %in% c(1),1,0)))) # 0.76555

ts_res <- cbind(PassengerId=test[,'PassengerId'], Survived=ts_pred)
write.csv(ts_res, './titanic/0309_SexPclass.csv', row.names=F)
