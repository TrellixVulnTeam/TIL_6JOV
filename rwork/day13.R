#유클리디안, 맨하튼 , 코사인, 민코프스키 거리

#표준화와 정규화
#표준화: 평균과 얼만큼 떨어져 있는지 .. 멀리 떨어져 있을수록 가중치를 크게 둔다


train<-read.csv("train.csv")
train
test<-read.csv("test.csv")
test

#Name,Ticket,Cabin컬럼 제거
train<-train[,-c(4,9,11)]
names(test)
test<-test[,-c(3,8,10)]

#성별 0,1로 변환
#Switch함수(ifelse문과 비슷): 특정 인덱스에 대한 구문(함수)를 수행할 수 있음
# x<-c(5,6,7,8)
# switch(1,mean(x),sum(x),var(x))
# switch(2,mean(x),sum(x),var(x))
# switch(3,mean(x),sum(x),var(x))

train$Sex<-sapply(train$Sex,switch, 'male'=0,'female'=1)

test$Sex<-sapply(test$Sex,switch, 'male'=0,'female'=1)

#승선 항구 c=0, Q=1, S=2로 변환
train$Embarked<-sapply(train$Embarked,switch,'C'=0,'Q'=1,'S'=2)
test$Embarked<-sapply(test$Embarked,switch,'C'=0,'Q'=1,'S'=2)


#나이와 운임 열에 대해 na제거
train_age<-na.omit(train$Age)
train_age
train_age_avg<-mean(train_age)  #na를 제외한 나머지 평균
train$Age[is.na(train$Age)]<-train_age_avg

test_age<-na.omit(test$Age)
test_age
test_age_avg<-mean(test_age)  #na를 제외한 나머지 평균
test$Age[is.na(test$Age)]<-test_age_avg


test_fare<-na.omit(test$Fare)
test_fare
test_fare_avg<-mean(test_fare)  #na를 제외한 나머지 운임 평균
test$Fare[is.na(test$Fare)]<-test_fare_avg


#나이가 18세 이상이면 0, 아니면 1로 치환

train$Age<-ifelse(train$Age<18,1,0)
test$Age<-ifelse(test$Age<18,1,0)

#정규회(운임, 등실)
normalize<-function(x){
  num<-x-min(x)
  denom<-max(x)-min(x)
  return(num/denom)
}

train$Pclass<-normalize(train$Pclass)
test$Pclass<-normalize(test$Pclass)


test_length<-length(test$Fare)
fare<-normalize(c(train$Fare,test$Fare))
fare
train$Fare<-fare[1:(length(fare)-test_length)] #Train데이터 추출
test$Fare<-fare[(length(fare)-test_length+1):length(fare)]


#결측값: 딥러닝 예측, 회귀모델, .. 머신러닝
iris
install.packages("ggvis")
library(ggvis)
library(dplyr)


iris %>% 
  ggvis(~Petal.Length, ~ Petal.Width, fill=~factor(Species)) %>% 
  layer_points()

mmn<-function(x){
  num<-x-min(x)
  denom<-max(x)-min(x)
  return(num/denom)
}

iris_n<-as.data.frame(lapply(iris[1:4],mmn))
summary(iris_n)

#67%:33%
table(iris$Species)
set.seed(1234)
rs<-sample(2,nrow(iris),replace=TRUE,prob=c(0.67,0.33))
iris[rs==1,1:4]  #train데이터(67%)
iris[rs==2,1:4]   #test(33%)

train.label<-iris[rs==1,5]  #train(67%)
test.label<-iris[rs==2,5]   #test(33%)


library(class)


pred<-knn(train=train, test=test, cl=train.label, k=3)

sum(pred==test.label)/length(pred)
#or
library(gmodels)
CrossTable(x=test.label,y=pred)


plot(faithful
     main='main title',
     sub='sub title',
     xlab='eruption time(min)',
     ylab='waiting time to next eruption')

#las 옵션: 레이블 방향 변경
plot(faithful)
plot(faithful, las=0) #Plot(faithful)와 같음
plot(faithful, las=1)
plot(faithful, las=2)
plot(faithful, las=3)

#bty변수:그래프 외곽선 모양 설정
plot(faithful)
plot(faithful, bty='n') #Plot(faithful)와 같음
plot(faithful, bty='l')
plot(faithful, bty='l')
plot(faithful, bty=']')

#pch옵션
#help에서 points 검색 
plot(faithful)
plot(faithful, pch=24)

plot(faithful, pch=24, col='green2', bg='blue')


plot(LakeHuron)
str(LakeHuron)
#선의 유형 지정
plot(LakeHuron, lty='solid') #default
plot(LakeHuron, lty='dashed')
plot(LakeHuron, lty='twodash')
plot(LakeHuron, lty='dotted')



pressure
plot(pressure)
plot(pressure,type='p')  #default
plot(pressure,type='l')
plot(pressure,type='b')  #both: 점 선 다 표현
plot(pressure,type='o')  #overplot: 선과 점이 겹쳐져 나옴
plot(pressure,type='h')  #histogram
plot(pressure,type='s')  #step:계단형식


#type='n' nothing, 크래프 틀만 생성
#사용자 정의 형식의 그래프 생성하고자 할 때 사용
x<-1:10
y1=exp(1:10)  #자연상수 2.718의 1승부터 10승까지 
y2<-exp(10:1)

#line함수는 단독으로 쓰일 수 없어서 plot호출 후 
plot(x,y1,type='n',ylab='y')
lines(x,y1,type='o',col='red')
lines(x,y2,type='o',col='blue')


##1)격자 모양을 출력
plot(faithful, type='n')
#점선 격자무늬
grid()
points(faithful,pch=19,col='blue')
#2)격자 모양을 출력
dev.off()
plot(faithful, pch=19,col='blue')
grid()



####다음주#####
#맥쥬->땅콩, 담배->껌, 라이터...
#물건1을 구매했을 때 어떤 물건들이 추가적으로 구매될 수 있는지
#가장 구매가 함께 될 수 있도록 추천해주는 시스템 만듦.
#상품 배치(진열)할 때 함께 구매되는 경향이 있는 상품들을 진열->매출액 상승


#이메일: 조건부 확률->베이즈 이론->베이지안필터기->광고메일/일반메일 분류

#클러스터링(집단 분할)

#텍스트마이닝

#영화/음악 추천시스템 제작










colors()   #col속성 값
head(colors(),10)
grep('purple',colors(),value=TRUE)


palette('default') #기본 색상 파레트
palette()
pie(rep(1,12),col=1:12)



palette(rainbow(6))  #변경 파레트
palette()
pie(rep(1,12),col=1:12)




pie(rep(1,12),col=gray(level = seq(0,1,length=12)))

#alpha:투명도, 0이면 완전 투명, 1이면 불투평
pie(rep(1,12),col=rainbow(12,alpha = seq(0,1,length=12)))


#관련 help를 참고하여 색상 설정
pie(rep(1,12), col=heat.colors(12))
pie(rep(1,12), col=terrain.colors(12))
pie(rep(1,12), col=cm.colors(12))


install.packages('mlbench')
library(mlbench)
data('Ozone')

plot(Ozone$V8, Ozone$V9)
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone',pch='+')
#구글 검색 :r pch symbols 검색


plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone', cex=1) #기본크기
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone', cex=0.1)
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone', cex=2)


plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone', cex=0.1,col='red')
colors()

#좌표 축 값의 범위 설정
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone', cex=0.1,col='red',xlim=c(0,150),ylim = c(0,100))


cars
plot(cars, type="l")
plot(cars, type='o', cex=0.5)


plot(cars, type='o')

cars

#speed하나에 2개 이상의 dist를 가지고 있어서
#각각의 스피드마다 dist의 평균 구해서


#퀴즈
library(dplyr)
cars %>% group_by(speed) %>% summarise(mean(dist))

#tapply(데이터, 색인, 함수)

tapply(cars, list(speed, dist), mean) 

#1은 1번그룹, 2는 1번그룹, 10은 1번그룹
#모든 수가 1번 그룹에 소속
tapply(1:10, rep(1,10),sum)

#1~10까지의 숫자를 홀수 , 짝수별 합계
tapply(1:10, 1:10%%2==1,sum)

#iris에서 종별 Sepal.length의 평균
tapply(iris$Sepal.Length, iris$Species, mean)

#퀴즈
library(dplyr)
tapply(cars$dist, cars$speed, mean)


plot(tapply(cars$dist, cars$speed, mean),tpye='o',xlab='speed',ylab='dist',cex=0.7)

#창을 2칸으로 나누어 시각화
opar<-par(mfrow=c(1,2))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone2')


par(opar)
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')



p11<-par(mfrow=c(1,1))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')

p12<-par(mfrow=c(1,2))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')


par(p11)  #기존에 설정된 화면 출력 방식을 불러오기
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')

dev.off()
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')



p21<-par(mfcol=c(2,1))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')



p22<-par(mfcol=c(2,2))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')


p22<-par(mfrow=c(2,2))
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')
plot(Ozone$V8, Ozone$V9,xlab='sandburg',ylab='El Monte',main='Ozone')












