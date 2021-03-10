#1.데이터 확인

url<-'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
download.file(url=url,destfile = './data/mushroom.csv')



df<-read.csv('./data/mushroom.csv',na.strings = '?',header = F)

df
head(df,10)
str(df)
summary(df)
nrow(df)
ncol(df)


##결측값 확인

library(Amelia)
missmap(df,col = c('red','grey'))  #v12에 결측값 존재

sum(is.na(df$e.1)) #2480

# 1열: label / 나머지 열: feature


#2.데이터 전처리

#2-1 결측값 처리(V12=stalk-root)


library(ggplot2)

#V12 데이터 분포 확인
table(df[,c('V12')])
# b      c    e    r 
# 3776  556 1120  192 

#V12를 V1~V23까지  비율 파악 후 가장 분류가 잘되는 변수 고르기
compare.v12 <-function(x){
  print(proportions(table(df[,c('V12',x)]),2))
}


for (i in seq(1:23)){
  compare.v12(paste('V',i,sep=''))
}
proportions(table(df[,c('V12','V6')]),2)




# V12 X V13

#                      V13
# V12   f          k          s          y
# b 0.30434783 0.97297297 0.61456103 0.66666667
# c 0.00000000 0.02702703 0.13704497 0.33333333
# e 0.69565217 0.00000000 0.19700214 0.00000000
# r 0.00000000 0.00000000 0.05139186 0.00000000

ggplot(df,aes(x=df$V13,fill=df$V12))+geom_bar()

#V12 X V14
#                         V14
# V12     f          k          s          y
# b 0.30434783 1.00000000 0.64785553 0.06349206
# c 0.00000000 0.00000000 0.14446953 0.17460317
# e 0.69565217 0.00000000 0.20767494 0.00000000
# r 0.00000000 0.00000000 0.00000000 0.76190476

ggplot(df,aes(x=df$V14,fill=df$V12))+geom_bar()


# V13,V14 -> V12 분류하기

#f -> e  (b의 수가 가장 많음에도 e의 비율이 더 높음)

#k,s -> b 

# y -> b or r
# =>r으로 분류 (v13에서 y에 해당하는 수가 적기 때문에 0.66666667은 무의미하다고 판단)
table(df$V13)
# f    k    s     y 
# 552 2372 5176   24 
table(df$V14)
# f    k    s    y 
# 600 2304 4936  284 


for(i in seq(1:nrow(df))){
  if(is.na(df$V12[i])){
    if(df$V14[i]=='f'){
      df$V12[i]<-'e'
    }
    else if(df$V14[i]%in%c('k','s')){
      df$V12[i]<-'b'
    }
    else if(df$V14[i]=='y'){
      df$V12[i]<-'r'
    }
  }
}

sum(is.na(df$V12))

#결측값 채운 후 결과
table(df$V12)
#   b    c    e    r 
# 6176  556 1168  224 



#2-2 one hot encoding


for(i in seq(2,23,)){
  for (j in seq(1,length( unique( df[i][,1] ) ))){
    df[paste('V',i,'_',j,sep='')]<-ifelse(df[paste('V',i,sep='')]==unique(df[i])[j,1],1,0)
  } 
}

summary(df)
head(df,10)


# 3. train, test 분할 & knn  모델링
set.seed(1234)
idx<-sample(1:nrow(df),nrow(df)*0.7) 

train<-df[idx,c(24:ncol(df))]
test<-df[-idx,c(24:ncol(df))]

train
summary(train)
summary(test)
nrow(train)
nrow(test)

train_labels <-df[idx,1]
test_labels <-df[-idx,1]

length(train_labels)
length(test_labels)

library(class)
test_pred<-knn(train=train,test=test,
               cl=train_labels,k=3)

sum(test_labels==test_pred)/length(test_labels) # 1 ...?