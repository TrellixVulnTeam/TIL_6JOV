#### 인터넷에 있는 데이터 읽어오기 ####
url <- 'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
mushroom <- read.csv(file=url, header=F, na.strings='?')
str(mushroom)


#### 정답 데이터 분리 ####
mushroom.answer <- mushroom[,1]
mushroom[,1] <- NULL


#### 각 컬럼 별 NA 값 확인 ####
apply(mushroom, 2, function(x) sum(is.na(x))) # V12 2480


#### V12 결측값 채우기 1 ####
# 이후에 나오는 함수에서 names로 찾으려고 factor화
mushroom$V12 <- factor(mushroom$V12)

# NA 행과 나머지 행 인덱스로 나누기 
na.idx <- which(is.na(mushroom[,11]))
compare.idx <- which(!is.na(mushroom[,11]))

# 값 참조할 데이터 만들기
library(dplyr)
set.seed(1234)
compare <- sample_frac(mushroom[-na.idx,] , size=0.3) 

# 값 비교할 컬럼들 
#na: stalk-root
t.cols <- c(9,10,12) # stalk-shape, stalk-surface-below-ring, stalk-surface-above-ring

# 주의: 아아주 오래 걸림 
for (i in na.idx){
  idx <- compare.idx %>%
    sapply(function(x) sum(compare[x,t.cols]==mushroom[i,t.cols])) %>%
    order(decreasing=T) %>%
    head(5)
  mushroom[i,11] <- names(which.max(table(compare$V12[idx])))
  print(i)
}


#### 문자 --> 수치 변환 ####
#### chr 변수를 num factor로 변경 ####
head(mushroom)
toNum <- function(x) {
  f <- as.numeric(factor(x, labels=(1:length(unique(na.omit(x))))))
}
mush.num <- as.data.frame(apply(mushroom, 2, toNum))
mush.num


#### 원핫인코딩 ####

mush.encoded <- data.frame(1:8124)
head(mush.encoded)


# 0*n 으로 이루어진 리스트 만들기 
for(i in 1:ncol(mush.num)){
  n <- max(mush.num[,i])
  mush.zero <- mapply(rep, rep(0, n), nrow(mush.num))
  
  # 1, 0 채우기    
   for (j in 1:8124){
    mush.zero[j, mush.num[j,i]] <- 1
  }
  mush.zero <- as.data.frame(mush.zero)
  names(mush.zero)<- paste(i, rep(1:n), sep='-')
  mush.encoded <- cbind(mush.encoded, mush.zero)
}
# mush.encoded[,1] <- NULL

str(mush.encoded)


#### train/test 분할 ####
set.seed(1234)
idx <- sample(1:8124, 8124*0.7)
train <- mush.encoded[idx,]
test <- mush.encoded[-idx,]

train_label <- mushroom.answer[idx]
test_label <- mushroom.answer[-idx]


#### 모델 생성 & 결과 확인 ####
v <- vector()
for (i in seq(1, 25, 2)) {
  pred <- knn(train, test, cl=train_label, k=i)
  v <- c(v, round(sum(pred==test_label)/length(pred), digits=3))
}
names(v) <- paste('k=',seq(1, 25, 2),sep='')
v
# k=1   k=3   k=5   k=7   k=9  k=11  k=13  k=15  k=17  k=19  k=21  k=23  k=25 
# 1.000 1.000 1.000 1.000 0.998 0.998 0.998 0.998 0.997 0.997 0.997 0.997 0.997