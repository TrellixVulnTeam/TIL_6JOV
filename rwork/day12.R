#graphics 패키지 : 고수준 그래픽, 저수준 그래픽 함수 
#고수준 그래픽 함수 : 왼전한 하나의 그래프 생성
#plot(), boxplot(), hist(), crve(),...
#저수준 그래픽 함수: 독자적으로 그래프 생성 불가능
#완정된 그래프에 요소를 첨가하는 역할
#points(), lines(), abline(), text(), polygon(),...

plot(faithful)  #산점도 
#분출시간이 길어질 수록 대기시간 또한 길어진다는 상관관계 확인 가능

faithful


#클러스터(cluster):집단

#faithful에서 분출시간이 3분 초과한 데이터 저장
library(dplyr)
eruptions.long<-faithful %>%  filter(eruptions>3)
head(eruptions.long)
#or
eruptions.long <- faithful[faithful$eruptions>3,]
#or
eruptions.long <- faithful %>% filter(eruptions>3)


#col-색상, pch-크기
points(eruptions.long,col='red',pch=19)

#dev.off()->그래프 없앰
dev.off()

#points(eruptions.long,col='red',pch=19) #저수준 그래픽->에러 발생


#선형회귀모델
#분출시간에 따라 대시시간의 변화가 어떠한지
faithful.lm<-lm(waiting ~ eruptions,data=faithful)
#절편: 33.47 기울기: 10.73
faithful.lm

#y=wx+b
#w: 기울기, b: y절편

#!! waiting= 10.73 * x +33.47
#x에 eruptions가 대입->연산->waiting예측



#intercept: 절편


#fitted: 회귀모델에서 예측값 추출
plot(faithful)
points(eruptions.long,col='red',pch=19)
#waiting= 10.73 * x +33.47 (예측값)
fitted(faithful.lm) #예측값 추출

head(fitted(faithful.lm))

#회귀선
lines(x=faithful$eruptions, y=fitted(faithful.lm),col='blue')

#3이라는 값을 지나는 선 추가
abline(v=3,col='purple')

abline(h=mean(faithful$waiting), col='green')




coef(faithful.lm[1])  #절편만 나옴
coef(faithful.lm[2]) #기울기만 나옴

#y=ax+b

abline(a=coef(faithful.lm[1]), b=coef(faithful.lm[2]))


#plot(x) :x타입에 따라 출력되는 그래프가 달라짐.
#x: 벡터, 데이터프레임, 팩터, 시계열, 테이블, 선형회귀모델...
cars
str(cars)
cars$speed
cars$disp

#벡터이므로 산점도 그래프로 출력됨
plot(cars$speed, cars$dist)



str(ToothGrowth)

plot(ToothGrowth$supp, ToothGrowth$len)
#첫번째 인수가 팩터이므로 박스(상자) plot으로 출력


str(iris)
#plot함수로 시각화할때 변수가 2개를 촐과하는 경우에는 
#산점도 행렬로 생성
plot(iris[,1:4])




#시계열 데이터를 plot함수에 넣었을 때 도표로(그래프로) 출력

nhtemp
str(nhtemp)
plot(nhtemp)

UCBAdmissions
str(UCBAdmissions)
#성별과 허가여부에 따른 그래프 출력

plot(UCBAdmissions)
#테이블 데이터는 모자이크 도표로 출력
#모자이크 조각의 크기로 교차표의 상대적 빈도 확인


savePlot('myplot.pdf',type='pdf')
savePlot('myplot.png',type='png')

#저장
png('myplot.png',width=800, height=400)
plot(faithful)
dev.off()


#knn사용사례
#-컴퓨터비전
#-추천시스템(영화, 음악)
#-질병 분류, 유전자 데이터 패턴 인식
#장점: 쉽다, 훈련이 빠르다, 데ㅣㅇ터 분포에 대한 가정을 하지 않는다. 

#단점: k값?, 분류 작업이 느리다, 직관적이지 않다(데이터를 이해하기가 어렵다)


#머신러닝-> knn 알고리즘을 이용한 암 분류기 제작
wbcd<-read.csv('wisc_bc_data.csv')
str(wbcd)

wbcd<-wbcd[-1]
str(wbcd)

table(wbcd$diagnosis)

wbcd$diagnosis<-factor(wbcd$diagnosis, levels = c("B","M"), labels = c("Benign",'Malignant'))
str(wbcd)



round(prop.table(table(wbcd$diagnosis))*100,1)

summary(wbcd[c('radius_mean','area_mean','smoothness_mean')])

normalize<- function(x){
  ((x-min(x))/(max(x)-min(x)))
}

normalize(c(10,20,30,40,50))

str(wbcd)

wbcd_n<-as.data.frame(lapply(wbcd[2:31], normalize))
wbcd_n




wbcd_train<-wbcd_n[1:469,]
wbcd_test<-wbcd_n[470:569,]


wbcd_train_labels<-wbcd[1:469,1]
wbcd_test_labels<-wbcd[470:569,1]

#모델 생성
#주변에 있는 가까운 21개의 데이터를 검색하고 그 데이터를 다수결로 해서 판단.

library(class)
wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test,
    cl=wbcd_train_labels, k=21)

wbcd_test_pred  #예측결과

wbcd_test_labels  #정답


#cross table 
library(gmodels)
CrossTable(x=wbcd_test_labels, y = wbcd_test_pred)



#표준화
wbcd_z<-as.data.frame(scale(wbcd[-1]))
summary(wbcd_z$area_mean)


wbcd_train<-wbcd_z[1:469,]
wbcd_test<-wbcd_z[470:569,]

wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test,
                    cl=wbcd_train_labels, k=21)


install.packages(c("gmodels"))
library(gmodels)
CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)


#k값에 대해 변화를 주면서 가장 테스트 정확도가 높았을 때 K값?

wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test,
                    cl=wbcd_train_labels, k=i)

#퀴즈2
scores<-c()
for(i in seq(1,25,2)){
  wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test,
                      cl=wbcd_train_labels, k=i)
  
scores=c(scores,sum(wbcd_test_labels==wbcd_test_pred)/length(wbcd_test_pred))
}
seq(1,25,2)[which.max(scores)]



# wbcd_test_pred<-knn(train=wbcd_train, test=wbcd_test,
#                     cl=wbcd_train_labels, k=21)
# wbcd_test_pred
# 
# CrossTable(x=wbcd_test_labels, y=wbcd_test_pred)


#or
for (i in seq(1, 25, 2)) {
  wbcd_test_pred <- knn(train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=i)
  print(paste(i, sum(wbcd_test_labels==wbcd_test_pred)/length(wbcd_test_pred)))
}





