
df<-read.csv('train.csv',na.strings="")
str(df)

library(tidyverse)
view(df)

#기술통계량 함수가 포함된 패키지
install.packages('psych')
library(psych)

#결측맵 함수가 포함된 패키지
install.packages('Amelia')
library(Amelia)
missmap(df,col=c('red','grey'))


library(dplyr)
df<-select(df,Survived,Pclass,Age,Sex,SibSp,Parch)
missmap(df,col=c('red','grey'))

df<-na.omit(df)
missmap(df,col=c('red','grey'))

factor(df$Survived)
df$Pclass<-factor(df$Pclass,order=TRUE,levels=c(3,2,1))
df$Pclass

str(df)   


install.packages("ggplot2")
library(ggplot2)

install.packages("GGally")
library(GGally)


df<-read.csv('train.csv',na.strings="")

ggcorr(df,nbreaks = 8, label=TRUE,label_size = 3, color='grey50')









mtcars
str(mtcars)

#match함수를 이용한 데이터셋 결합
a=c(1,2,3,4,5)
b=c(2,4,7,8,9)
#첫번째 인수 a가 두 번째 인수의 몇번째 있는지 알려줌, 없는 경우 NA
match(a,b)
match(a,b,nomatch = 0)

car<-mtcars
row.names(car)
car$name<-row.names(car)
head(car)
row.names(car)<-NULL

head(car)

#145마력이 넘는 힘 쎈 자동차 모델로만 데이터프레임을 구성
highhp.car<-car[car$hp>145,]


#car에서무게가 3200파운드 미만
lightwt.car<-car[car$wt<3.2,]

#무게가 가벼우면서 힘이 쎈 자동차 모델을 출력하고자 함.
index<-match(highhp.car$name,lightwt.car$name)
lightwt.car[na.omit(index),]


#match함수 대신 %in% 연산자 사용 가능
vec<-10:1
vec
7 %in% vec
c(20,15,11,9,8,3,1,0) %in% vec

match(c(20,15,11,9,8,3,1,0),vec)

#두개 같음
!is.na(match(c(20,15,11,9,8,3,1,0),vec))
c(20,15,11,9,8,3,1,0) %in% vec

#%in%연산자를 이용하여 마력 높고 무게 낮은 차량 추출

idx<-highhp.car$name%in% lightwt.car$name
highhp.car[idx,]

#서브셋
#$:데이터로부터 하나의 원소를 추출, 데이터프레임에 적용하면 벡터로 나옴
#[[]]:데이터로부터 하나의 원소를 추출, 이름과 위치에 의해 원소를 선택 가능,
#리스트나 데이터프레임 모두 사용 가능
#[]:데이터로부터 여러 개의 원소를 추출

mtcars$mpg
str(mtcars)

mtcars[[1]]
mtcars[['mpg']]

mtcars[c(1,4)]
mtcars[c('mpg','hp')]

# 음수 인덱스를 사용하면 특정 원소를 제외한 서브셋 생성
mtcars[-c(2,3,5,7:11)]

mtcars[-1]

#특정 열 제거
mtcars[1]<-NULL
mtcars

#음수, 양수 인덱스를 섞어서 사용 못함
mtcars[c(-1,2)]



iris
str(iris)

data(iris)
str(iris)

#iris 1~4번 열 추출
iris[1:4]

iris[,c('Sepal.Length','Sepal.Width')]

#drop=FALSE로 하면 데이터 프레임
iris[,'Sepal.Length',drop=FALSE]
class(iris[,'Sepal.Length',drop=FALSE])



iris['Sepal.Length'] #데이터프레임

iris[,'Sepal.Length'] #벡터
 
iris[1:5] #1~5 열
iris[1:5,] #1~5행

iris[1:5,c('Sepal.Length','Sepal.Width')]


#퀴즈:'Sepal.Length'가 7초과한 데이터 전체를 추출

iris[iris$Sepal.Length>7,]
#iris[iris["Sepal.Length"]>7,c(특정열들)]


subset(iris,
       select = c('Sepal.Length','Sepal.Width'),
       subset=(Sepal.Length>7)
       )

#데이터 무작위 표본 추출
#sample함수 
#sample(데이터,표본 개수, 복원추출여부)

#1~10수 중에서 5개 숫자를 비복원 추출
sample(1:10,5) #기본 값 replace=FALSE(비복원 추출)
sample(1:10,5,replace = TRUE)

sample(1:10) #10개가 랜덤하게 비복원 추출

iris


#데이터->모델->예측/분류

#모델링? 데이터를 훈련용/테스트용으로 분할

#모델링 과정?
#1)데이터를 훈련용(70%)/테스트용(30%)으로 분할
#2)오직 훈련용 데이터만으로 모델(예측/분류)을 생성
#-과적합(overfitting):훈련 데이터로 평가 결과>>테스트 데이터 평가 평가
#-원인: 데이터가 부족->보충, 변수가 너무 많음(고차원)->차원축소(저차원),...



#sample함수로 동일한 난수가 발생
#시드(seed)값을 동일하게 주면, 매번 발생되는 난수가 동일하게 추출
#set.seed:기드값 설정

set.seed(20210303)
sample(1:10)

#데이터->일부를 추출하여 모델 생성
#ex)데이터가 1~10번까지 10개
#전처리->랜덤:1245679번 추출(훈련데이터)->모델->평가(2,4,9)


set.seed(1)
sample(1:10,5,replace=TRUE)

#데이터프레임으로부터 무작위 추출

sample(iris,3)

#데이터프레임 행으로부터 표본 추출(행번호가 나옴)
set.seed(1)
index<-sample(1:nrow(iris), 5)
iris[index,]



#일반적으로 중복값은 제거
#duplicated():중복 여부를 논리값으로 출력
duplicated(c(1,2,3,1,1,4,3))


id<-c('a001','a002','a003')
name<-c('mouse','keyboard','usb')
price<-c(3000,9000,5000)
product<-data.frame(id=id,name=name,price=price)
product

#c('a001','mouse',3000) 추가
product<-rbind(product,c('a001','mouse',3000))

duplicated(product)

#중복이 아닌 것들만 추출
product[!duplicated(product),]

product.unique<-product[!duplicated(product),]
#which(true에 해당되는 데이터의 index추출),duplicated 중복된 원소 위치 파악

which(duplicated(product))

#중복행을 제거
idx<-which(duplicated(product))
product.unique<-product[-idx,]
product.unique


#중복 원소 파악하지 않고, 제거만 수행
product
unique(product)


#complete.cases함수:결측값 제거(na.omit과 비슷), 결측값 여부를 TRUE,FALSE로 출력(FALSE가 결측값)
airquality
str(airquality)
#결측값이 없는 행만 추출(complete.cases수행 결과 true)
airquality[complete.cases(airquality),]

#결측값이 있는 행만 추출
airquality[!complete.cases(airquality),]

airquality.nona<-airquality[!complete.cases(airquality),]
str(airquality.nona)




airquality.nona2<-na.omit(airquality)
airquality.nona2



#cut함수:데이터를 구간에 따라 그룹별로 볌주화
#():개구간, []:폐구간
#(3,10): 범위가 3초과 10미만
#(3,10]:범위가 3초과, 10이하


iris$Sepal.Width
min(iris$Sepal.Width)
max(iris$Sepal.Width)

cut(x=iris$Sepal.Width, breaks=c(0,1,2,3,4,5))
#왼쪽이 개구간, 오른쪽이 폐구간
#(0,1] :0<x<=1
cut(x=iris$Sepal.Width, breaks=c(0,1,2,3,4,5),right=FALSE)  #right=TRUE가 기본값


#table함수,summary함수와 함께 사용

iris.cut1<-cut(x=iris$Sepal.Width, breaks=c(0,1,2,3,4,5))
table(iris.cut1)
summary(iris.cut1)


#더 이해하기 쉽고 눈에 잘 들어오게 label설정
iris.cut2<-cut(x=iris$Sepal.Width, 
    breaks=c(0,1,2,3,4,5),
    labels=c('Smaller','Small','Medium','Big','Bigger')
    )


table(iris.cut2)
summary(iris.cut2)

#구간을 자동으로 분리(break에서 최소,최대 일일이 지정하는 것 대신)
#include.lowest=TRUE:최소값에 해당하는 부분을(2)포함하고 싶다면 적용
cut(x=iris$Sepal.Width, breaks=5,include.lowest=FALSE) 






iris.cut3<-cut(x=iris$Sepal.Width, 
               breaks=c(0,1,2,3,4,5),
               labels=c('Smaller','Small','Medium','Big','Bigger'),
               include.lowest = TRUE  #include.lowest=TRUE는 최소값을 
)
iris.cut3


#정렬
x<-c(3,7,5,1,2,5)
sort(x)
sort(x,decreasing = TRUE)

length(x)<-7
x

sort(x)  #NA값 포함 안됨
sort(x,na.last=TRUE) #na가 맨뒤에 포함
sort(x,na.last=FALSE)#na가 앞에 포함

y<-c(11,22,33,55,44)
order(y)
y[order(y)]

y<-c(11,22,33,55,44)
z<-c('ss','bb','ii','aa','pp')
df<-data.frame(y,z)
df

#y열을 기준으로 오름차순 정렬
df[order(df$y),]

#y열을 기준으로 내림차순
df[order(df$y,decreasing = TRUE),]


w<-c('c','c','n','n','n')
df<-data.frame(y,z,w)
df

#w열 1차 기준, y열 2차 기준

df[order(df$w,df$y),]
df[order(df$z,df$y),]


#xtfrm():동일하지 않은 정렬 방법을 적용

xtfrm(df$w)  #숫자 벡터로 변환

#w열을 기준으로 내림차순,y열을 기준으로 오름차순
index<-order(-xtfrm(df$w),df$y)
df[index,]

#퀴즈3
#iris의 종(species)별로 내림차순 정렬, sepal.length기준으로 오름차순 정렬

iris[order(-xtfrm(iris$Species), iris$Sepal.Length),]


####
midwest<-as.data.frame(ggplot2::midwest
