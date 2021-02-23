p<-c(2,3,5,7,11,13,17,19)
p
p[3]
p[3:5]
p[c(1,5,7)]

p[-3]
p[-3:-5]

p[-(3:5)]

p[1:length(p)-1]
p[-length(p)]

p[2]<-13
p
p[c(6,8)]<-c(100,200)
length(p)
p[15]<-99
p

#불린참조
p

p<10

p[p<10]  #p<10보다 작은 값들만 참조 출력(TRUE에 해당하는 것만 출력됨)

p
p[c(TRUE,TRUE,FALSE)]


#which():논리값->TRUE위치 인덱스 추출 함수
#which.max(),min()함수도 있음

data<-c(100:111)  #12건 데이터(1월~12월까지)
data
which(data>105)


month.abb[which(data>105)]
month.name[which(data>105)]

which.min(data)  #data에 저장된 자료 중 최소값의 인덱스
which.max(data)  #data에 저장된 자료 중 최대값의 인덱스

#요일별 교통하고 사망자수 데이터
traffic.death<-c(100,90,80,70,120,150,200) #월~일 사망자 수 

#토요일 사망자수
traffic.death[6]
names(traffic.death)<-c('mon','tue','wed','thu','fri','sat','sun')
names(traffic.death)

traffic.death['sat']

traffic.death[c('sat','wed')]


#사망자수가 100명 이상인 요일만 출력
traffic.death>=100
traffic.death[traffic.death>=100]
names(traffic.death[traffic.death>=100])


#팩터(factor):카테로기 구분하는목적으로 사용되는 데이터를 범주형 데이터로
#레벨(level):범주형(팩터)에 포함된 범주값
#factor()함수: 범주형 데이터로 사용하고자 하는 문자 or 숫자 벡터를 팩터로 변환

#문자벡터
review<-c('good','good','bad','indifferent','bad','good')
review

review.factor<-factor(review)
review.factor

str(review.factor)
str(review)

as.numeric(review.factor) #팩터형->숫자벡터로 변환

everyday<-c('mon','mon','fri','tue','tue')
#everyday.factor<-factor(everyday)
#everyday.factor

everyday.factor<-factor(everyday, levels=c('mon','tue','wed','the','fri','sat','sun'))
everyday.factor


levels(everyday.factor)

#레벨을 바꾸고 싶을 때
levels(review.factor)

levels(review.factor)<-c('B','G','I')
review.factor

#레벨의 개수를 셀 때

nlevels(review.factor)

length(levels(review.factor))


#서열팩터(ordered factor): 순서가 있는 범주형 데이터, 부등호 기호로 서열 표시

eval<-c('Medium','Low','High','Medium','High')
eval.factor<-factor(eval)
eval.factor

eval.ordered<-factor(eval,levels=c('Low','Medium','High'),ordered = TRUE)
eval.ordered

#table():각 레벨별 빈도

eval.factor
table(eval.factor)


table(eval.ordered)

#숫자벡터->펙터로 변환
sex<-c(2,1,2,2,1,0)
sex.factor<-factor(sex,levels=c(1,2),labels=c('Male','Female'))
sex.factor



#행렬:2차원 벡터,벡터에 차원을 부여 (dim함수)
#행렬:벡터로 구성, 벡터는 타입이 모두 동일
#matrix함수로도 행렬 생성

v<-1:12
#행을 3개 열을 4개로 만들어라
dim(v)<-c(3,4)
v

matrix(data=v,nrow=3,ncol=4,byrow=TRUE)

#생략해도 됨
matrix(v,3,4,byrow=TRUE)


rnames<-c('r1','r2','r3')
cnames<-c('c1','c2','c3','c4')

matrix(v,3,4,byrow=TRUE,dimnames = list(rnames,cnames))


#데이터를 0으로 초기화
matrix(0,3,4)

matrix(NA,3,4)

mat<-matrix(v,ncol=4)
#행렬은 2차원 벡터
str(mat)

#행, 렬(차원에 대한 정보 나옴)
dim(mat)

#행의 개수
dim(mat)[1]
#열의 개수
dim(mat)[2]

nrow(mat)

ncol(mat)

#전체 데이터의 개수(벡터의 길이)
length(mat)

#두 벡터를 결합하여 행렬을 생성
v1<-1:5
v2<-6:10

rbind(v1,v2)
cbind(v1,v2)

#벡터와 행렬을 결합하여 새로운 행렬 생성
1:3
4:6
cbind(1:3,4:6,matrix(7:12,3,2))


#행렬과 행렬간 결합하여 새로운 행렬 생성
matrix(1:6,2:3)
matrix(7:12,2,3)

#위의 두개의 행렬을 위 아래로 결합하고 싶을 때
rbind(matrix(1:6,2:3),matrix(7:12,2,3))

v<-1:12
mat<-matrix(v,3,4)      
mat

#행에 해당하는 차원만 추출하고 싶을 때(행렬이 아닌 벡터로 출력됨,2차원->1차원)
mat[1,]

#열에 해당하는 차원 추출(행렬이 아닌 벡터로 출력됨,2차원->1차원)
mat[,3]



#행렬에서 특정 행이나 열을 추출할 때 1차원 벡터가 되어버리는데 이것을 2차원 행렬구조가 유지되게 할 때

mat[1,,drop=FALSE]
mat[,3,drop=FALSE]

mat[2:3,]
mat[,3:4]
mat[1:2,2:3]
mat[c(1,3),]

mat

mat[,c(1,4)]
mat[,-c(2,3)]

#행렬에 저장된 데이터 변경하는 방법 
mat[1,3]<-77
mat


mat[2,]<-c(22,55,22,55)
mat

mat[2,]<-c(22,55)
mat

mat[2:3,3:4]<-c(1,2,3,4)
mat


#matrix생성하시오 
       seoul busan daegu gwangju jeonju
seoul   0    350    300   3000     200
busan   350    0
daegu
gwangju
jeonju



rnames<-c('seoul', 'busan', 'daegu', 'gwangju', 'jeonju')
cnames<-c('seoul', 'busan', 'daegu', 'gwangju', 'jeonju')
v<-c(0,350,300,300,200,350,0,50,200,190,300,50,0,180,200,300,200,180,0,80,200,190,200,80,0)


city.distance.mat<-matrix(v,5,5,byrow=TRUE,dimnames = list(rnames,cnames))

city.distance.mat['seoul','busan']

city.distance.mat[c('seoul','gwangju'),]


w<-c(1,2,3,4,5,6)
mtx<-matrix(w,2,3)
mtx

mtx+1
mtx-1
mtx*2
mtx/2

#행렬간 연산할 때는 반드시 두 행렬의 차원이 같아야함

matrix(1:6,2,3)
matrix(6:1,2,3)

matrix(1:6,2,3)+matrix(6:1,2,3)

#행렬 차원 다를 때는 수행되지 않음
matrix(1:6,2,3)+matrix(6:1,3,2)


#element-wise product(행렬끼리 계산한 것이 아니고 행렬의 요소끼리 곱셈이 이루어진 것)
matrix(1:6,2,3)*matrix(6:1,3,2)


#행렬끼리 연산할 때
#행렬의 곱셈은 앞의 행렬의 열과 뒤의 행렬의 행이 일치
w
matrix(w,2,3)%*%matrix(w,2,3)


matrix(w,2,3)%*%matrix(w,3,2)

mtx<-matrix(w,2,3)
mtx%*% 1:3  #2행 3열 %*% 길이 3인 벡터->3행 1열

mtx
t(mtx)

t(t(mtx))


mtx
#행 합계를 구하는 함수
rowSums(mtx)
#열 합계 구하는 함수
colSums(mtx)

#행 평균
rowMeans(mtx)
#열 평균
colMeans(mtx)
