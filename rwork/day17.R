smsraw<-read.csv("sms_spam_ansi.txt",fileEncoding = 'euc-kr')
smsraw
str(smsraw)
smsraw$type<-factor(smsraw$type)
str(smsraw)

install.packages("tm")
library(tm)
library(stringr)

# tagging(태깅)
# 품사 태깅
# 단어 태깅
# 
# SAMSUNG 회사
# 홍길동 사람이름

table(smsraw$type)

smsCorpus<-VCorpus(VectorSource(smsraw$text))
inspect(smsCorpus[1:3])

smsCorpus[[1]]
as.character(smsCorpus[[1]])

lapply(smsCorpus[1:5], as.character)

smsCorpusClean<-tm_map(smsCorpus, content_transformer(tolower))

as.character(smsCorpus[[5]])
as.character(smsCorpusClean[[5]])

#숫자 제거
smsCorpusClean<-tm_map(smsCorpusClean, removeNumbers)
as.character(smsCorpusClean[[5]])
#불용어 제거
stopwords()
smsCorpusClean<-tm_map(smsCorpusClean, removeWords, stopwords())
as.character(smsCorpusClean[[5]])

#구두점 제거
smsCorpusClean<-tm_map(smsCorpusClean, removePunctuation)
as.character(smsCorpusClean[[5]])

removePunctuation("hi...hello! Kim.")

replacePunctuation<-function(x){ gsub("[[:punct:]]+", " ", x)}
replacePunctuation("hi...hello! Kim.")

#word stemming
library(SnowballC)
wordStem(c("learns", "learning"))

?stemDocument()

as.character(smsCorpusClean[[4]])

smsCorpusClean<-tm_map(smsCorpusClean, stemDocument)
as.character(smsCorpusClean[[4]])

smsCorpusClean<-tm_map(smsCorpusClean, stripWhitespace)
as.character(smsCorpusClean[[4]])

lapply(smsCorpus[1:3], as.character)
lapply(smsCorpusClean[1:3], as.character)

#DTM(행:문서, 열:단어가 오는 행렬)
smsDtm<-DocumentTermMatrix(smsCorpusClean)
smsDtm

#Maximal term length: 40 가장 긴 문자수를 갖는 단어의 문자 수

#TF-IDF 알고리즘:문서간 유사도를 측정하는 알고리즘

#문서의 이름
rownames(smsDtm[,])

inspect(smsDtm[1:3,50:60])


#랜덤하게 분할
smsDtmTrain<-smsDtm[1:4169,]
smsDtmTest<-smsDtm[4170:5559,]

smsDtmTrain<-smsDtm[1:4169,]
smsDtmTest<-smsDtm[4170:5559,]


smsTrainLabels<-smsraw[1:4169,]$type
smsraw$type
smsTestLabels<-smsraw[4170:5559,]$type
prop.table(table(smsTrainLabels))
prop.table(table(smsTestLabels))

install.packages("Wordcloud")
library(wordcloud)
wordcloud(smsCorpusClean, min.freq = 50, random.order=FALSE, ordered.colors=TRUE,
)

spam<-subset(smsraw, type=='spam')
ham<-subset(smsraw, type=='ham')

wordcloud(spam$text, max.words = 40, colors = brewer.pal(5,"YlGn"))
wordcloud(ham$text, max.words = 40, colors = brewer.pal(7,"Greens"))
#DTM(행:문서, 열:단어가 오는 행렬)
smsDtmTrain
smsDtmFreqTrain<-removeSparseTerms(smsDtmTrain,0.999)
smsDtmFreqTrain
#removeSparseTerms는 sparse term을 제거해주는 함수

findFreqTerms(smsDtmTrain,5, 10) #최소 5번 이상 최대 10번 이하 등장한 단어

smsFreqWords<-findFreqTerms(smsDtmTrain,5)
str(smsFreqWords)


smsDtmFreqTrain<-smsDtmTrain[,smsFreqWords]
smsDtmFreqTest<-smsDtmTest[,smsFreqWords]

smsDtmFreqTrain #4169*1137
smsDtmFreqTest  #1390*1137

#1137개 각각의 단어에 대해서 등장한 경우/등장하지 않은 경우로 나누어
#구분하여 저장 ex) 등장->YES, 등장X->NO

convertCounts<-function(x){
  x<-ifelse(x>0, "Yes", "No")
}
smsTrain<-apply(smsDtmFreqTrain, MARGIN = 2, convertCounts)
smsTrain
smsTest<-apply(smsDtmFreqTest, MARGIN = 2, convertCounts)
smsTest[5,1:5]

str(smsTrain)
smsTrain[1]
smsTrain[4169]

smsTrain
str(smsTrain)
str(smsTest)

#나이브베이즈 패키지 설치 & 로드
install.packages("e1071")
library(e1071)

#나이브베이즈 모델 생성
smsClassifier<-naiveBayes(smsTrain, smsTrainLabels)
smsClassifier

smsTrain
smsTrainLabels
#테스트데이터 -> 모델 -> 예측(분류) 결과
smsTestPred<-predict(smsClassifier, smsTest)

smsTestPred #예측
smsTestLabels #정답

library(gmodels)
CrossTable(smsTestPred, smsTestLabels)



#나이브베이즈 모델 생성
smsClassifier2<-naiveBayes(smsTrain, smsTrainLabels, laplace = 1)

#테스트데이터 -> 모델 -> 예측(분류) 결과
smsTestPred2<-predict(smsClassifier2, smsTest)

smsTestPred2 #예측
smsTestLabels #정답

library(gmodels)
CrossTable(smsTestPred2, smsTestLabels)


# 
# #tf-idf 사용
# 
# 코퍼스
# 문서1:먹고 싶은 사과
# 문서2:먹고 싶은 바나나
# 문서3:길고 노란 바나나 바나나
# 문서4:저는 과일이 좋아요
# 
# DTM(4*9) 문서-단어 행렬
#        과일이 길고 노란 먹고 바나나 사과 싶은 저는 좋아요
# 문서1    0      0    0    1     0     1    1    0     0
# 문서2    0      0    0    1     1     0    1    0     0
# 문서3    0      1    1    0     2     0    0    0     0
# 문서4    1      0    0    0     0     0    0    1     1
# 
# 유사도 알고리즘 : 유클리디안거리, 코사인유사도
# 문서간 유사도 : 코사인유사도, TF-IDF유사도(LDA, LSA,...)
# 
# tf(d,t):특정 문서 d 내에서 t 단어가 발생한 횟수
# ex)tf(d1,사과)=1
# df(t) : 특정 단어 t가 등장한 문서의 수
# ex) df(과일이)=1, df(바나나)=2
# idf(d,t): df(t)에 반비례하는 수
# idf(d,t) = log( n / (1+df(t)) )
# 
# idf=n/df(t)
#    =4/2
# n:총 문서의 개수(문서1~4번까지, 4)
# 
# ex) n=1000000 (문서의 개수가 100만개)
# 1) 로그를 사용하지 않았을때 idf?
#   idf(d,t)=n/df(t)
#   n=1000000
# 단어t     df(t)     idf(d,t)  
# word1       1       1000000
# word2      100       10000
# ...
# word5    1000000       1
# 2) 로그를  사용했을때 idf?(log의 밑을 10이라고 가정)
#   idf(d,t)=log(n/(df(t)+1))
#   n=1000000
#   단어t          df(t)     idf(d,t)  
#   word1(nlp)       1          6
#   word2            100        4
#   ...
#   word5(the)    1000000       0
# 
# tf-idf=tf*idf
# ifidf는 모든 문서에서 자주 등장하는 단어는 중요도가 낮다고 판단.
# 특정 문서에만 자주 등장하는 단어는 중요도가 높다고 판단.
# tfidf값이 낮으면 중요도가 낮다는 것. 높으면 중요가 높다는 것.
# ex) the 단어는 모든 문서에서 자주 등장
# the의 tfidf는 다른 단어의 tfidf보다 낮아지게 된다.
# 
# 
#      과일이 길고   노란 먹고 바나나 사과 싶은 저는 좋아요
# 문서1    0      0    0    1     0     1    1    0     0
# 문서2    0      0    0    1     1     0    1    0     0
# 문서3    0      1    1    0     2     0    0    0     0
# 문서4    1      0    0    0     0     0    0    1     1
# 
# tf(d,t):특정 문서 d 내에서 t 단어가 발생한 횟수
# 
# tf(문서1,과일이)=0
# DTM 행렬의 각 요소값은 tf값
# 
# idf에서는 자연로그(e=2.718...)사용(ln)
# idf(d,t)=log(n/(df(t)+1))
# 
# '과일이'의 idf? ln(4/(1+1))=ln(2)=0.69
# ...
# '먹고' 또는 '바나나'의 idf? ln(4/(2+1))=ln(4/3)=0.28
# ...
# 
# 
# tfidf
#     과일이       길고	  노란	 먹고	 바나나 	사과 	싶은	 저는	 좋아요
# 
# 문서1	0	          0	    0	  0.287682	0	0.693147	0.287682	0	0
# 문서2	0	          0	    0	  0.287682	0.287682	0	0.287682	0	0
# 문서3	0	          0.693147	0.693147	0	0.575364	0	0	0	0
# 문서4	0.693147	  0	0	0	0	0	0	0.693147	0.693147
# 
# 
# 
# 결론적으로,
# tfidf값을 통해서 알 수 있는것.
# 1) 특정 단어를 가장 중요하게 다루는 문서를 알 수 있음
# 2) 각 문서들마다 중요한 단어를 알 수 있음
# 
# tfidf값을 통해서 할 수 있는것
# 1) cos유사도 구할 수 있음


















