# 1. 단어 길이가 2미만인 단어는 제거
# 
# 2.findFreqTerms함수에서 최소 등장 횟수를 변경하여 모델
# 
# - 5보다 더 작은 값으로 수정 -> 정확도 비교
# 
# 
# 
# 3.각 문서간 코사인 유사도(6개) -> 최대값에 해당되는 문서쌍을 출력

# 코퍼스

# 문서1:먹고 싶은 사과

# 문서2:먹고 싶은 바나나

# 문서3:길고 노란 바나나 바나나

# 문서4:저는 과일이 좋아요

# 

# DTM(4*9) 문서-단어 행렬

# 과일이 길고 노란 먹고 바나나 사과 싶은 저는 좋아요

# 문서1 0 0 0 1 0 1 1 0 0

# 문서2 0 0 0 1 1 0 1 0 0

# 문서3 0 1 1 0 2 0 0 0 0

# 문서4 1 0 0 0 0 0 0 1 1


email<-read.csv('email_title.txt',header = FALSE)

email$V1<-factor(email$V1)
str(email)
library(tm)
emailCorpus<-VCorpus(VectorSource(email$V2))



over2<-function(x){
  gsub('\\b[[:alpha:]] ',' ',x)
}
over2('I am a boy')



CorpusLen<-tm_map(emailCorpus,content_transformer(over2))

CorpusNum<-tm_map(CorpusLen,removeNumbers)

CorpusPunct<-tm_map(CorpusNum,removePunctuation)

CorpusLower<-tm_map(CorpusPunct,content_transformer(tolower))

CorpusUseless<-tm_map(CorpusLower,removeWords,stopwords())

CorpusRMspace<-tm_map(CorpusUseless,stripWhitespace)
#어근화

library(SnowballC)
CorpusFinal<-tm_map(CorpusRMspace,stemDocument,'english')


#wordcloud 시각화
library(wordcloud)
wordcloud(CorpusFinal,min.freq=20,random.order = F)
wordcloud(CorpusFinal,min.freq=20,random.order = F,colors =brewer.pal(5,'Greens'))
wordcloud(CorpusFinal,min.freq=20,random.order = F,colors =brewer.pal(5,'YlGn'))
wordcloud(CorpusFinal,min.freq=20,random.order = F,colors =brewer.pal(5,'RdYlGn'))


#DTM
emailDTM<-DocumentTermMatrix(CorpusFinal)
str(emailDTM)

Freqwords2<-findFreqTerms(emailDTM,2)
Freqwords3<-findFreqTerms(emailDTM,3)
Freqwords5<-findFreqTerms(emailDTM,5)


#colnames(emailDTM)
set.seed(1234)
sample_idx<-sample(1:22,22*0.7,replace = F)

dtmFreqTrain2<-emailDTM[-sample_idx,Freqwords2]
dtmFreqTest2<-emailDTM[sample_idx,Freqwords2]

dtmFreqTrain3<-emailDTM[-sample_idx,Freqwords3]
dtmFreqTest3<-emailDTM[sample_idx,Freqwords3]

dtmFreqTrain5<-emailDTM[-sample_idx,Freqwords5]
dtmFreqTest5<-emailDTM[sample_idx,Freqwords5]


transCount<-function(x){
  x<-ifelse(x>0,'Yes','No')
}
emailTrain2<-apply(dtmFreqTrain2,2,transCount)
emailTest2<-apply(dtmFreqTest2,2,transCount)

emailTrain3<-apply(dtmFreqTrain3,2,transCount)
emailTest3<-apply(dtmFreqTest3,2,transCount)

emailTrain5<-apply(dtmFreqTrain5,2,transCount)
emailTest5<-apply(dtmFreqTest5,2,transCount)

str(emailTrain2)
emailTrain2[1]

Train_label<-email$V1[-sample_idx]
Test_label<-email$V1[sample_idx]

#나이브 베이즈
#모델 생성
library(e1071)

BayesClassifier21<-naiveBayes(emailTrain2,Train_label)
BayesClassifier22<-naiveBayes(emailTrain2,Train_label,laplace=1)


BayesClassifier31<-naiveBayes(emailTrain3,Train_label)
BayesClassifier32<-naiveBayes(emailTrain3,Train_label,laplace=1)

BayesClassifier51<-naiveBayes(emailTrain5,Train_label)
BayesClassifier52<-naiveBayes(emailTrain5,Train_label,laplace=1)

BayesClassifier21

#예측
Predict_label21<-predict(BayesClassifier21,emailTest2)
Predict_label22<-predict(BayesClassifier22,emailTest2)

Predict_label31<-predict(BayesClassifier31,emailTest3)
Predict_label32<-predict(BayesClassifier32,emailTest3)

Predict_label51<-predict(BayesClassifier51,emailTest5)
Predict_label52<-predict(BayesClassifier52,emailTest5)
BayesClassifier21
emailTest2

#교차표 검증
library(gmodels)
CrossTable(Predict_label21,Test_label)
CrossTable(Predict_label22,Test_label)


CrossTable(Predict_label31,Test_label)
CrossTable(Predict_label32,Test_label)


CrossTable(Predict_label51,Test_label)
CrossTable(Predict_label52,Test_label)



#코사인유사도
library(stringr)
cos<-c("먹고 싶은 사과","먹고 싶은 바나나","길고 노란 바나나 바나나","저는 과일이 좋아요")
words<-unique(unlist(str_split(cos,' ')))

ncols<-length(words)
dtm1<-matrix(0,4,ncols)
colnames(dtm1)<-words
dtm1
t(dtm1)

for(i in 1:4){
  words_l=str_split(cos,' ')[[i]]
  print(words_l)
  for(word in words_l){
    if(word %in% words){
      dtm1[i,word]=dtm1[i,word]+1
    }
  }
}

norms<-apply(dtm1,1,FUN=function(x){
  sqrt(sum(x^2))
})

mat<-matrix(nrow=4,ncol=4)
for(i in 1:4){
  div<<-norms*norms[i]
  up<<-sum(t(dtm1)*t(dtm1)[,i])
  mat[i,]<-up/div
}



# > norms
# [1] 1.732051 1.732051 2.449490 1.732051
#      문서1    문서2   문서3     문서4

which(mat==max(mat))
#(1,2),(2,2),(4,2)


#      과일이 길고   노란 먹고 바나나 사과 싶은 저는 좋아요
# 문서1    0      0    0    1     0     1    1    0     0
# 문서2    0      0    0    1     1     0    1    0     0
# 문서3    0      1    1    0     2     0    0    0     0
# 문서4    1      0    0    0     0     0    0    1     1
