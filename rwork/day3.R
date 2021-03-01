#배열? 행렬의 일반화된 데이터 형식, 차원을 속성으로 갖는 벡터
#벡터(1차원),행렬(2차원) 모두 배열이라고 할 수 있음
#dim함수로 배열 생성

a<-1:24
dim(a)<-c(3,4,2)  #a의 차원에 대한 크기를 지정 (3차원, 2개의 면(테이블),3행4열)
a

#두번째 방법
#array 함수: 다차원 배열 생성

ary<-array(1:24,c(3,4,2))
ary[1,3,2]   #2번째 면에 있는 1행 3열

ary[1,,]
ary
ary[,1,]
ary[,,2]

#ary배열의 2번째 면에 있는 1번 열의 값을 추출
ary[,1,2]
#이렇게 하면 벡터로 출력되는데 이걸 2차원 구조로 출력 시키고 싶을 때
ary[,1,2,drop=FALSE]

#리스트
#벡터와 행렬은 원소의 데이터 타입이 모두 같아야 함

lst<-list(0.6,0.9,0.5)
lst

#[[1]]은 원소의 위치(인덱스)를 의미
#[1] 0.6은 원소의 값
#리스트에는 스칼라, 벡터(숫자,문자),행렬, 함수 저장 가능

lst<-list(1.5,'apple',c(2,3,4),matrix(1:6,ncol=3),mean)
lst

lst<-list()
lst
lst[[1]]<-1.5
lst[[2]]<-'apple'
lst[[3]]<-c(2,3,4)
lst[[1]]<-matrix(1:6,ncol=3)
lst[[5]]<-mean
lst

#각각의 원소들에게 이름을 주는 방법
lst<-list(0.6,0.9,0.5)
lst
names(lst)<-c('n1','n2','n3')
lst
#이름을 주면[[1]] 형식이 $이름으로 변경됨

#이름 참조할 때
lst$n1

#lst에 지정되어져 있는 이름을 알고싶을 때
lst
names(lst)
#원소의 개수
length(lst)

#lst[[n]]:lst리스트의 n번째 원소가 선택, 원소의 저장 형식을 그대로 가지고 출력

#lst[n]:lst리스트의 n번째 원소가 선택,원소가 리스트 형식으로 출력

product<-list('a001','mouse',30000)
product 
product[[3]]  #30000,벡터 형식 그대로 출력됨
product[3] #리스트 형식으로 출력

#타입 확인
class(product[[3]]) #숫자 벡터
class(product[3]) #리스트

product[[3]]*0.9
#product[3]*0.9  에러 발생

product
product[1]
product[2]

product[c(1,2)]


#불린 참조
product[c(TRUE,FALSE,TRUE)]
#첫번째,세번째원소가가 참조되어지고 두번째원소를 참소 안됨


#특정 원소 제외하고 참조 할 때
product[-1]

#각각의 원소에 이름 지정하고 리스트 만듦
product<-list(id='a001',name='mouse',price=30000)
product

#특정 이름의 값을 추출하는 두가지 방법
product$id

product[['name']]

#이름을 활용해 2개 이상의 원소 참조, 출력 결과는 리스틀 나옴
product[c('name','price')]

#없는 이름으로 접근하면 
#product[['nn']] NULL이 나옴
#
#product[[4]] 에러 발생


#리스트 안에 리스트를 표현하는 구조
lst<-list(one=1,two=2,three=list(a=3.1,b=3.2))
lst[['three']]
lst$three
#3번째 원소를 추출, 추출 결과 또한 리스트

#리스트 안에 리스트를 참조(이름을 활용해)
lst$three$a
lst[['three']][['a']] #벡터
lst[['three']]['a'] #리스트로 출력

#리스트 조작: [[]],$기호로 사용하여 요소 접근

product<-list(id='a001',name='mouse',price=30000)

product[[3]]<-50000
product
product[['price']]<-50000
product
product$price<-50000
product

#값을 1개 할당할때는 [[]],[]모두 가능
product[3]<-50000

product

procut['price']<-50000
product


#하나의 원소에 여러 개의 값을 할당할때는 [[]],[]는 다름
product<-list(id='a001',name='mouse',price=30000)
#[[]]는 할당 데이터가 벡터 형식
#[]는 할당하고자 하는 값을 리스트 형식으로 변환해야 함

product[[3]]<-c(40000,50000)
product

#product[3]<-c(20000,30000) #dp에러 발생
#[]는 할당하고자 하는 값을 리스트 형식으로 변환해야 함
product[3]<-list(c(20000,30000))
product

#두 개 이상의 원소 값들을 동시 변경할 때는 []를 사용

product[1:3]<-list('a02','monitor',99999)
product


product[[3]]

product[[4]]<-c('domestic','export')
product

product$madein<-c('korea','india')
product

product[['madein2']]<-c('usa','china')
product

#product['madein3']<-c('usa2','china2') #할당할 값을 리스트로 변경해야함

product['madein3']<-list(c('usa2','china2'))
product

length(product)

#리스트에 여러개 원소를 한번에 추가(리스트 구조,추가하고자하는 데이터 타입이 모두 같은 경우에는 벡터 구조도 가능)
product[8:10]<-list(0.1,0.2,0.3)
product

product[8:10]<-list(0.1,0.2,'0.3')
product

#타입이 같은 경우 벡터로도 저장 가능
product[11:13]<-c(0.1,0.2,0.3)
product
#타입이 다른 경우 벡터로 저장할 경우 형변환이 이루저진 후 저장 됨
product[11:13]<-c(0.1,0.2,'0.3')
product

product[11:13]<-list(0.1,0.2,'0.3')
product

n<-c('one','two','three')
v<-c(100,200,300)
mylist<-list()
#한꺼번에 저장됨
mylist[n]<-v
mylist

#리스트에서 원소 제거는 NULL을 할당
mylist [['two']]<-NULL
mylist

#두개 이상 제거할 때
mylist[c('one','three')]<-NULL
mylist

n<-c('one','two','three')
v<-c(100,200,300)
mylist<-list()
#한꺼번에 저장됨
mylist[n]<-v
mylist

#조건에 따른 원소 제거
mylist
mylist[mylist<200]<-NULL
mylist

#리스트 결합(벡터의결합과 같음)
w1<-list('a','b','c')
w2<-list('d','e','f')

c(w1,w2)

#r의 수치연산 관련 함수 대부분은 벡터 자료구조를 사용
mydata<-list(1.5,2.0,3.5,4.5)
#mean(mydata) 에러나옴(리스트라서)

#만약 리스트로 저장된 데이터를 연산하려면, 벡터로 변환
#unlist함수: 리스트->벡터

mean(unlist(mydata))
max(unlist(mydata))






#데이터프레임:행과 열로 구성, 2차원 구조
#행렬은 모든 데이터 타입이 일치해야함
#데이터 프레임은 서로 다른 데이터 타입을 가질 수 있음(리스트와 같음)
#데이터 프레임은 2차원 구조, 리스트는 1차원구조

#데이터프레임은 동일한 길이의 벡터로 이루어진 리스트를 구성요소로 하는 2차원 데이터구조

#data.frame()함수를 이용하여 벡터로부터 데이터프레임을 생성
v1<-c('a1','a2','a3')
v2<-c(10,20,30)
v3<-c('x','y')
data.frame(v1,v2)
#data.frame(v1,v2,v3) 에러 나옴(길이 달라서)

v3<-c('x','y','z')
df<-data.frame(v1,v2,v3)
str(df)
#obs->obsevations의 약자
#3 variables

#   x1 x2 ... x10000
#0  0  20 ...  255
#   0  20 ...  255
#   0  20 ...  255
#   ...
#99  0  20 ...  255

#100(obs,instance,object)장의 이미지
#각 이미지 데이터의 차원은?10000차원, feature가 1000개 있음
#각각의 이미지가 10000차원 공간의 (0,20,...255)위치에 점으로 표시가 됨
#유클리디안 거리 또는 코사인 유사도 등의 알고리즘 기반 거리 계산을 통해
#유사한 데이터를 찾아낼 수 있음


str(df)

data.frame(row.names=v1,v2,v3)

p<-data.frame(id=v1,name=v2, price=v3)
p
str(p)


v1<-c('a1','a2','a3')
v2<-c(10,20,30)
v3<-c('x','y','z')
p<-data.frame(id=v1,price=v2,name=v3)
p
str(p)

#stringsAsFactors #벡터->데이터프레임 생성할때 데이터타입을 팩터로 지정
#(factor형태로서 string(문자열)을 읽겠습니까?)
stringAsFactors=FALSE #팩터로 문자열을 읽지 않겠다. 즉 문자열로 읽겠다
stringAsFactors=TRUE #팩터로 문자열을 읽겠다. 즉 문자열을 팩터로 읽겠다

p<-data.frame(id=v1, price=v2, name=v3, stringAsFactors=TRUE)
str(p)

#as.data.frame 함수: 행렬, 리스트로부터 데이터브레임 생성

mat<-matrix(c(1,2,3,4,5,6),ncol=2)
mat
length(mat)
#행렬->데이터프레임



num<-as.data.frame(mat)
num

colnames(num)  #행렬의 열 이름 출력
colnames(num)<-c('d1','d2')
num







v1<-c('a1','a2','a3')
v2<-c(10,20,30)
v3<-c('x','y','z')
lst<-list(v1,v2,v3)

p<-as.data.frame(lst)

colnames(p)<-c('id','name','price')
p

#length함수:행렬에서 전체 원소의 개수,데이터프레임에서는 열의 개수
#열의 개수 구하는 함수
length(p)

ncol(p)
#행의 개수 구하는 함수
nrow(p)


#datasets:r설치시 기본적으로 내장되어 있는 데이터셋

str(state.abb)
str(state.name)
str(state.region)
str(state.area) #평방마일

us.state<-data.frame(state.abb,state.name,state.region,state.area)
us.state

str(us.state)

#1>>>str(us.state) 열 추출

#[[]]or [] 사용하여 열 추출
#[[]]:열 하나를 벡터, or 팩터로 출력
#[]:데이터프레임이 추출, 하나 또는 여러 개의 열을 추출

#데이터프레임에서 특정 열을 추출할 때 [[]] 면 벡터로 추출됨
us.state[[2]]
str(us.state[[2]])

#데이터프레임에서 특정 열을 추출할 때 [] 면 데이터 프레임으로로 추출됨
us.state[2]
str(us.state[2])

#여러 열을 추출할 때는 데이터 프레임으로 추출됨
us.state[c(2,3)]


#2>>>행렬 인덱싱 사용 가능
us.state

us.state[,2]
us.state[,2,drop=FALSE] 
#행렬에서는 drop=FALSE 적용시, 출력 결과의 타입이 행렬로 유지, 
#데이터 프레임에서는 drop=FALSE 적용시, 출력 결과의 타입이 데이터 프레임



us.state[,c(2,4)]
us.state[['state.name']]
us.state$state.name

us.state[,'state.name']

us.state[c('state.name','state.area')]  #리스트 인덱싱
us.state[,c('state.name','state.area')]  #행렬 인덱싱





id<-c('a1','a2','a3')
price<-c(10,20,30)
name<-c('x','y','z')


product<-data.frame(id,name,price)
product
str(product)


#rbind():데이터프레임에 행 추가
product<-rbind(product,c('a4','40','k'))
product


#제거
product<-product[-4,]
product
#여러 행 추가


product<-rbind(product,c('a4','k',40))
product


#여러행 추가
new.rows<-data.frame(id=c('a5','a6'),
           name=c('a','b'),
           price=c(50,60))
new.rows

product<-rbind(product,new.rows)
product


#타입 바꿀 때ㄴ
product$price<-as.numeric(product$price)
str(product)
