#kmenas: 머신러닝 알고리즘(클러스터링)
#knn과 비슷(혼동하면 안됨)

#1.ㅏ?
#-사전 지식->그룹의 개수 결정
#-시각화->그룹의 개수 결정
#sq

#curve:(함수 또는 표현식, 시작점, 끝점)
curve(sin,0,2*pi)

data(cars)
#cars 선형회귀->신뢰구간 출력
#speed, dist
dev.off()
m<-lm(dist~speed,cars)  #종속변수(y축)~ 독립변수(x축)
m
plot(cars)
abline(m)


#speed에 따라 dist 어떻게 되는지 
#fit: 회귀모델로 적합된 값 
#lwr:신뢰구간의 하한
#upr:신뢰구간의 상한
p<-predict(m, interval = 'confidence')
p

# fit        lwr       upr
# 1  -1.849460 -12.329543  8.630624
#-1.849460dms cars의 첫번째 데이터 speed 4에 대한 dist 예측값



#다각형(x의 첫번째 인수와 y의 첫번째 인수 한 점...)

x<-c(cars$speed, tail(cars$speed,1), rev(cars$speed), cars$speed[1])
y<-c(p[,'lwr'],tail(p[,'upr'],1),rev(p[,'upr']),p[,'lwr'][1])

polygon(x,y,col=rgb(.7,.7,.7,.1))

plot(cars, cex=0.5)
#글자 출력 ,pos는 글자 위치

text(cars$speed, cars$dist, pos=3, cex=.5)

plot(cars, cex=0.5)
identify(cars$speed, cars$dist)



#범례출력
plot(iris$Sepal.Width, iris$Sepal.Length, cex=.5, pch=20, xlab='width',ylab='length')
points(iris$Petal.Width,iris$Petal.Length, cex=.5, pch='+',col='red')
legend('topright', legend=c('Sepal','Petal'), pch=c(20,43), cex=.8, col=c('black','red'), bg='gray')



boxstats<-boxplot(iris$Sepal.Width)
boxstats


boxstats<-boxplot(iris$Sepal.Width,horizontal = TRUE)

# $stats
# [,1]
# [1,]  2.2
# [2,]  2.8
# [3,]  3.0
# [4,]  3.3
# [5,]  4.0
#outlier
# $out
# [1] 4.4 4.1 4.2 2.0



#hist():자료의 분포를 알아내고자 할 때 많이 사용

hist(iris$Sepal.Length)
#hist(x, breaks= 'struges')
#sturges= log2(n)+1, n은 자료의 개수 :막대의 구간을 설정
log2(150)


x<-hist(iris$Sepal.Length, freq = FALSE)  # freq= FALSE면적의 합이 1이 됨
x  #histogram 의 정보 


#밀도 그림 그래프 (hitogram에서 중심을 지나도록 그려짐)
plot(density(iris$Sepal.Width))

dev.off()
plot(density(iris$Sepal.Width))

#
hist(iris$Sepal.Width,freq=FALSE)
lines(density(iris$Sepal.Width))


#막대 그래프
#barplot()
barplot(tapply(iris$Sepal.Width, iris$Species, mean))



#구간을 2개로 나눔: (0,5], (5,10], 각각의 데이터가 어느 구간에 속했는지 나옴
cut(1:10, c(0,5,10))
cut(1:10, breaks=3)

#데이터의 비율: pie그래프
cut(iris$Sepal.Width, breaks=10)
table(cut(iris$Sepal.Width, breaks=10))
pie(table(cut(iris$Sepal.Width, breaks=10)), cex=.7)

# rep(c('a','b','c'),1:3)
# table(rep(c('a','b','c'),1:3))


#3개의 층으로 시각화:
#가장 아래쪽: 배경
#2번째 층: 그래프 
#3번째 층: 범위, 색상, 
install.packages("ggplot2")
library(ggplot2)

#aes축 정보 설정
ggplot(data=mtcars, aes(x=wt, y=mpg))+
  geom_point()+
  labs(title='mytitle',
       x='weight', y='mpg')

####################################################
class(mtcars$gear)
mtcars$gear<-factor(mtcars$gear,levels = c(3,4,5),
                    labels = c('3 gears','4 gears','5 gears'))

mtcars$cyl<-factor(mtcars$cyl,levels = c(4,6,8),
                    labels = c('4 cylinders','6 cylinders','8 cylinders'))



ggplot(data=mtcars, aes(x=mpg))+
         geom_histogram()+
         facet_grid(cyl~.)+  #실린더에 따라 나누어 데이터 
         labs(title="cyl vs mpg")
         



ggplot(data=mtcars, aes(x=cyl, y=mpg))+
  geom_boxplot()+
  labs(x='cyl',y='mpg')





ggplot(data=mtcars, aes(x=mpg, fill=cyl))+
  geom_density()+
  labs(x='mpg')




####################################################

ggplot(data=mtcars, aes(x=wt, y=mpg))+
  geom_point()+
  labs(title='mytitle',
       x='weight', y='mpg')





#kmeans기반 10대 학생 시장 세분화

teens<-read.csv('snsdata.csv')
str(teens)

table(teens$gender)
#na를 범주로 참고하게 
table(teens$gender, useNA='ifany')

#NA몇개인지 알기 위해
summary(teens$age)
#NA, 3살 106살 ->전처리

#13세 이상, 20세 미만: 정상 범위
#이 범위 벗어나면 NA로 처리
teens$age<-ifelse(teens$age>=13 & teens$age<20, teens$age, NA)
summary(teens$age)

#성별 NA 처리?
#NA자체 종류를 따로 만들기
teens$female<-ifelse(teens$gender=='F' & !is.na(teens$gender),1,0)  #여성인지의 여부?
#0인 경우: 남성 or NA
teens$nogender<-ifelse(is.na(teens$gender),1,0) #성별이 없는지 여부?

table(teens$gender,useNA = 'ifany')
table(teens$female,useNA = 'ifany')
table(teens$nogender, useNA = 'ifany')

mean(teens$age, na.rm=TRUE)


#퀴즈1. 
#졸업연도별 나이 평균 출력
library(dplyr)
teens %>% group_by(gradyear) %>% 
  summary(mean(age, na.rm=TRUE))

tapply(teens$age, teens$gradyear,mean,na.rm=T)
# 2006     2007     2008     2009 
# 18.65586 17.70617 16.76770 15.81957 

aggregate(data=teens, age~gradyear, mean, na.rm=T)


#ave_age<-ave(data, group, fun)
ave_age<-ave(teens$age, teens$gradyear, FUN=function(x) mean(x, na.rm = TRUE)) #디폴트는 mean인데 
#NA제거 하기 위해서 사용자 지정 함수로 설정

teens$age<-ifelse(is.na(teens$age), ave_age, teens$age) #결측값 대체
teens$age

summary(teens$age)


#kmeans 클러스터링
interests<-teens[5:40]
interests_z<-as.data.frame(lapply(interests, scale))
interests_z

#data.frame으로 바꾼 이유는 kmeans에 대상이 df여야 함


#36차원 데이터
set.seed(2345)
teen_clusters<-kmeans(interests_z, 5)
teen_clusters

teen_clusters$size #각 클러스터에 할당된 데이터 개수
teen_clusters$centers #각 클러스터의 중심점 행렬
teen_clusters$cluster #각 데이터별 할당된 클러스터 번호

teen_clusters$withinss  #각 클러스터 내의 데이터간 거리의 제곱 합, 작을수록 클러스터링이 잘 된 것
teen_clusters$tot.withinss

teen_clusters$betweenss #클러스터 간 중심의 거리 제곱합, 크면 클 수록 좋음(클러스터 간 이질성)



##
teens$cluster<-teen_clusters$cluster
teens

#클러스터  나이의 평균
aggregate(data=teens, age ~ cluster, mean)
#클러스터 성비
aggregate(data=teens, female~cluster,mean ) #3번 클러스터가 가장 많다

#클러스터 친구수
aggregate(data=teens, friends ~cluster, mean)



