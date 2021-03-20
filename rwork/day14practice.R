# 1.mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# mpg 데이터 원본에는결측치가 없습니다. 우선 mpg 데이터를 불러와 몇 개의 값을 결측치로 만들겠습니다. 
# 아래 코드를 실행하면 다섯 행의 hwy 변수에 NA가 할당됩니다.
mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA # NA 할당하기



# Q1. drv(구동방식)별로 hwy(고속도로 연비) 평균이 어떻게 다른지 알아보려고 합니다. 분석을 하기 전에
# 우선 두 변수에 결측치가 있는지 확인해야 합니다. drv 변수와 hwy 변수에 결측치가 몇 개 있는지
# 알아보세요.
sum(is.na(mpg$drv))
sum(is.na(mpg$hwy))
# Q2. filter()를 이용해 hwy 변수의 결측치를 제외하고, 어떤 구동방식의 hwy 평균이 높은지 알아보세요. 
# 하나의 dplyr 구문으로 만들어야 합니다.

mpg %>% 
  filter(!is.na(hwy)) %>% 
  group_by(drv) %>% 
  summary(mean(hwy))
                 

# 2. mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# 우선 mpg 데이터를 불러와서 일부러 이상치를 만들겠습니다. drv(구동방식) 변수의 값은 4(사륜구동), 
# f(전륜구동), r(후륜구동) 세 종류로 되어있습니다. 몇 개의 행에 존재할 수 없는 값 k를 할당하겠습니다. 
# cty(도시 연비) 변수도 몇 개의 행에 극단적으로 크거나 작은 값을 할당하겠습니다.
mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기
mpg[c(10, 14, 58, 93), "drv"] <- "k" # drv 이상치 할당
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42) # cty 이상치 할당

# 이상치가 들어있는 mpg 데이터를 활용해서 문제를 해결해보세요.
# 구동방식별로 도시 연비가 다른지 알아보려고 합니다. 분석을 하려면 우선 두 변수에 이상치가 있는지
# 확인하려고 합니다.
# • Q1. drv 에 이상치가 있는지 확인하세요. 이상치를 결측 처리한 다음 이상치가 사라졌는지 확인하세요. 결측
# 처리 할 때는 %in% 기호를 활용하세요.
table(mpg$drv)

mpg$drv<-ifelse(mpg$drv %in% c('4','f','r'), mpg$drv, NA)

table(mpg$drv)

dev.off()
# • Q2. 상자 그림을 이용해서 cty 에 이상치가 있는지 확인하세요. 상자 그림의 통계치를 이용해 정상 범위를
# 벗어난 값을 결측 처리한 후 다시 상자 그림을 만들어 이상치가 사라졌는지 확인하세요.
boxplot(mpg$cty)$stats

mpg$cty<-ifelse(mpg$cty < 9 | mpg$cty>26, NA, mpg$cty)

boxplot(mpg$cty)


# • Q3. 두 변수의 이상치를 결측처리 했으니 이제 분석할 차례입니다. 이상치를 제외한 다음 drv 별로 cty
# 평균이 어떻게 다른지 알아보세요. 하나의 dplyr 구문으로 만들어야 합니다.
mpg %>% 
  filter(!is.na(drv) & !is.na(cty)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy= mean(cty))

# 3. kmeans를 이용하여 iris 데이터를 3개 그룹으로 나누어보세요

data(iris)

iris.x<-iris[1:4]
iris.x<-as.data.frame(lapply(iris.x,scale))
iris.x

set.seed(1234)
iris_clusters<-kmeans(iris.x,3) # 군집화
iris_clusters

#실제 값과 비교하기
iris_labels <-iris[5]

#<개수 비교>

table(iris_labels)
# setosa versicolor  virginica 
# 50         50         50

iris_clusters$size
# 50 53 47

#<정확도 비교>
iris_labels_1 <-ifelse(iris_labels=='setosa',1,ifelse(iris_labels=='versicolor',2,3))
sum(iris_clusters$cluster==iris_labels_1)/length(iris_labels_1) # 0.8333333


#4. snsdata의 결측값을 적절하게 대체하여 kmeans를 적용해보세요

#1. 데이터 확인
snsdata<-read.csv('snsdata.csv')

summary(snsdata)
library(Amelia)
missmap(snsdata[1:4],col = c('red','grey')) # age,gender NA 존재

sum(is.na(snsdata$age)) #5086
sum(is.na(snsdata$gender)) #2724
aggregate(data=teens,age~gradyear,mean,na.ra=T)

#나이 이상치 제거 & 결측값 채우기 (gradyear 이용)
sns.box<-boxplot(teens$age)
sns.box
# $stats
# [1,] 13.396
# [2,] 16.312
# [3,] 17.287
# [4,] 18.259
# [5,] 21.158

# 13.396 미만 , 21.158 초과하는 데이터 NA로 바꾸기
snsdata$age<-ifelse(snsdata$age>=13.396 & teens$age<21.158, teens$age,NA)


ave_age<-ave(snsdata$age,snsdata$gradyear,FUN=function(x) median(x,na.rm=T))
snsdata$age<-ifelse(is.na(snsdata$age),ave_age,snsdata$age) 

sum(is.na(snsdata$age)) #0



#성별 결측값 채우기 (유클리디안 거리 이용)


sum(is.na(snsdata$gender)) #2724
table(snsdata$gender)

#    F     M 
# 22054  5222 

colnames(snsdata)

snsdata$gender <-ifelse(snsdata$gender=='M',0,ifelse(snsdata$gender=='F',1,NA))
sns.scale<-as.data.frame(lapply(snsdata[,c(1,3,4)],scale))
sns.scale


na.index<- which(is.na(snsdata$gender))
na.index

for (i in na.index){
  e.dis<-sqrt(rowSums((t(t(sns.scale)-as.numeric(sns.scale[i,])))^2))
  top10.index<-order(e.dis)[1:10]
  snsdata$gender[i]<-round(mean(snsdata[top10.index,'gender'],na.rm=T))
}

#gender 결측값 처리 후 결과
sum(is.na(snsdata$gender))
table(snsdata$gender)
# 0     1 
# 5488 24512 

#female, male 컬럼 생성
library(dplyr)
snsdata<-snsdata %>% 
  mutate(female=ifelse(gender==1,1,0)) %>% 
  mutate(male=ifelse(gender==0,1,0))


#k-means clustering
interests<-snsdata[5:ncol(snsdata)]
interests_z<-as.data.frame(lapply(interests,scale))

#k 설정

#Elbow Method
sqrt(nrow(snsdata)/2) #122.4745


tot.withinss <-c()
betweens<-c()

for (i in seq(1,120)){
  tot.withinss[i]<-kmeans(interests_z,i)$tot.withinss
  betweens[i]<-kmeans(interests_z,i)$betweens
}

#withinss
plot(1:120, tot.withinss, type="b",xlab='k 개수')

#bewteens
plot(1:120, betweens, type="b",xlab='k 개수')


#실행 결과 그래프에서 elbow point를 파악하기 어려움 -> k 범위 줄이기

tw<-0
bt<-0
for (i in seq(1,25)){
  tw[i]<-kmeans(interests_z,i)$tot.withinss
  bt[i]<-kmeans(interests_z,i)$betweens
}

bt
tw

plot(1:25, tw, type="b",xlab='k 개수')
#plot(1:25, bt, type="b",xlab='k 개수')


#withinss값을 그래프로 그리기, 기울기가 완만해지는 3~4가 Elbow point라는 것을 알수 있다
# withinss 값으로 그래프를 그렸을때, 기울기가 완만해지는 구간 ->  k 개수:13~14, 또는 22~23
#(하지만 elbow point라고 봐도 되는지 잘 모르겠습니다)


# 범위 1~10
tw<-0
bt<-0
for (i in seq(1,10)){
  tw[i]<-kmeans(interests_z,i)$tot.withinss
  bt[i]<-kmeans(interests_z,i)$betweens
}

plot(1:10, tw, type="b",xlab='k 개수')

#범위를 10으로 줄였을때, 8-9 기울기가 가장 완만함 -> k=8~9

