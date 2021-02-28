#문자열 대체: 
#grep함수: fixed=FALSE(default),pattern에 작성된 식을 정규표현식으로 해석
#그러나 fixed=TRUE이면 pattern 에 작성한 값을 문자열로 취급

#정규표현식이 포함된 문자열 추출
words<-c('at','bat','cat','cheap','check','cheese','chick','hat','chase')
grep('che',words,value=TRUE)
grep('che',words)
grep('at',words,value=TRUE)

#c또는 h가 포함된 문자열 검색
grep('[ch]',words,value=TRUE)
#a또는 t가 포함된 문자열 검색
grep("[at]",words,value=TRUE)

#ch또는 at가 포함된 문자열 검색
grep("ch|at",words,value=TRUE)


#check,chick
#ch  +e 또는i+  ck
grep("ch(e|i)ck",words,value=TRUE)

#?: ?앞의 문자가 0번 또는 1번 나타나는 패턴(최대 1번)
#*: *앞의 문자가 0번 이상 반복되는 패턴(최소0번)
#+: +앞의 문자가 1번 이상 반복되는 패턴(최소0번)

words<-c('at','bat','cat','cheap','check','cheese','chick','hat','chase','chaenomeles','chasse')
grep("chas?e",words,value=TRUE)  #chase,chae

grep("chas*e",words,value=TRUE) #chase,chae,chasee

grep("chas+e",words,value=TRUE)

#chase, cheese만 출력 되도록 하고싶을 떄
grep("ch(as|e+)se",words,value=TRUE)
grep("ch(a*|e*)se",words,value=TRUE)


grep("^c",words,value=TRUE)
grep("t$",words,value=TRUE)

#.(마침표):모든 문자
#.*:모든 문자가 0개 이상

#c로 시작하고 t로 끝나는 모든 문자열 검색
grep("^c.*t$",words,value=TRUE)

#at앞에 아무 문자도 없거나 h 또는 c로 시작하는 문자열을 검색
grep("^[hc]?at",words,value=TRUE)
grep("^at|(h|c)at",words,value=TRUE)


word2<-c("12 Dec", "OK", "http://", "<TITLE>Time?</TITLE>","12345", "Hi there")


#[[:alnum:]]: 알파벳+숫자
#[[:digit:]]: 숫자
#[[:punct:]]: 문장부호, 특수문자
#[[:space:]]: 공백
#[[:alpha:]]: 알파벳

grep("[[:alnum:]]",word2,value = TRUE)
grep("\\w",word2,value = TRUE)


grep("[[:alpha:]]",word2,value = TRUE)

grep("[[:digit:]]",word2,value = TRUE)
grep("\\d",word2,value = TRUE)


grep("[[:punct:]]",word2,value = TRUE)

grep("[[:space:]]",word2,value = TRUE)
grep("\\s",word2,value = TRUE)



#Sys.Date():현재 날짜 

Sys.Date()

date()

Sys.time()

class(Sys.Date()) #타입=date
class("2021-02-26") #타임=문자열

as.Date("2021-02-26") #date타입->문자열 타입

as.Date("02/26/2021",format="%m/%d/%y")  #2021-02-25이런 형식이 기본형식,기본형식이 아닐경우 format적용



d<-as.Date("2021-02-26")
format(d,format="%m/%d/%y")



today<-Sys.Date()
today
format(today,format="%Y/%m/%d %A")


weekdays(as.Date("2021-02-27")) #특정일의 요일 정보가 나옴


d<-as.Date("2021-02-27")
d-1  #연산 가능함
d+1:10

weekdays(d+1:10)


#seq함수: 연속된 날짜 생성
s<-as.Date("2021-02-26")
e<-as.Date("2021-04-1")
seq(s,e,1)

#lengthout()
seq(from=s,by=1,length.out=10)

#동일한 결과
seq(from=s,by=7,length.out=9)
seq(from=s,by="7 days",length.out=9)
seq(from=s,by="week",length.out=9)

seq(from=s,by="month",length.out=9)
seq(from=s,by="2 months",length.out=9)

seq(from=s,by="year",length.out=9)
seq(from=s,by="2 year",length.out=9)


seq(from=as.Date("2021-01-30"),by="month",length.out=5)





s<-as.Date("2021-02-26")
qrt<-seq(from=s,by="3 months",length.out=4)
qrt
months(qrt)
quarters(qrt)  #분기정보


install.packages("reprex")

#입력

product<-data.frame()
product
product<-edit(product)  #fix(product)와 같은 문장
product



write.csv(product,file="myproduct.csv",row.names = FALSE)

#엑셀에서 name열 복사 한 후 
p<-readClipboard()
p


#a1부터 c4까지 복사
p<-readClipboard()
p


read.table(file="clipboard",sep="\t",header=TRUE)




read.csv("product.csv")

read.csv("product-with-no-header.csv",header=FALSE)

p<-read.csv("product.csv",stringsAsFactors = TRUE)
str(p)

p<-read.csv("product.csv",as.is=TRUE)  #as.is=TRUE는 stringAsFactors=FALSE와 같음

#readtable은 다양한 구성의 자료를 읽을 수 있고 readcsv는 ,로 구분된 자료를 읽음
#read.table은 첫번째부터 데이터로 봄(헤더 설장 따로 해주어야함)
p<-read.table("product.txt",header=TRUE)
p


str(p)


read.table("product-colon.txt",sep=":",header=TRUE)


#NA:데이터 누락(결측값)
read.table("product-missing.txt",header=TRUE,na.strings =c('누락','몰라'))


#read.table()는 #으로 시작하는 라인은 주석문으로 간주하고 무시함

read.table("product-comment.txt",header=TRUE)

brand.eval<-read.table("brand-eval.csv",header=TRUE,sep=",",row.names = "id")
str(brand.eval)
brand.eval


brand.eval<-read.table("brand-eval.csv",header=TRUE,sep=",",row.names = "id",
                       colClasses = c('character','character','numeric','numeric','numeric'))
brand.eval

#엑셀 데이터 읽기 
install.packages("openxlsx")
library(openxlsx)
read.xlsx("product.xlsx",sheet=1)


url<-"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris.uci<-read.csv(url,header=FALSE)
iris.uci


download.file(url=url,destfile = "myIris.csv")



#

url<-"http://seanlahman.com/files/database/baseballdatabank-master_2016-03-02.zip"
local.copy<-"baseball.zip"
download.file(url,local.copy)


bs<-read.csv(unzip(zipfile = local.copy,"baseballdatabank-master/core/Salaries.csv"))
head(bs)


install.packages("ggplot2")
library(ggplot2)
mpg

mpg$displ

midwest<-as.data.frame(midwest)  #tibble->dataframe
install.packages("dplyr")
library(dplyr)

#rename(데이터프레임, 변경후컬럼이름=변경전 컬럼 이름)
midwest

rename(midwest, cg=category)
