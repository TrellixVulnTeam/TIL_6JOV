
train <- read.csv('train.csv', na.strings = "")
test <- read.csv('test.csv', na.strings = "")


#### NA 몇 개 있는지 확인 ####
paste(1:ncol(train), names(train), apply(is.na(train), 2, sum))
# "6 Age 177"   "11 Cabin 687"    "12 Embarked 2"  


#### Name에서 호칭 종류로 name 변수 만들기 ####
call <- unlist(strsplit(train$Name, split=' '))
name <- grep('^[A-Z][a-z]+[.]$', call, value=T)
train <- cbind(train, name)


#### chr 변수를 num 으로 변경 ####
toNum <- function(x) {
  f <- factor(x, labels=(1:length(unique(na.omit(x)))))
}

name.int <- toNum(train[,'name']) # Capt.=1, ..., 
sex.int <- toNum(train[,'Sex']) # female=1, male=2
emb.int <- toNum(train[,'Embarked']) # C=1, Q=2, S =3


#### 숫자로 변환한 factor 원데이터에 추가 ####
train <- cbind(train, name.int, sex.int, emb.int)

head(train)

#### Embarked NA 채우기 ####
# Ticket 번호 유사한 애들과 비교
which(is.na(train$Embarked)) # 62 830
train$Ticket[c(62,830)] # "113572" "113572"
grep('1135[\\d]*', train$Ticket, value=T) # "113509" "113572" "113505" "113514" "113510" "113505" "113503" "113501" "113572"
names(which.max(table(train$emb.int[grep('1135[\\d]*', train$Ticket)]))) # 3

grep('113[\\d]*', train$Ticket, value=T)
names(which.max(table(train$emb.int[grep('113[\\d]*', train$Ticket)]))) # 3
train$emb.int[c(62,830)] <- '3'


#### num형태의 데이터 값을 표준화한 데이터프레임 'scaled' 만들기 ####
df <- data.frame(sapply(train[,c('Pclass', 'SibSp', 'Parch', 'Fare', 'name.int', 'sex.int', 'emb.int')], as.numeric))
df
tr.scaled <- as.data.frame(sapply(df, scale))
tr.scaled <- cbind(Id=train$PassengerId, tr.scaled, Age=train$Age)
head(tr.scaled)

#### 유클리드 거리로 NA 채우기 ####
#### Age ####
#NA인 개수
target <- which(is.na(tr.scaled$Age)) # index (length: 177)

# cor 소수점 둘째 자리에서 반올림했을 때 0.3 이상인 것 --> Age.na1: Pclass, SibSp, name.int
cor(na.omit(train$Age), tr.scaled[-target,-1])
# Pclass      SibSp      Parch      Fare        name.int  sex.int    emb.int Age
# -0.369226   -0.3082468 -0.1891193 0.09606669  0.2941115 0.09325358 -0.03039433   1


compare <- tr.scaled[-target,]
train$Age.na1_10 <- train$Age # 원본 보존 위해


for (i in target) {
  df <- t(compare[,c('Pclass', 'SibSp','name.int')]) - as.numeric(tr.scaled[i,c('Pclass', 'SibSp','name.int')])
  euc.dist <- sqrt(colSums(df^2))
  idx <- order(euc.dist)[1:10]
  train$Age.na1_10[i] <- mean(compare$Age[idx])
}

tr.scaled$age.na1_05 <- as.numeric(scale(train$Age.na1_05)) # 상위 5개 평균
tr.scaled$age.na1_10 <- as.numeric(scale(train$Age.na1_10)) # 상위 10개 평균


#### 연령대 나누어 표준화한 변수 만들기 ####
age.lvl <- cut(train$Age.na1_05, 
               breaks = c(0,10,20,30,40,50,80),
               labels = c(1:6)
)
tr.scaled$age.lvl_05 <- as.vector(scale(as.numeric(age.lvl)))


age.lvl <- cut(train$Age.na1_10, 
               breaks = c(0,10,20,30,40,50,80),
               labels = c(1:6)
)

tr.scaled$age.lvl_10 <- as.vector(scale(as.numeric(age.lvl)))
tr.scaled$age.lvl_10

#### 유클리드 거리 모델 train에 테스트 ####
pred <- data.frame(pred1=c(1:nrow(train)))

paste(names(tr.scaled), 1:ncol(tr.scaled))
# [1] "Id 1"          "Pclass 2"      "SibSp 3"       "Parch 4"       "Fare 5"        "name.int 6"   
# [7] "sex.int 7"     "emb.int 8"     "Age 9"         "age.na1_05 10" "age.na1_10 11" "age.lvl_05 12"
# [13] "age.lvl_10 13"


for (i in 1:nrow(tr.scaled)) {
  df <- t(tr.scaled[,c(2:5,7,8,13)])-as.numeric(tr.scaled[i,c(2:5,7,8,13)])
  euc.dist <- sqrt(colSums(df^2))
  comp <- order(euc.dist)[1:21]
  pred$pred8[i] <- as.numeric(names(which.max(table(train$Survived[comp]))))
  print(i)
}


# order(euc.dist)[1:11]
sum(train$Survived==pred$pred1)/nrow(train) # 0.8338945 [,c(2:8,10)] 
sum(train$Survived==pred$pred2)/nrow(train) # 0.8350168 [,c(2:5,7,8,10)]
sum(train$Survived==pred$pred3)/nrow(train) # 0.8271605 [,c(2,5,7)]
sum(train$Survived==pred$pred4)/nrow(train) # 0.8406285 [,c(2:5,7,8,11)]
sum(train$Survived==pred$pred5)/nrow(train) # 0.8473625 [,c(2:5,7,8,12)]
sum(train$Survived==pred$pred6)/nrow(train) # 0.8316498 [,c(2:5,7,12)]
sum(train$Survived==pred$pred6)/nrow(train) # 0.8327722 [,c(2:5,7,13)]
sum(train$Survived==pred$pred7)/nrow(train) # 0.8507295 [,c(2:5,7,8,13)]
# order(euc.dist)[1:21]
sum(train$Survived==pred$pred8)/nrow(train) # 0.8215488 [,c(2:5,7,8,13)]




#2. test 데이터 전처리 및 예측 모델 적용 코드
train <- read.csv('./titanic/train.csv', na.strings = "")
test <- read.csv('./titanic/test.csv', na.strings = "")

#### NA 몇 개 있는지 확인 ####
paste(1:ncol(test), names(test), apply(is.na(test), 2, sum))
# "5 Age 86"  "9 Fare 1"  "10 Cabin 327"   


#### Name에서 호칭 종류로 name 변수 만들기 ####
call <- unlist(strsplit(test$Name, split=' '))
name <- grep('^[A-Z][a-z]+[.]$', call, value=T)
test <- cbind(test, name)


#### chr 변수를 num 으로 변경 ####
toNum <- function(x) {
  f <- factor(x, labels=(1:length(unique(na.omit(x)))))
}

name.int <- toNum(test[,'name']) # Capt.=1, ..., 
sex.int <- toNum(test[,'Sex']) # female=1, male=2
emb.int <- toNum(test[,'Embarked']) # C=1, Q=2, S =3


#### 숫자로 변환한 factor 원데이터에 추가 ####
test <- cbind(test, name.int, sex.int, emb.int)


#### num형태의 데이터 값을 표준화한 데이터프레임 'scaled' 만들기 ####
df <- data.frame(sapply(test[,c('Pclass', 'SibSp', 'Parch', 'Fare', 'Age', 'name.int', 'sex.int', 'emb.int')], as.numeric))
scaled <- as.data.frame(sapply(df, scale))
scaled <- cbind(Id=test$PassengerId, scaled, Fare2=test$Fare, Age2=test$Age)


#### 유클리드 거리로 NA 채우기 ####
#### Fare ####
target <- which(is.na(scaled$Fare)) # index (length: 1)

# cor 소수점 둘째 자리에서 반올림했을 때 절대값 0.3 이상인 것 --> Fare.na1: Pclass, Age, emb.int

cor(na.omit(scaled)$Fare[-target], na.omit(scaled)[-target,-1])
# Pclass     SibSp     Parch      Fare  Age       name.int    sex.int    emb.int
# -0.5854746 0.1527369 0.2473385  1     0.3371862 -0.01659537 -0.1918723 -0.3226839

compare <- na.omit(scaled[-target,])
test$Fare.na1_05 <- test$Fare
test$Fare.na1_10 <- test$Fare # 원본 보존 위해


for (i in target) {
  df <- t(compare[,c('Pclass', 'Age','emb.int')]) - as.numeric(scaled[i,c('Pclass', 'Age','emb.int')])
  euc.dist <- sqrt(colSums(df^2))
  idx <- order(euc.dist)[1:10]
  test$Fare.na1_10[i] <- mean(compare$Fare2[idx])
}

scaled$fare.na1_05 <- as.numeric(scale(test$Fare.na1_05)) # 상위 5개 평균
scaled$fare.na1_10 <- as.numeric(scale(test$Fare.na1_10)) # 상위 10개 평균


#### Age ####
target <- which(is.na(scaled$Age)) # index (length: 86)

# cor 소수점 둘째 자리에서 반올림했을 때 0.3 이상인 것 --> Age.na1: Pclass, name.int, fare.na1_05
cor(na.omit(scaled)$Age[-target], na.omit(scaled)[-target,-c(1,5,6)])
# Pclass     SibSp      Parch      name.int  sex.int   emb.int      fare.na1_05 fare.na1_10
# -0.5095681 -0.1097185 -0.1559856 0.3952369 0.0248228 -0.1733412   0.3495588   0.3495588

compare <- scaled[-target,]
test$Age.na1_05 <- test$Age
test$Age.na1_10 <- test$Age # 원본 보존 위해

for (i in target) {
  df <- t(compare[,c('Pclass', 'name.int','fare.na1_05')]) - as.numeric(scaled[i,c('Pclass', 'name.int','fare.na1_05')])
  euc.dist <- sqrt(colSums(df^2))
  idx <- order(euc.dist)[1:10]
  test$Age.na1_10[i] <- mean(compare$Age2[idx])
}

scaled$age.na1_05 <- as.numeric(scale(test$Age.na1_05)) # 상위 5개 평균
scaled$age.na1_10 <- as.numeric(scale(test$Age.na1_10)) # 상위 10개 평균


#### 연령대 나누어 표준화한 변수 만들기 ####
age.lvl <- cut(test$Age.na1_05, 
               breaks = c(0,10,20,30,40,50,80),
               labels = c(1:6)
)
scaled$age.lvl_05 <- as.vector(scale(as.numeric(age.lvl)))


age.lvl <- cut(test$Age.na1_10, 
               breaks = c(0,10,20,30,40,50,80),
               labels = c(1:6)
)
scaled$age.lvl_10 <- as.vector(scale(as.numeric(age.lvl)))



#### 유클리드 거리 모델 ####
pred.ts <- data.frame(pred1=c(1:nrow(test)))

# train!!!
# [1] "Id 1"          "Pclass 2"      "SibSp 3"       "Parch 4"       "Fare 5"        "name.int 6"   
# [7] "sex.int 7"     "emb.int 8"     "Age 9"         "age.na1_05 10" "age.na1_10 11" "age.lvl_05 12"
# [13] "age.lvl_10 13"

paste(names(scaled), 1:ncol(scaled))
# [1] "Id 1"           "Pclass 2"       "SibSp 3"        "Parch 4"        "Fare 5"        
# [6] "Age 6"          "name.int 7"     "sex.int 8"      "emb.int 9"      "Fare2 10"      
# [11] "Age2 11"        "fare.na1_05 12" "fare.na1_10 13" "age.na1_05 14"  "age.na1_10 15" 
# [16] "age.lvl_5 16"   "age.lvl_10 17"  


for (i in 1:nrow(scaled)) {
  df <- t(tr.scaled[,c(2:4,7,8,10)])-as.numeric(scaled[i,c(2:4,8,9,14)])
  euc.dist <- sqrt(colSums(df^2))
  idx <- order(euc.dist)[1:11]
  pred.ts$pred1[i] <- as.numeric(names(which.max(table(train$Survived[idx]))))
}

res <- cbind(PassengerId=test[,'PassengerId'], Survived=pred.ts$pred1)
write.csv(res, './titanic/res1.csv', row.names=F)

# order(euc.dist)[1:11]
# df <- t(tr.scaled[,c(2:5,7,8,13)])-as.numeric(scaled[i,c(2:4,12,8,9,17)]) # 0.76315
# df <- t(tr.scaled[,c(2:5,7,8,13)])-as.numeric(scaled[i,c(2:4,13,8,9,17)]) # 0.76794
# df <- t(tr.scaled[,c(2:5,7,8)])-as.numeric(scaled[i,c(2:4,13,8,9)]) # 0.74162
# df <- t(tr.scaled[,c(2:5,7,13)])-as.numeric(scaled[i,c(2:4,13,8,17)]) # 0.76794
# df <- t(tr.scaled[,c(2:4,7)])-as.numeric(scaled[i,c(2:4,8)]) # 0.77511
# df <- t(tr.scaled[,c(2:4,6,7)])-as.numeric(scaled[i,c(2:4,7,8)]) # 0.77033
# df <- t(tr.scaled[,c(2:4,7,8)])-as.numeric(scaled[i,c(2:4,8,9)]) # 0.76555
# df <- t(tr.scaled[,c(2:4,7,8,10)])-as.numeric(scaled[i,c(2:4,8,9,14)]) # 0.73923











##############다른 분 풀이

train<-read.csv('train.csv',na.strings = '')
test<-read.csv('test.csv',na.strings='')
str(train)
head(train)
#전처리===========================================================
# 결측치 (Cabin, Age, Embarked)
install.packages("Amelia")
library(Amelia)
missmap(train,col = c('red','blue'))
missmap(test,col = c('red','blue'))

library(ggplot2)
library(GGally)
ggcorr(train,nbreaks = 5,label = T)
ggcorr(test,nbreaks = 5,label = T)


# [1] "PassengerId" "Survived"    "Pclass"      "Name"        "Sex"         "Age"         "SibSp"       "Parch"       "Ticket"      "Fare"       
#[11] "Cabin"       "Embarked"   
names(train)


ggcorr(train,nbreaks = 5,label = T) #Sex, Pclass, Fare가 상관관계가 높게 나옴

# 성별 1,0으로 변환
train$Sex<-ifelse(train$Sex=='female',1,0)
test$Sex<-ifelse(test$Sex=='female',1,0)

# Fare 범주화(quartile별로 1,2,3,4)
splits<-summary(train$Fare)
train$Farecat<-as.numeric(with(train,cut(Fare,breaks=splits[-3],include.lowest=T,labels=c(1,2,3,4))))
test$Farecat<-as.numeric(with(test,cut(Fare,breaks=splits[-3],include.lowest=T,labels=c(1,2,3,4))))


# feature별 생존률 차이 살펴보기
with(train,tapply(Survived,Sex,mean))
for (i in c('Sex','Pclass','Farecat')){
  print(tapply(train[['Survived']],train[[i]],mean))
}
# 0         1  (성별)
# 0.1889081 0.7420382 
# 1         2         3 (Pclass)
# 0.6296296 0.4728261 0.2423625 
# 1         2         3         4 (Fare(범주형))
# 0.1973094 0.3789238 0.2727273 0.5971564 





#Fare, Pclass 정규화
makenormal<-function(target){
  min<-min(target,na.rm=T)
  max<-max(target,na.rm=T)
  return((target-min)/(max-min))
  
}


train$Fare<-makenormal(train$Fare)
train$Pclass<-makenormal(train$Pclass)
test$Fare<-makenormal(test$Fare)
test$Pclass<-makenormal(test$Pclass)

# case1: 유클리디안 거리 (Sex, Pclass, Fare)
features=c('Sex','Pclass','Fare')
y=c('Survived')
train_xy<-train[c(features,y)]

#사전 정확도 검증을 위해 train, test 셋 분리(7대3)
testsplit<-function(x){
  num_data<-nrow(x)
  train_idx<-sample(1:num_data,num_data*0.7)
  test_xy<<-x[-train_idx,]
  train_xy<<-x[train_idx,]
}
testsplit(train_xy)
str(test_xy)
str(train_xy)


#각 샘플별 유클리디안 거리가 유사한 top N개의 데이터의 y의 평균(반올림)값을 뽑아내는 함수
Udist_Nth<-function(test,train,features,y,N){
  predict<<-c()
  for(i in 1:nrow(test[features])){
    idx<-order(colSums((t(train[features])-t(test[features])[,i])^2))[1:N]
    predict<<-c(predict,round(mean(train[idx,y])))
  }
  return(predict)
}

test_xy$Predict<-Udist_Nth(test_xy,train_xy,features,y,5)
sum(test_xy$Survived==test_xy$Predict)/length(test_xy$Survived==test_xy$Predict)


#무작위 샘플 20회로 테스트 해보기
for(sampleset in 1:20){
  features=c('Sex','Pclass','Fare')
  y=c('Survived')
  train_xy<-train[c(features,y)]
  testsplit(train_xy)
  
  predict<-c()
  for(i in 1:nrow(test_xy[features])){
    idx<-order(colSums((t(train_xy[features])-t(test_xy[features])[,i])^2))[1:5]
    predict<-c(predict,round(mean(train_xy[idx,y])))
  }
  test_xy$Predict<-predict
  
  scores<-c()
  scores<-c(scores,sum(test_xy$Survived==test_xy$Predict)/length(test_xy$Survived==test_xy$Predict))
}

mean_20scores<-mean(scores)
mean_20scores#[1] 0.7873134


#test파일 예측하기
test$Survived<-Udist_Nth(test,train,features,y,5)
str(test)

submission<-test[c('PassengerId','Survived')]
View(submission)

#submission파일 만들기
write.csv(submission,paste('data/',as.character(mean_20scores),'.csv',sep=''),row.names = F)

