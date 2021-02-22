# 1. 변수 x에 1~10까지 값 할당, y에 3~1까지 값 할당
# - letters 상수벡터를 이용하여 x에 알파벳 소문자 이름 부여
# - x+y를 수행하고 결과를 설명

x<-1:10
y<-3:1

letters[x]
x+y

 # 2. 숫자 2,5,3을 원소로 갖는 벡터 생성한 후 rep함수를 이용하여 다음 벡터를 생성
# - 2,5,3,2,5,3,2,5,3,2,5,3,2,5,3
x<-c(2,5,3)

rep(x,times=5)
# - 2,5,3,2,5,3,2,5,3,2
rep(x,length.out=10)
# - 2,2,5,5,5,5,5,3,3,3
c(rep(2,each=2),rep(5,each=5),rep(3,each=3))





# 3. 주사위를 7번 던져서 나온 3,2,5,1,5,6,5의 값을 
# 1)여섯 개의 레벨을 갖는 팩터로 저장하시오.

n<-c(3,2,5,1,5,6,5)
n.factor<-factor(n,levels=c(1:6))
n.factor
# 2)각 레벨에 one, two, ... six로 이름 부여하시오.

n.factor<-factor(n,levels=c(1,2,3,4,5,6),labels=c('one','two','three','four','five','six'))
n.factor
# 3)레벨별 발생 빈도를 출력하시오.

table(n.factor)



# 4. 1~12까지의 숫자 벡터로 3*4행렬 생성하고 변수에 저장하시오.
# 알파벳 소문자 상수 벡터 letters를 이용하여 행과 열이름을 각각 지정하시오.
# a  b   c   d
# a  1  4
# b 2   5   ...
# c  3  6       12

v<-1:12
a<-matrix(v,3,4)

rnames<-letters[1:3]
cnames<-letters[1:4]
mat<-matrix(v,3,4,byrow = TRUE,dimnames = list(rnames,cnames))

# 5. 4번에서 생성한 행렬로부터 1번째와 3번째 열을 추출하여 부분행렬을 생성하고,
m1<-mat[,c(1,3)]
# 2번째와 4번째 열을 추출하여 부분행렬을 생성하고,
m2<-mat[,c(2,4)]
# 이들을 열의 방향으로 결합한 새로운 행렬을 생성하시오.
mat2<-cbind(m1,m2)
mat2

# 6. 4번과 5번문제에서 생성한 두 행렬에 대해 +, -, *, /, %*% 연산을 수행하시오
mat+mat2
mat-mat2
mat*mat2
mat/mat2
t(mat)%*%mat2
mat%*%t(mat2)

# 7. 1~9999까지 정수로 9개의 열을 갖는 행렬을 생성하시오.
mat<-matrix(1:9999,ncol=9)
mat
# 마지막 세 개 행과 마지막 두 개 열로 구성된 3*2 부분행렬을 만드시오.

mat[c(dim(mat)[1]-2,dim(mat)[1]),c(dim(mat)[2]-1,dim(mat)[2])]
