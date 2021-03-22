# 패키지/파일 로드 ####
library(tm) 
library(stringr)
library(SnowballC)
library(wordcloud)
library(e1071) 
library(gmodels)

emailRaw <- read.csv('sms_spam_ansi.txt', header = F, encoding='UTF-8')
colnames(emailRaw) <- c('type', 'text')

# 분류 데이터 factor로 변경 ####
emailRaw$type <- factor(emailRaw$type)

# str(emailRaw)
# 'data.frame':	22 obs. of  2 variables:
#   $ type: Factor w/ 2 levels "ham","spam": 2 2 2 2 2 1 1 1 1 1 ...
# $ text: chr  "The IRS is Trying to Contact You" "You Have a Refund Coming" "Verify Your Bank Account" "You Have a Package Delivery" ...

# Corpus 생성 ####
eCorpus <- VCorpus(VectorSource(emailRaw$text))

# 알파벳 이외의 문자 모두 제거
eCorpusClean <- tm_map(eCorpus, 
                       content_transformer(
                         function(x, pat) gsub('[^[:alpha:]]+', ' ', x)))

# 소문자 변환, 길이 2 미만/불용어/공백 제거, 어간 추출 
eCorpusClean <- tm_map(eCorpusClean, content_transformer(tolower))
eCorpusClean <- tm_map(eCorpusClean, removeWords, '[[:alpha:]]{1}')
eCorpusClean <- tm_map(eCorpusClean, removeWords, stopwords())
eCorpusClean <- tm_map(eCorpusClean, stemDocument)
eCorpusClean <- tm_map(eCorpusClean, stripWhitespace)


# DTM 생성 ####
eDtm <- DocumentTermMatrix(eCorpusClean)
# > eDTM
# <<DocumentTermMatrix (documents: 22, terms: 139)>>
#   Non-/sparse entries: 156/2902
# Sparsity           : 95%
# Maximal term length: 11
# Weighting          : term frequency (tf)


# train/test set 분할 ####
set.seed(1234)
idx <- sample(1:nrow(eDtm), size=nrow(eDtm)*0.7)

eTrain <- eDtm[idx,]
eTest <- eDtm[-idx,]

eTrainLabels <- emailRaw$type[idx]
eTestLabels <- emailRaw$type[-idx]


# findFreqTerms 함수로 최소 등장 횟수 지정한 단어 뽑기 ####
findFreqTerms(eTrain,2) # 6
findFreqTerms(eTrain,3) # 2
findFreqTerms(eTrain,4) # 1

eFreqWords2 <- findFreqTerms(eTrain,2)
eFreqWords3 <- findFreqTerms(eTrain,3)
eFreqWords4 <- findFreqTerms(eTrain,4)


# wordcloud 시각화 ####
wordcloud(eCorpusClean, min.freq=50, random.order=F, colors=brewer.pal(3,'RdPu'))

spam <- subset(emailRaw, type=='spam')
ham <- subset(emailRaw, type=='ham')

wordcloud(spam$text, min.freq=50, random.order = F, colors=brewer.pal(3,'RdPu'))
wordcloud(ham$text, min.freq=50, random.order = F, colors=brewer.pal(3,'RdPu'))


# 횟수 => yes/no 변경 ####
eTrain1 <- apply(eTrain, 2, function(x){ifelse(x>0, 'yes', 'no')})
eTest1 <- apply(eTest, 2, function(x){ifelse(x>0, 'yes', 'no')})


# 단어 최소 횟수 다른 데이터 생성 ####
eTrain2 <- eTrain1[,eFreqWords2] 
eTest2 <- eTest1[,eFreqWords2]

eTrain3 <- eTrain1[,eFreqWords3] 
eTest3 <- eTest1[,eFreqWords3]

eTrain4 <- eTrain1[,eFreqWords4] 
eTest4 <- eTest1[,eFreqWords4]

# 나이브 베이즈 모델 만들기 ####
eClassifier1 <- naiveBayes(eTrain1, eTrainLabels)
eClassifier2 <- naiveBayes(eTrain2, eTrainLabels)
eClassifier3 <- naiveBayes(eTrain3, eTrainLabels)
eClassifier4 <- naiveBayes(eTrain4, eTrainLabels)

# 테스트 데이터 모델에 입력하여 분류 결과 생성
eTestPred1 <- predict(eClassifier1, eTest1)
eTestPred2 <- predict(eClassifier2, eTest2)
eTestPred3 <- predict(eClassifier3, eTest3)
eTestPred4 <- predict(eClassifier4, eTest4)

# 정확도 평가 
CrossTable(eTestPred1, eTestLabels) # 정확도: 5/7, spam을 spam이라고 분류: 1/3
CrossTable(eTestPred2, eTestLabels) # 정확도: 4/7, spam을 spam이라고 분류: 1/3
CrossTable(eTestPred3, eTestLabels) # 정확도: 4/7, spam을 spam이라고 분류: 1/3
CrossTable(eTestPred4, eTestLabels) # 정확도: 4/7, spam을 spam이라고 분류: 0/3 (모두 ham으로 분류)
#3. 각 문서 간 코사인 유사도 (6개) -> 최대값에 해당되는 문서쌍을 출력 

txt <- c('먹고 싶은 사과', '먹고 싶은 바나나', '길고 노란 바나나 바나나', '저는 과일이 좋아요')
txtCorpus <- VCorpus(VectorSource(txt))
txtDtm <- DocumentTermMatrix(txtCorpus,control = list(wordLengths=c(2, Inf)))
txtMat <- as.matrix(txtDtm)
txtMat
# txtMat
# Docs 과일이 길고 노란 먹고 바나나 사과 싶은 저는 좋아요
# 1      0    0    0    1      0    1    1    0      0
# 2      0    0    0    1      1    0    1    0      0
# 3      0    1    1    0      2    0    0    0      0
# 4      1    0    0    0      0    0    0    1      1


txtCosine <- vector()
for (i in 1:4) {
  for (j in 1:4){
    a <<- txtMat[i,]
    b <<- txtMat[j,]
    dotP <<- sum(a*b)
    norm1 <<- sqrt(sum(ifelse(a>0, a^a, 0)))
    norm2 <<- sqrt(sum(ifelse(b>0, b^b, 0)))
    cosSim <<- ifelse(dotP==0 | (norm1*norm2)==0,0,dotP/(norm1*norm2))
    txtCosine <<- c(txtCosine, cosSim)
  }
}

txtCosMat <- matrix(txtCosine, 4,4)
txtCosMat
# > txtCosMat
#           [,1]      [,2]      [,3] [,4]
# [1,] 1.0000000 0.6666667 0.0000000    0
# [2,] 0.6666667 1.0000000 0.4714045    0
# [3,] 0.0000000 0.4714045 1.0000000    0
# [4,] 0.0000000 0.0000000 0.0000000    1
#1에 가까울수록 유사도 높음

