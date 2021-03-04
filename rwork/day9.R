iris.copy<-iris
class(iris.copy$Species)
#character타입으로 변경
class(as.character(iris.copy$Species))


iris.copy$Sepal.Ration<-iris.copy$Sepal.Length/iris.copy$Sepal.Width
head(iris.copy)


#파생변수 추가 
#transform함수: 변수(피처)를 변환
#iris열에 sepalraion가 추가되고 species는 캐릭터로 변환
iris.copy<-iris
iris.trans<-transform(iris.copy,
          Species=as.character(Species), #iris.copy$Species대신 이렇게 써도 됨,
          sepalRation=Sepal.Length/Sepal.Width
          )  

iris.trans


#apply family: apply(),lapply(),sapply()
#데이터에 특정 함수를 적용하는 함수

#apply():적용하고자 하는 데이터가 행렬 or 배열일 때 사용 가능
#결과타입: 벡터, 행렬(vector, matrix)

#lapply(),sapply:데이터가 리스트 or 벡터일 때 사용
#인수가 2개, 첫번째 인수에는 데이터, 두번째 인수에는 함수 
#lapply함수 결과:항상 리스트 형식으로 반환
#sapply함수 결과: 벡터 또는 행렬로 단순화 해서 반환 #simplify
#벡터는 길이가 1,행렬은 길이가 2이상 이면서 모두 같은 경우
#길이가 2이상이면서 서로 다른경우에는 리스트로 출력




x<-1:20
dim(x)<-c(4,5)
apply(x,1,max)

x<-1:24
dim(x)<-c(4,3,2)
x

class(apply(x,1,paste,collapse=","))  #1:행, 2:열, 3: 3번째 차원(으로 paste가 되어짐)
apply(x,2,paste,collapse=",")
apply(x,3,paste,collapse=",")


apply(x,c(1,2),paste,collapse=",")  #행과 열이 교차하는 원소로 구성됨


#타이타닉
str(Titanic)

#등급별 탑승 인원을 파악
apply(Titanic, 1, sum)

#성별(두번 째 차원)탑승 인원을 파악
apply(Titanic, 2, sum)

#생존자별(네 번째 차원)탑승 인원을 파악
apply(Titanic, 4, sum)

#승객 등급별 생존자 통계를 알고싶다면?
apply(Titanic,c(1,4),sum)



#lapply(),sapply:데이터가 리스트 or 벡터일 때 사용
#인수가 2개, 첫번째 인수에는 데이터, 두번째 인수에는 함수 
#lapply함수 결과:항상 리스트 형식으로 반환
#sapply함수 결과: 벡터 또는 행렬로 단순화 해서 반환 #simplify
#벡터는 길이가 1,행렬은 길이가 2이상 이면서 모두 같은 경우
#길이가 2이상이면서 서로 다른경우에는 리스트로 출력
exams<-list(s1=c(80,70,60,50,100),
     s2=c(80,40,60,50),
     s3=c(30,70,60,50,100,90),
     s4=c(80,60,60,50,100)
     )

exams
lapply(exams,length)  #출력 결과가 리스트로 나옴, 길이가 모두 1
sapply(exams,length)  #길이가 1이기 때문에 벡터로 반환

lapply(exams,mean)
sapply(exams,mean)

lapply(exams,sd)
sapply(exams,sd)

sapply(exams,range)  #길이가 2로 모두 동일함(따라서 출력 결과가 행렬로 나옴)

# s4=c(80,60,60,50,100)
# range(s4) #최대, 최소값을 갖는 벡터가 반환

#lapply,sapply는 데이터프레임에 대해 사용가능
str(iris)
lapply(iris,class)

#sapply(iris,mean) #에러 남
#따라서 sapply(iris,사용자함수)
sapply(iris,function(x) ifelse(is.numeric(x),mean(x),NA))



#mapply():적용하고자 하는 함수가 벡터연산을 지원하지 않을 때 유용하게 사용 가능
mapply(rep,1:4,4:1)
#list(rep(1,4),rep(2,3),rep(3,2),rep(4,1))

#집단 요약(그룹을 기준으로 요약)
#벡터를 집단별로 분할(split,unstack)
car<-mtcars
car<-within(car,
       am<-factor(am,
              levels=c(0,1),
              labels=c('Automatic','Manual'))
       )

str(car)


car
#mpg를 변속기 종류(2가지)에 따라 분할
g<-split(car$mpg, car$am)
class(g)
#집단별 mpg평균

mean(g[[1]])

mean(g[['Manual']])

sapply(g,mean)


#split과 유사한 unstack함수
data.frame(car$mpg,car$am)
unstack(data.frame(car$mpg,car$am))
#Species를 기준으로 iris$Sepal.Length를 분류
gg<-unstack(data.frame(iris$Sepal.Length,iris$Species))
str(gg)


#unstack함수는 그룹별로 분할된 데이터의 길이가 동일하면 데이터프레임, 동일하지 않으면 리스트로 출력
g1<-unstack(data.frame(car$mpg,car$am))  #리스트

g2<-unstack(data.frame(iris$Sepal.Length,iris$Species))  #데이터프레임

#summary함수는 데이터프레임에 대해 기술통계를 구해주는 함수
summary(g1) #summary안나옴
summary(g2) #summary나옴


#그룹 분할 작업->그룹별 연산 작업을 동시에 진행하겠다면...
#tapply(),aggregate(),by()함수를 사용


#tapply(데이터 벡터, 그룹 팩터, 그룹별 연산 함수):3개 인수

tapply(iris$Sepal.Length,iris$Species,mean)


#종별 꽃 데이터의 개수를 출력
tapply(iris$Sepal.Length,iris$Species,length)
str(iris)

str(car)
#실린더(cyl)개수별 am 유형별 조합에 따른 mpg평균
#      a    m
#  4
#  6
#  8
with(car,tapply(mpg, list(cyl,am), mean))

#aggregate(집계함수): 그룹별로 각각 함수를 적용 
aggregate(벡터, 리스트 형식으로 집단 변수, 함수)

with(car,aggregate(mpg, list(Cylinder=cyl,Transmission=am),mean))


#car[c(1:6)] 변수의 평균, 실린더 개수와 변속기 유형의 조합에 따라...
aggregate(car[c(1:6)],list(car$cyl,car$am),mean)

#아이리스 꽃 종류별 측정 변수별 요약
str(iris)

aggregate(iris[c(1:4)],list(iris$Species),mean)




#by함수: 데이터프레임을 그룹별 데이터를 처리
by(iris, iris$Species, summary)

by(iris,iris$Species, function(x) mean(x$Sepal.Length))


rowsum(iris[-5], iris$Species)


#번주별 관측값 개수(범주별 개수가 몇개 있는지)
gc<-tabulate(car$gear)
names(gc)<-1:length(tabulate(car$gear))
gc


table(car$gear)


#xtabs함수: table함수와 동일한 기능 수행, 포뮬러 사용
#~기준으로 오른쪽에 있는 것 기준으로 왼쪽을 출력하겠다
xtabs(~am, car)
xtabs(~am+gear,car)

#포뮬러? 데이터 처리시 어떤 열을 사용할 것인지를 나타낸 수식

#포뮬러: mpg~cyl+am
#cyl와 am 유형별 mpg열의 평균을 구하시오.
aggregate(mpg~cyl+am,car, mean)

#같은 구문임
with(car, aggregate(mpg,list(cyl,am),mean))

#dplyr:분할(s)-적용(A)-결합(c)작업을 수월하게 할 수 있도록 도움을 주는 라이브러리 

#filter 조건을 만족하는 행 추출
air<-filter(airquality,Month==6)
head(air)

airquality[airquality$Month==6,]
subset(airquality, subset=(Month==6))


air<-filter(airquality, Month==6,Temp>90)  #,는 and연산
air<-filter(airquality, Month==6&Temp>90)

air<-filter(airquality, Ozone>80 | Temp>90)
