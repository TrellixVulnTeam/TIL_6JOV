id<-c('a1','a2','a3')
name<-c('x','y','z')
price<-c(1000,2000,3000)
product<-data.frame(id,name,price)  #디폴트 stringAsFactors=FALSE
product
str(product)

product<-rbind(product,c('a4','s',4000))
product

new.rows<-data.frame(id=c('a5','a6'),
           name=c('i','j'),
           price=c(5000,6000)
           )
new.rows
#주의사항: 열 이름이 동일해야 함
product<-rbind(product,new.rows)
#다른 방법으로 열 추가
#product$madein<-c('kor','chi','chi','kor','kor','usa')

#cbind():새로운 열 추가
cbind(product,madein=c('kor','chi','chi','kor','kor','usa'))


#두 개 이상의 열을 추가하는 경우에는 데이터프레임으로 생성한 다음 수행
new.cols<-data.frame(menu=c('aa','bb','aa','cc','aa','bb'),
           quantity=c(10,20,30,20,10,25)
           )
new.cols

product<-cbind(product,new.cols)
product



df1<-data.frame(sex='f',month=1,weight=3.5)
df2<-data.frame(sex='m',month=3,weight=4.5)
df3<-data.frame(sex='m',month=4,weight=5.5)
df4<-data.frame(sex='f',month=7,weight=6.5)
df5<-data.frame(sex='f',month=8,weight=7.5)

lst<-list(df1,df2,df3,df4,df5)
lst

lst[1]
lst[[1]]

#첫번째 데이터 프레임
str(lst[[1]])

rbind(lst[[1]],lst[[2]])

lst
#rbind(lst[[1]],lst[[2]],,,...lst[[120]])

#do.call():리스트내의 여래 개 데이터 프레임을 합치는 작업

#do.call(적용함수, list)

do.call(rbind,lst)





#lst에 저장되어 있는 리스트들을 묶어서 하나의 데이터프레임으로 생성
lst1<-list(sex='f',month=1,weight=3.5)
lst2<-list(sex='m',month=3,weight=4.5)
lst3<-list(sex='m',month=4,weight=5.5)
lst4<-list(sex='f',month=7,weight=6.5)
lst5<-list(sex='f',month=8,weight=7.5)

lst<-list(lst1,lst2,lst3,lst4,lst5)
lst

#do.call(rbind,lst) ->2차원 배열
as.data.frame(lst[1])  #list->dataframe

#lapply():첫번쨰 인수에는 리스트의 원소, 두번째 인수에는 적용 함수(반복해서 적용하게 됨)

#lst에 저장되어 있는 각 원소에 대해 as.data.frame을 반복해서 적용해라
lapply(lst,as.data.frame) 

#lst(리스트)에 저장되어 있는 각각의 요소에 대해 as.data.frame함수를 적용하고, 
#변환된 데이터프레임들을 rbind함수를 모두 적용하여 하나의 데이터프레임으로 연결
do.call(rbind,lapply(lst,as.data.frame))

#merge():데이터프레임을 결합하는 함수
state.x77 #matrix-<dataframe

states<-data.frame(state.x77)
states
str(states)

states

row.names(states)
states

states$name<-row.names(states)
states

row.names(states)<-NULL
states
head(states) #가장 상단의 6개만 나옴
tail(states) #가장 하단의 6개
tail(states,10) #가장 하단의 10개


states
#states에서 income이 5000달러 이상에 해당되는 자료를 출력

states[states$Income>5000,'Income']
states[states$Income>5000,'name']

states[states$Income>5000,c('Income','name')]

#states에서 Area가 100000 이상에 해당되는 자료를 출력(name,area)
large.states<-states[states$Area>100000,c('name','Area')]
large.states
#조건에 해당되는 모든 열을 가져오고 싶을 때
rich.states<-states[states$Income>5000,c('Income','Area')]
rich.states
#데이터프레임결합(기본 값: 공통으로 열(name)이 일치하는 행만 선택)
#all옵션
merge(rich.states,large.states) #all=FALSE가 디폴트
merge(rich.states,large.states,all=TRUE)

#subset():행과 열을 선택
 
states[states$Income>5000,] 

#states집합에서Income>5000 조건을 만족하는 부분집합을 추출
subset(states,Income>5000)

subset(states,Income>5000 & Area>50000)  
#name이 알래스카인 모든 행을 추출
subset(states,name=='Alaska')  

subset(states,subset=(Income>5000 & Area>50000),select=Murder) 

subset(states,subset=(Income>5000 & Area>50000),select=c(Murder,Illiteracy)) 

mtcars

#mpg가 30보다 큰 자동차 데이터 출력

mtcars[mtcars$mpg>30,]

subset(mtcars,mpg>30)
#mps가 30보다 큰 자동차데이터(mpg)출력
subset(mtcars,subset=mpg>30,select=mpg)

#실린더(cyl)가 4개 이면서 am가 0인 자료의 mpf,hp,wt출력
subset(mtcars,subset=(cyl==4&am==0),select=c('mpg','hp','wt'))

subset(mtcars,subset=(mpg>mean(mpg)),select=c('mpg','hp','wt'))


subset(mtcars,mpg>mean(mpg),c('mpg','hp','wt'))

iris
class(iris)

subset(iris,select=c(Sepal.Width,Petal.Length))

subset(iris,select=-c(Sepal.Width,Petal.Length))

subset(iris,select=-Sepal.Width)

#iris Sepal.Length와 sepal.width간 비율
iris$Sepal.Length/iris$Sepal.Width
#특성공학(feature engineering): 주어진 데이터 컬럼으로부터 연산을 수행하여 새로운 연산을 수행한다

#with
with(iris,Sepal.Length/Sepal.Width)

#with(iris{
  #명령문 기술
#})

#기술통계
summary(iris$Sepal.Length)

#에러나옴
with(iris,{
  stats<-summary(Sepal.Length)
  stats
})

stats

#에러안나옴:with함수 안에서 사용한 변수를 함수 밖에서도 사용하고 싶으면 화살표 <<-이렇게 
with(iris,{
  stats<<-summary(Sepal.Length)
  stats
})

stats

iris$Sepal.Ratio<-iris$Sepal.Length/iris$Sepal.Width

iris<-within(iris,Sepal.Ratio<-Sepal.Length/Sepal.Width)
iris

#with,within은 거의 동일(코드의 양을 줄여줌)
#차이점은 within은 데이터 수정이 가능함, with는 불가
#예를들어
#sepal.ration가 na이면->중앙값으로 대체,
within(iris,{
  Sepal.Ration=ifelse(is.na(Sepal.Ratio),Median(Sepal.Ratio,na.rm=T),Sepal.Ratio)
})
#within(iris,{#조건 ,                    참                         거짓
#Sepal.Ration=ifelse(is.na(Sepal.Ratio),Median(Sepal.Ratio,na.rm=T),Sepal.Ratio)
#})





#sqldf 패키지:SQL 명령문을 사용할 수 있음
install.packages('sqldf') #패키지 설치
library(sqldf) #설치된 패키지를 프로그램에서 사용하기 위해 불러오기


#SQL(Structured Query Language):데이터베이스에 데이터를 검색(select)/수정(update)/삭제(delete)/추가(insert into) 작업
#수행할 수 있도록 해주는 사전에 약속된 데이터베이스 표준 질의어

mtcars

#mtcars에 저장되어 있는 모든(*) 데이터를 추출하시오.
#검색=select추출컬럼1,...,추출컬럼 n from 테이블

sqldf('select*from mtcars')


sqldf('select cyl from mtcars')


sqldf('select cyl,hp,gear from mtcars')

#행이름 출력

sqldf('select * from mtcars', row.names = TRUE)

sqldf('select * from mtcars where mpg>30', row.names = TRUE)

sqldf('select * from mtcars where mpg>30 order by hp', row.names = TRUE)


sqldf('select avg(mpg) as avg_mpg from mtcars where mpg>30 group by cyl', row.names = TRUE)


state.x77
class(state.x77)

st<-state.x77 #배열
#st를 데이프레임으로 바꾸세요
st<-data.frame(st)
colnames(st)
rownames(st)

colnames(st)
#차원?
dim(st) #50개, 변수(피처) 8개

#행단위로 합계
rowSums(st)
#행단위 평균
rowMeans(st)





library(MASS)
cats
