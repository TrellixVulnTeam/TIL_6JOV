print('hello')
print(
  'hello'
)
print('hello')

?print

#스칼라, 벡터, 행렬, 데이터프레임, 리스트
#스칼라:길이가 1인 벡터

#키, 몸무게, 혈액형, 나이(4차원 벡터)
(170,60,A,30)
(180,60,A,30)
(150,60,A,30)
...
(120,60,A,30)


50*4
#하나의 벡터를 이루는 데이터의 개수가 N개이면 N차원 벡터라고 함

이미지 데이터(100*100픽셀)
ex) (2)

a<-3 
a
print(a) 
b<-2
b                                     
c(1,2,3)
c('we','love','data')

odd<-c(1,3,5)
even<-c(2,4,6)
c(odd,even)
3:9
5:-1

#다양한 증감치를 이용한 수열 생성
seq(from=3,to=9) #3:9
seq(from=3,to=9 ,by=0.5)
seq(from=3,to=9 ,by=-0.5)
#수열의 길이를 지정
seq(from=0,to=100 ,length.out=5)

#백터 전체를 반복할 때 times사용
rep(1,times=3)
rep(c(1,2,3),times=5)

#벡터의 각 원소값들을 반복할 때 each사용
rep(c(1,2,3),each=5)
rep(1:3,length.out=8)



#벡터는ㄴ 동일한 데이터 유형으로 표현됨
n<-c(1,2,3)
cha<-c('x','y','z')
c(n,cha)

#str:벡터의 유형 및 구조 확인
str(n)
#num(numeric):수치
str(cha)
#벡터의 길이:3,3개 의 원소를 갖는 1차원 벡터

#length:벡터의 길이만 확인
length(n)



#상수 벡터

LETTERS
letters
month.abb
month.name
pi

m<-c(12,9,3,5,1)


month.name[c(1,2)]
month.name[m]


시가 종가 거래량(features)
100 200   500     


#벡터화(vectorized)연산=>속도가 빠르다
1+2  #1이라는 벡터와 2라는 벡터에 +연산을 수행한 결과 
2^10
10%%3
10%/%3

#벡터 연산은 원소와 원소기리 연산 수행
c(1,2,3)+c(4,5,6)



x<-c(1,2,3)
x*c(4,5,6)


y<-c(10,20,30)

y/c(2,4,5)

y%%c(3,5,7)


#길이가 짧은쪽의 요소가 반복되어진다
x<-c(1:3)
y<-c(4:9)

x+y

#스칼라와도 연산 가능,길이가 다를 때 길이가 짧은 쪽의 요소가 반복되어진다
c(1,3,5)+10


#배수관계가 아니여도 연산결과는 뜨지만 경고메세지 뜸
c(1,2,3)+c(4,5,6,7,8)


#논리연산자:==,!=,<,>,<=,>=,!x ,x|y,x&y,isTRUE(x)

v<-pi
w<-10/3

v==w
v!=w
v>w
!(v>w)
v<w

(v==w)|(v<w)
(v==w)&(v<w)
isTRUE(v==w)

x<-c(1,3,5)
y<-c(3,3,3)
x==y
x==3

#r은 TRUE는 1, FALSE는 0으로 간주
as.numeric(TRUE) #논리값->숫자로 변환
as.numeric(FALSE)
TRUE+TRUE
FALSE+FALSE

x<-c(0,25,50,75,100)
sum(x>50)

sum(1:5)
sum(1,2,3)
sum(1:2,3:5)
sum(TRUE,FALSE,TRUE)

#any함수:논리값이 하나로도 TRUE이면 결과가 TRUE리턴
#all함수:논리값이 모두 TRUE이면 결과가 TRUE

a<--3:3
a
any(a>0)
all(a>0)

sqrt(2)^2==2
sqrt(2)^2-2


#수치 비교시 정밀도 문제를 피하기 위해서는 all.equal()함수를 이용,약간의 오차를 무시하므로,
#두 값이 같다고 출력되어진다
all.equal(sqrt(2)^2, 2)

#2의 제곱근의 제곱=>2이지만, r에서는 정확하게 2가 아님(부동소수점수 연산)


#행벡터=(1,90,80)
#열벡터=()


fruits<-c('Apple','Banana','Strawberry')
food<-c('Pie','Juice','Cake')

#fruits+food 에러
#문자끼리 결합할때는 paste함수
paste(fruits,food)

paste(fruits,'Juice')



x<- -3:3
abs(x)


#로그값: log함수는 리폴트가 밑수가 e인 자연로그
log(1:5)

log(1:5,base=3) #밑수가 3인 로그
log(1:5,base=2) #밑수가 2인 로그
log(1:5,base=10)


#밑수가 10인 로그함수 
log10(1:10)
#밑수가 2인 로그함수
log2(1:10)


#exp함수: 밑수가 e인 지수값

exp(1:5)

y<-exp(1:5)
log(y)

factorial(1:5)

choose(5,2)  #5개중에서 2개를 선택하는 경우의 수, 5c2

#nCr = n!/(r!(n-r)!)=>120/12=>10

sqrt(1:5)  #유효자릿수가 7자리


#현재 시스템의 유효자리수 확인
options('digits')


#유효자리 수 확인하고 싶을 때
signif(456.789,digits = 2)
signif(456.789,digits = 3)
signif(456.789,digits = 4)


round(456.789,digits =1)
round(456.789,digits = 2)
round(456.789,digits = 3)


#1~10까지 수에 대한 각각의 제곱근을 구한 다음 소수이하 2자리까지 출력


x<-sqrt(1:10)
round(x,digits=2)
#한줄로
round(sqrt(1:10),digits=2)


round(456.789,digits=1)

#-n를 주면 정수부분에서n번째 자리에서 반올림
round(456.789,digits=-1)
round(456.789,digits=-2)


#가까운 짝수로 반올림
round(11.5)
round(12.5)


#floor:작은 가까운 정수로 반올림
#ceiling:큰 가장 가까운 정수로 반올림
#trunc:0에 가까운 정수로 반올림


floor(456.78)
floor(-456.78)




ceiling(456.78)
ceiling(-456.78)


trunc(456.78)
trunc(-456.78)


3/0
5-Inf
Inf*Inf
Inf*(-Inf)



#r에서는 1.8*10의 308승까지 표현 가능

is.infinite(10^306)
is.infinite(10^307)
is.infinite(10^308)
is.infinite(10^309)

is.infinite(10^(306:310))


#NsN(Not a Number:숫자가 아님, 계산 결과를 정의할 수 없다)
Inf/Inf
Inf*0
log(-2)            
NaN+3
is.nan(Inf*0)


#Na(Not Available,결측값)
k<-NA
k+2
sqrt(NA)


z<-1:5
z
sum(z)

#prod:벡터의 요소들을 다 곱하는 것
prod(z)
min(z)
max(z)
mean(z)
median(z)
var(z)
sd(z)
range(z)


z<-c(z,NA)
z

sum(z)
range(z)
median(z)

#NA제거하는 법

sum(z,na.rm = TRUE)
sum(na.omit(z))


#cumsum함수: 누적합
traffic.death<-c(10,20,NA,30,20)
cumsum(traffic.death)



#diff:뒤쪽 원소에서 앞쪽 원소의 차 
traffic.death<-c(10,20,30,20)
diff(traffic.death)



1:10
diff(1:10,lag=3) #3칸 떨어진 원소간의 차를 구함


p<-1:10
q<-6:15
#union(p,q):두 벡터에 대한 합집합
union(p,q)  #합집합 
intersect(p,q)#교집합
setdiff(p,q) #차집합

setequal(p,q) #두 집합이 동일한지 확인

#첫번째 인수에 오는 값이 두번째 벡터의 원소인지 테스트:is.element()
is.element(3,1:5)
is.element(6,1:5)
is.element(4:7,1:5)


#인덱스는 파이썬은 1번부터 시작하지만 r은 0번부터 시작함
num<-0:30
num[5]
num[5:10]


num[c(2,5,10,27)]



#1,3,5인덱스에 해당하는 벡터를 추출
prime<-c(2,3,5,7,11,13)
idx<-c(1,3,5)
prime[idx]



prime[-3]  #3번 인덱스가 제외

prime[-2:-4] #2~4번 인덱스가 제외

prime[-(2:4)] #2~4번 인덱스가 제외



prime<-c(2,3,5,7,11,13)
length(prime)


prime[1:(length(prime)-2)]


prime[-length(prime)]


#2번 인덱스 값을 30으로 변경
prime[2]<-30
prime


prime[c(3,4)]<-c(30,40)
prime
