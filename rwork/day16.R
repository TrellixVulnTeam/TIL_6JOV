#베이지안 기법
#-베이지안 확률의 이론은 사건에 대한 우도(likehood)는
#복수 시행에서 즉시 이용할 수 있는 증거를 바탕으로 추정해야 한다는 
#아이디어에서 출발



#사건         시행
#앞면        동전던지기
#당첨       복권구매
#스팸/햄     메일수신



#사건의 확률: 사건이 발생한 시행횟수/전체 시행횟수

#ex)      스팸메일(10)/받은 메일(50)==20%
#사건 A의 확률= p(A)     p(비), p(스팸)




#사정확률: 이전까지 받은 메시지가 스팸일 확률 20%=>지금 받은 메세지가 스팸일 확률 20%
#우도(likehood): ex)'나이트'단어가 사용될 확률, p(나이트/스팸)

#'나이트'단어가 어떤 메세지에 등장할 롹률  p(나이트): 주변우도'
#'
#'베이즈 이론 수식: p(스팸/나이트)= 우도*사전확률/ 주변우도
#'
#'
#'p(나이트/스팸) *  p(스팸):사정확률/p(나이트)



#조건부 확률:1) A,B사건의 서로 영향을 미치지 않는 경우
#             2)서로 영향을 미치지 않는 경우




#ex) p(A교집합B)= p(A)*p(B)
#비 오고 우산 팔리는 확률
#ex) p(A),p(B)
#-->조건부 확률:p(A교B)=p(A)*p(B|A):a가 일어난 상황에서 b가 일어난 확률
#-->p(A교B)/p(A)


#p(A교B)= p(A)*p(B|A)
#(B교A)= p(B)*p(A|B)
#==>p(A)*p(B|A)=p(B)*p(A|B)
#==>나이브베이지 이론: p(B|A)= p(A|B)*p(B)/p(A)


#p(스팸/나이트)= p(나이트|스팸)*p(스팸)/p(나이트)
#==>사후확률= 우도*사전확률/주변우도


#라플라스 추정량







smsraw<-read.csv('sms_spam_ansi.txt')
smsraw

str(smsraw)
smsraw$type<-factor(smsraw$type)
str(smsraw$type)


install.packages('tm')
library(tm)
library(stringr)


mytext<-c('software environment','software  environment','software\tenvironment')
mytext

str_split(mytext,' ')


sapply(str_split(mytext,' '),length)  #단어수
sapply(str_split(mytext,' '),str_length)  #각 단어를 구성하는 글자수 

#전체문자열을 다른 문자열로 바꾼다 
mytext.nowhitespace<-str_replace_all(mytext, "[[:space:]]{1,}"," ")
mytext.nowhitespace


sapply(str_split(mytext.nowhitespace,' '),length)  #단어수
sapply(str_split(mytext.nowhitespace,' '),str_length)  #각 단어를 구성하는 글자수 



mytext<-'The 45th President of the United States, Donald Trump, states that he knows how to play trump with the former president'
myword<-unlist(str_extract_all(mytext, boundary('word')))
table(myword)
myword

myword<-str_replace(myword, 'Trump','Trump_unique_')
myword<-str_replace(myword, 'States','States_unique_')
myword


table(tolower(myword))

mytext <- c("He is one of statisticians agreeing that R is the No. 1 statistical software.","He is one of statisticians agreeing that R is the No. one statistical software.")
str_split(mytext, " ")


mytext2<-str_split(str_replace_all(mytext, '[[:digit:]]{1,}[[:space:]]{1,}',""), " ")
mytext2


mytext2[[1]]
#문자들 합칠 때 쓰는 함수: str_c

str_c(mytext2[[1]],collapse=" ")
str_c(mytext2[[2]],collapse=" ")

mytext3<-str_split(str_replace_all(mytext, '[[:digit:]]{1,}[[:space:]]{1,}',"_number_"), " ")
str_c(mytext3[[1]],collapse=" ")
str_c(mytext3[[2]],collapse=" ")
mytext



mytext <- "Kim et al. (2014) argued that the state of default-setting is critical for people to protect their own personal privacy on the Internet."

str_split(mytext,' ')

str_split(mytext,'\\. ')


mytext
mytext2<-str_replace_all(mytext,'-',' ')
mytext2

#불용어(stopwords): a,an, the 처럼 빈번하게 사용, but 의미는 찾기 어려운..
#she is an actor, she is the actor



#불용어 사전 설정 및 제거(a, an, the)

mytext<-c('she is an actor', 'she is the actor')
mystopwords<-'(\\ba)|(\\ban)|(\\bthe)'
str_remove_all(mytext,mystopwords)

stopwords('en')
stopwords('SMART')



#어근 동일화 작업
various_be<-'(\\b(a|A)m)|(\\b(a|A)re)|(\\b(i|I)s)|(\\b(W|w)as)|(\\b(W|w)ere)'


mystemmer.func<-function(myt){
  str_replace_all(myt, various_be,'be ')
  print(mytext)
}
mytext <- c("I am a boy. You are a boy. The person might be a boy. Is Jane a boy?")
mystemmer.func(mytext)






mytext <- "The United States comprises fifty states. In the United States, each state has its own laws. However, federal law overrides state law in the United States."
mytext<-unlist(str_extract_all(mytext, boundary('word')))
length(table(mytext))
sum(table(mytext))






#n그램
mytext <- "The United States comprises fifty states. In the United States, each state has its own laws. However, federal law overrides state law in the United States."
myword<-unlist(str_extract_all(mytext,boundary('word')))
myword

mytext.2gram<-str_replace_all(mytext,'\\bUnited States','United_States')
#                                     '\\b(t|T)th United States,'The_united_States')
mytext.2gram


myword2<-unlist(str_extract_all(mytext.2gram, boundary('word')))
table(myword2)

length(table(myword2))
sum(table(myword2))


#말뭉치: VCorpus 함수를 이용하여 구성

my.text.location<-'ymbaek_papers'
mypaper<-VCorpus(DirSource(my.text.location))
mypaper


summary(mypaper)
str(mypaper)
mypaper[[2]]  #메타 데이터 정보가 7개있다. 글자수는 990개
mypaper[[2]]$content  #내용 확인할 수 있다 
mypaper[[2]]$meta  #메타정보


meta(mypaper[[2]], tag='author')<-'Y.M.baek'  #메타정보 입력
mypaper[[2]]$meta
#or
meta(mypaper[[2]])


class(mypaper)

mypaper[[1]]

#전체 정보가 다 나옴
mypaper$content

myfunc<-function(x){   #단어+특수문자+단어 패턴에 해당되는 단어를 추출
      str_extract_all(x$content,'[[:alnum:]]{1,}[[:punct:]]{1}?[[:alnum:]]{1,}')
  
}

mypuncts<-lapply(mypaper, myfunc)

table(unlist(mypuncts))


#대문자로 시작하는 단어들에 대해 빈도수 조사
myfunc<-function(x){   
  str_extract_all(x$content,'[[:upper:]]{1}[[:alpha:]]{1,}')
  
}
myuppers<-lapply(mypaper, myfunc)
myuppers
table(unlist(myuppers))

#숫자로만 표시된자료에 대해 빈도수 조사


myfunc<-function(x){   
  str_extract_all(x$content,'[[:digit:]]{1,}')
  
}
mydigits<-lapply(mypaper, myfunc)
mydigits
table(unlist(mydigits))




smsraw
str(smsraw)
smsCorpus<-VCorpus(VectorSource(smsraw$text))
smsCorpus

smsCorpus[[1]]$content
#or
inspect(smsCorpus[1:5])
inspect(smsCorpus[[1]])

as.character(inspect(smsCorpus[[1]]))




lapply(smsCorpus[1:2], as.character)




#content를 변환함수 적용
smsCorpusClean<-tm_map(smsCorpus, content_transformer(tolower))
smsCorpusClean[[1]]$content
as.character(smsCorpusClean[[1]])





#tm_map함수
#코퍼스에 대해 전처리(변환작업)을 수행하는 함수
#smsCorpus에 대해 tolower(변환)을 수행

#removeNumbers함수를 적용하여 숫자를 모두 제거
res<-tm_map(smsCorpus,removeNumbers)

res[[4]]$content
#or
res<-tm_map(smsCorpus,content_transformer(removeNumbers))
res[[4]]$content


res<-tm_map(smsCorpus,tolower)  #error
res[[1]]$content


res<-tm_map(smsCorpus,content_transformer(tolower))  #error발생안함 
res[[1]]$content


#tm패키지 안에 있는 함수:removeNumbers, removePunctuation, removeWords, stemDocument, and stripWhitespace.
#위의 함수는 단독 사용 가능 & content_transformer()안에 작성하여 사용 가능

#tm패키지 안에 있지 않고 위 5개 함수를 제외한 나머지 함수(사용자 정의 함수를 포함)는 반드시 
#content_transformer()안에 작성해야만 가능



#소문자 변환
smsCorpusClean<-tm_map(smsCorpus, content_transformer(tolower))
smsCorpusClean[[1]]$content

#특수문자 제거
smsCorpusClean<-tm_map(smsCorpusClean, removePunctuation)
smsCorpusClean[[1]]$content


#stopwords제거 
stopwords()
smsCorpusClean<-tm_map(smsCorpusClean, removeWords, stopwords())
smsCorpusClean[[1]]$content



removePunctuation('hello...RP')

remPunct<-function(x){
  gsub("[[:punct:]]+",' ',x)
  
}

remPunct('hello...RP')

install.packages('SnowballC')
library(SnowballC)

#단어단위로 steming하는 것 (어근만)
wordStem(c('run','runs','running'))
wordStem(c('learn','learns','learning','learned'))






