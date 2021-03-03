#스크립트 : 야드->미터로 변환하는 명령어 집합
#translength.R에 저장된 스크립트 내용은 아래와 같음
# x<-c(30,50,50)
# tlength<-round(x*0.9144,1)
# tlength
# result<-paste(tlength,'m',sep='')
# print(result)



#source함수:day7에서 translength.R을 실행하고자 함
source('translength.R')


#transLength함수를 정의->메모리에 적재
transLength<-function(x){
tlength<-round(x*0.9144,1)
result<-paste(tlength,'m',sep='')
return(result)
}

#ls()  #메모리에 적재된 변수, 함수 등의 이름이 목록으로 출력

transLength(10)
y<-c(100,150,200)
transLength(y)

trans2<-transLength
trans2(y)

trans2

f1<-function(x,y){x+y}
f1(1,3)

#함수에서 실행할 문장이 1개인 경우네는 중괄호 생략이 가능
f2<-function(x,y) x+y
f2(2,5)


tran3<-function(x){
if(!is.numeric(x)){
  return('not a number')
}   #!는 not 연산자
tlength<-round(x*0.9144,1)
result<-paste(tlength,'m',sep='')
return(result)
}

#tran3(10)
tran3('abc')

is.numeric('3')




#퀴즈
#피트(feet),인치(inch) 변환이 가능한 함수
#1야드=3피트, 1야드 =36인치
y<-c(100,150,200)


transLength<-function(x,mult=0.9144,unit="m"){
  tlength<-round(x*mult,digits=1)
  result<-paste(tlength,unit,sep='')
  return(result)
}


y<-c(100,150,200)
transLength(y,mult=3,unit='ft')
transLength(y,mult=36,unit='in')
transLength(y)

transLength(x=y,mult=3,unit="ft")
transLength(x,3,"ft")




#함수 안에 사용된 인수를 사용하고 싶으면
transLength<-function(x,mult=0.9144,unit="m",...){
  tlength<-round(x*mult,...)
  result<-paste(tlength,unit,sep='')
  return(result)
}
#...이 digit=3으로 치환됨
y<-c(100,150,200)
transLength(y,digits=3)

transLength(y)  #round(x*mult,...)  =>round(x*mult)



#
transLength<-function(x,mult=0.9144,unit="m",d=1){
  tlength<-round(x*mult,digits=d)
  paste(tlength,unit,sep='')
}

y<-c(100,150,200)
transLength(y)

#함수 자체를 인수처럼 취급할 수 있음
transLength<-function(x,mult=0.9144,unit="m",FUN=round,...){
  tlength<-FUN(x*mult,...)
  paste(tlength,unit,sep='')
}
y<-c(100,150,200)
transLength(y)


#floor->원데이터의 가까운 정수로 출력
transLength(y,FUN=floor)

transLength(y,FUN=signif, digits=3)

x<-pi
y<-3
if(x>y)x
if(x>y){
  print(x)
}


if(x<y)x else y

#조건문에 백터가 들어갈 수 없음(여러개 있다면 첫번째 원소만 취급됨)
x<-pi
y<-1:5
if(x<y)x else y



#조건문에 벡터를 포함하고자 한다면 iflese()함수 사용
#ifelse(조건, 참, 거짓)

t<-c(TRUE,FALSE,TRUE,FALSE,TRUE)
y<-1:5
n<-0
ifelse(t,y,n)

#ifelse함수는 벡터연산이 가능
x<-pi
y<-1:5
ifelse(x>y,x,y)

#mean:평균 median:중앙값

#switch함수: 첫번째 인수로 주어진 값에 따라 두번째 이후의 인수에 
#지정된 코드가 실행됨


center<-function(x,type){
  switch(type,
         mean=mean(x),
         median=median(x),
         trimmed=mean(x,trim=0.1),  #10% 절삭평균
         "choose one of mean, median, and trimmed"
         )
  
}

x<-c(2,3,5,7,11,13,17)
center(x,'mean')
center(x,'median')
center(x,'trimmed')  #절삭평균
#절삭평균: 산술평균(mean)이 outlier(이상치)에 민감하게 반응하는
#것을 보정해서 평균을 낸 것.


center(x,'other')


#
i<-5
repeat{if(i>25)break
  else{
    print(i)
    i<-i+5
  }
  }

i<-5
while(i<=25){
  print(i)
  i<-i+5
}

for(i in seq(from=5,to=25,by=5))
  print(i)

#for(변수 in 리스트) 반복명령문

#반복문 작성시 참고사항
#1)실행 결과는 루프 안에서는 출력되지 않는다->명시적으로 
#print함수를 호출해야만 출력이 됨
#for(i in seq(from=5,to=25,by=5)) i
for(i in seq(from=5,to=25,by=5)) print(i)

#2) for문이 종료된 이후에도 변수는 사라지지 않는다 
i<-1
for(i in seq(from=5, to=25,by=5)) i 
print(i) #가장 마지막에 i에 할당된 25가 저장되어 있음


#데이터 전처리:분석 목적에 적합한 형태
#수집되어 전처리 되어야 할 대상 데이터를 r에서 어떤 자료구조로 표현?
#자료구조:벡터(하나의 차원),
#행렬(배열),리스트, 데이터프레임 등은 두개 이상의 차원을 갖는 자료의 경우
#행렬/배열은 동일한 데이터 유형으로 구성

#데이터프레임은,리스트는 숫자, 문자가 섞여 있는 데이터 유형으로 구성

#mode:데이터 유형(숫자, 문자, 논리, 리스트, 함수)...
mode(3.14)
mode(c(3.14,1.5))
mode('Batman')
mode(c('Batman','Superman','Somun'))
mode(factor('High','Med','Low'))
mode('2021-03-02')
mode(as.Date('2021-03-02'))
mode(5>2)
mode(list(1.2,'apple',c(3,4)))

mode(mean)

d<-as.Date('2021-03-02')
d+1

as.integer(d)  #단위:일, 1970.1.1일을 기준으로 현재까지 경과한 날
length(d)

#타입을 바꾸고 싶을 때 as.-
as.numeric(1.618)
as.integer(1.618)
as.character(1.618)

as.numeric('test')  #변환이 불가능한 경우에는 NA가 출력

mode(as.numeric('1.234'))

as.numeric(c('-1','1.5','3.14'))

as.numeric(c('-1','1.5','3.14','test'))

mode(10:20)
as.numeric(as.character(10:20))

as.numeric(TRUE)
as.numeric(FALSE)

sum(c(TRUE,FALSE,TRUE))


#c(1,3,5,7,9) #벡터에서 4보다 큰 수는 총 몇개인가?
#중요!!!!!!
sum(c(1,3,5,7,9)>4)


#리스트->분석 모델에서 요구하는 타입이 데이터프레임이라면 =>타입변환

as.data.frame(x)
as.list(x)
#r에서는 as.변환하고자하는타입()를 이용하여 데이터 변환

#데이터 타입 확인할 때
is.data.frame(x)
is.factor(x)
is.vector(x)

#벡터에서 다른 타입으로 변환
vec<-1:6
vec

#벡터의 각 원소가 리스트으 ㅣ원소로 변환
as.list(vec)
#벡터 전체가 하나의 원소를 갖는 리스트로 변환
list(vec)


#벡터를 행렬로 변환:cbind(),as.matrix(),rbind()
vec<-1:6
vec

cbind(vec)
as.matrix(vec)
rbind(vec)

matrix(vec,2,3)

#벡터를 하나의 열로 구성된 데이터 프레임으로 변환
as.data.frame(vec)

#벡터를 하나의 행으로 구성된 데이터프레임으로 변환

as.data.frame(rbind(vec))

rbind(vec) #vector->matrix->df


#행렬구조를 벡터, 리스트, 데이터프레임으로 변환
#as.vector(),as.list(),as.data.frame()

#3행 2열(1~6값이 저장됨) 행렬=> 벡터, 리스트,데이터프레임으로 변환
mat<-matrix(1:6,3,2)
as.vector(mat)
as.list(mat)
as.data.frame(mat)


#리스트->다른 구조
#unlist함수: 리스트->벡터

lst<-list(odd=c(1,3,5),even=c(2,4,6))
lst

unlist(lst)
#as.vector함수로 작성해도 아무 변화 없음(unlist를 써야됨)
as.vector(lst)

identical(lst,as.vector(lst))  #TRUE

lst2<-list(odd=c(1,3,5),even=c('two','four','six'))
lst2

unlist(lst2)


#리스트->행렬: unlist(벡터)->행렬
lst<-list(odd=c(1,3,5),even=c(2,4,6))
lstvec<-unlist(lst)
matrix(lstvec,3,2)


#dimnames인수:리스트의 원소 이름을 행렬의 행 또는 열 이름으로 사용
matrix(unlist(lst),3,2,dimnames = list(NULL,names(lst)) )

#주의사항: 리스트에 matrix함수, as.matrix를 그대로 적용하면 행렬로 변환 안됨
#오류
matrix(lst)
as.matrix(lst)

#as.data.frame():리스트->데이터프레임으로 변환
#숫자와 문자가 섞여 있으면, 숫자->숫자벡터로, 문자->문자벡터로 변환됨
lst<-list(odd=c(1,3,5),even=c(2,4,6))
lstdf<-as.data.frame(lst)
str(lstdf)

lst2<-list(odd=c(1,3,5),even=c('two','four','six'))
lstdf2<-as.data.frame(lst2)
str(lstdf2)

#데이터프레임-다른 구조로 변환
#데이터프레임 인덱싱:열로부터 벡터를 생성
#데이터프레임 행->데이터프레임으로 출력

df1<-data.frame(odd=c(1,3,5),even=c(2,4,6))
df1
df1[1,]

str(df1[1,])  #행은 데이터프레임!!!

df1[,1]

str(df1[,1])  #열은 벡터!!!

str(df1[1])  #컴마 없이 주면 열->데이터프레임으로 추출
str(df1[2])


df1[[1]]  #벡터


#데이터프레임이 하나의 행 또는 열로 구성된 경우에만 가능:데이터프레임 전체를 벡터로 변환
#데이터프레임->행렬->as.vector사용하여 벡터로 변환

df2<-data.frame(odd=c(1,3,5),even=c(2,4,6))
df2

#as.vector(df2) 아무 변화 없이 그대로 출력

#1)데이터프레임->행렬
as.matrix(df2)

#2)행렬->as.vector
as.vector(as.matrix(df2))





df3<-data.frame(odd=c(1,3,5),even=c('two','four','six'))
df3

as.matrix(df3)  #메트릭스는 타입이 모두 동일해야하니 타입이 동일해짐
as.vector(as.matrix(df3))



#as.list():데이터프레임->리스트
#숫자->숫자벡터, 문자->문자(이전 버전에서는 팩터)로 변환

df4<-data.frame(odd=c(1,3,5),even=c(2,4,6))
as.list(df4)
str(as.list(df4))




df5<-data.frame(odd=c(1,3,5),even=c('two','four','six'))
as.list(df5)
str(as.list(df5))
#이전버전까지는 levels:four six two와 같이 팩터로 변환됨
#그러나 지금 버전은 문자 벡터로 출력됨



#as.matrix():데이터프레임->행렬
#주의사항:데이터 프레임이 모두 솟자로 구성->숫자행렬, 모두 문자로 구성-<문자행렬
#문자/숫자가 섞여서 구성-모두 문자로 변환된 행렬

df5<-data.frame(odd=c(1,3,5),even=c(2,4,6))
as.matrix(df5)


df6<-data.frame(odd=c(1,3,5),even=c('two','four','six'))
as.matrix(df6)
          