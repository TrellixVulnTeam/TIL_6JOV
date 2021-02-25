#정렬: sort(),order()
#sort():데이터가 정렬된 결과
#order():데이터 크기의 색인을 출력

v1<-c(20,10,50,40,20)
v2<-c(300,200,100,700,600)
v3<-c('a','b','b','a','b')
df<-data.frame(v1,v2,v3) 
df

#벡터 정렬
v1
sort(v1) #오름차순
sort(v1,decreasing = TRUE) #내림차순

#order(): 정렬 색인 값을 추출
v1
order(v1) #오름차순정렬했을 때, 
#20,10,50,40,30->10,20,30,40,50
#1  2 3  4   5  -> 2 1 5 4  3

v1[order(v1)]


#sort함수: 데이터프레임에서는 사용x
#order함수: 데이터프레임 정렬에서 사용

df

order(v1) #오름
order(-v2) #내림
order(v3) #오름

#      기준1/기준2/기준3
df[order(v1,-v2,v3),]

df[order(v1),]

df[order(v1,-v2,v3),]



install.packages('plyr')
library(plyr)
arrange(df, v1, desc(v2))

sort(letters,decreasing = TRUE)



x<-c(2,-1,3,7,0.5,8)
x[x]






#텍스트마이닝 ->베이즈이론 기반 베이지안 필터 이메일분류기(햄/스팸,성능 좋지 않은 편...)
#text mining

x<-'We have a dream'
#nchar함수(텍스트 안에 문자의 개수 , 공백문자도 하나의 문자로 취급)
nchar(x)
length(x) #문자 벡터의 벡터 길이(문자열자체를 하나로 봄(원소 개수 1개))

length(c('we','have','a','dream'))  #백터 길이4

y<-c('we','have','a','dream')
length(y[4])
nchar(y[4])

nchar(y)

#대소문자 변경
x<-'We have a dream'
tolower(x)
toupper(x)

#문자 분리하는 함수:split()
strsplit(x,split=' ')
class(strsplit(x,split=" "))  #공백 문자로 구분된 각각의 단어들로 구성된 벡터가 리스트에 저장됨

#모든 문자 분리 됨
strsplit(x,split="")


#strsplit 결과가 리스트로 저장
#리스트->벡터
unlist(strsplit(x,split=" "))
#or
res<-strsplit(x,split=" ")[[1]]
res[4]



x1<-'We have a dream'
x2<-'How are you'
x3<-'I am fine'

myword<-c(x1,x2,x3)
length(myword)
myword

#리스트로 나옴
strsplit(myword,split=" ") 
  
#i am fine 참조
strsplit(myword,split=" ")[[3]]
#fine 참조
strsplit(myword,split=" ")[[3]][3]


#대소문자 구분됨. what What WHAT wHat...다른 단어로 취급됨

#korea,Korea,KOREA,한국, 대한민국, 조선,...=>우리나라

said<-'WHAT IS ESSENTIAL is invisible to the Eye'
said.word<-strsplit(said, " ")


#unique():유일한 단어를 추출해주는 함수
unique(said.word)
#벡터로 접근해야됨
tolower(unique(said.word[[1]]))


##apply함수!!


#정규화작업 
apply(iris[,-5], 2, function(x){(x-min(x,na.rm = TRUE))/max(x, na.rm=TRUE)-min(x, na.rm=TRUE)})


#paste():문자열 결합 함수->하나의 문자열로 생성
paste('Everybody','wants','to','fly')

paste(c('Everybody','wants','to','fly'))  #한개의 벡터가 되버림,따라서 결합 안됨
#paste():분리된 벡터를 결합하는 함스 벡터의 원소들을 분리한 다음 결합하지 않는다



#이것도 역시 res가 벡터로 반환되기 때문에 결합하지 않고 따로 나옴
said<-'WHAT IS ESSENTIAL is invisible to the Eye'
res<-strsplit(said," ")[[1]]
paste(res)


#기본값으로 공백문자
paste('Everybody','wants','to','fly')

paste('Everybody','wants','to','fly',sep='-')

paste('Everybody','wants','to','fly',sep='')



#텍스트가 아닌 경우에는 모두 텍스트로  변환한 다음, 결합 수행
paste(pi,sqrt(pi))

paste("aaa",1+2,"bbb")  #1+2의 결과 3이 문자열로 변경된 후 paste함수 수행



#벡터를 인수로 준 경우에는 요소간 결합
heroes<-c('Batman','Captain America','Hulk')
colors<-c('Black','Blue','Green')
paste(colors,heroes)

paste('type',1)
paste('type',1:5)
#
c(1,2,3,4,5)
c('type') #길이 1->길이 5로 변경됨(c('type','type','type','type','type'))



paste(heroes,"wants","to")

paste(c('Everybody','wants','to','fly'))

#paste함수 collapse옵션: 텍스트 결합을 통해 생성된 텍스트들을 다시 하나로 연결하는 구분자를 정의할 때 사용


paste(c('Everybody','wants','to','fly'),collapse=" ")



heroes<-c('Batman','Captain America','Hulk')
sen<-paste(c('Everybody','wants','to','fly'))
sen

paste(heroes,sen[[2]],collapse=" and ")

#
heroes<-c('Batman','Captain America','Hulk')
paste(heroes,'wants','to','fly',collapse=", and ")


#paste함수에 sep옵션, collapse옵션
heroes<-c('Batman','Captain America','Hulk')
paste(heroes,'wants','to','fly',sep='-',collapse=';')

#p                  g
#donald-Trump, trump


#outer():두 집합에 대해 가능한 모든 순서쌍으 ㅣ곱을 수행(카티전 곱)
outer(c(1,2,3),c(3,2,1))

#outer+paste함수를 결합해서 문자열 생성
#outer함수의 3번째 자리에 인수자리에 함수를 작성(원래 카티전곱이 디폴트이지만 다른 연산을 하도록 수행할 수 있음)

asia.countries<-c("Korea","China","India")
info<-c('GDP','Population','Area')
outer(asia.countries,info, FUN=paste,sep="-")

#as.vector():행렬->벡터형식
out<-outer(asia.countries,info, FUN=paste,sep="-")
as.vector(out)


#
res<-out<-outer(asia.countries,asia.countries, FUN=paste,sep="-")


#lowe.tri():하삼각행렬 TRUE로 반환
res[lower.tri(res)]
#앞에 !붙이면 반전됨
res[!lower.tri(res)]




#substr:텍스트의 특정 부분 문자열 추출

substr('Data Analytics',1,4)
substr('Data Analytics',6,14)

#substring:텍스트의 특정 부분 문자열 추출, 끝위치 생략 가능
substring('Data Analytics',6)
#원소별로 부분 문자열 추출
myclass<-c('Data Analytics','Data Minig','Data Visualization')
substr(myclass,1,4)

substr(myclass,nchar(myclass)-5,nchar(myclass))


#grep():New문자열이 포함된 단어의 인덱스를 추출
class(islands)
landmasses<-names(islands)

index<-grep(pattern="New",x=landmasses)
landmasses[index]

grep(pattern = "New",x=landmasses,value = TRUE)



#두 개 이상의 단어로 이루어진 대륙 또는 섬을 출력
grep(pattern = " ",x=landmasses,value = TRUE)
#or
landmasses[grep(pattern = " ",x=landmasses)]



#sub(),gsub() 함수: 문자열 검색->다른 문자열 변경
#sub:처음 문자열 1개만 다른 문자열 변경
#gsub:일치하는 모든 문자열을 다른 문자열로 변경


txt<-'Data Anal is useful. Data Anal is interesting.'
sub(pattern = "Data",replacement = "Business",txt)

gsub(pattern = "Data",replacement = "Business",txt)


x<-c('input.csv','data.csv','big.csv')
#확장자를 제외한 파일명만 출력


gsub(pattern = ".csv",replacement = "",x)



#finance.yahoo.com->samsung
df<-read.csv("samsung.csv",header=TRUE,sep=",")
df

df2<-read.csv("samsung.csv")  #,header=TRUE,sep="," 디폴트
df2

read.csv('samsung.csv',header=FALSE,sep=',')
