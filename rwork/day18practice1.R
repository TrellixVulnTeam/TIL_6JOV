# 1.cars
# 임의의 속도가 입력되었을때 예상되는 제동거리를 출력 회귀모델 작성
# 
cars
str(cars)
plot(cars)
res<-lm(dist~speed,cars)
res
# Coefficients:
#(Intercept)     speed  
# -17.579        3.932  

plot(cars$speed,cars$dist,
     xlab='속도',
     ylab='제동거리')
abline(res$coefficients)

distance<-function(x){
  predict(res,data.frame(speed=x))
}

distance(30)
distance(70)

# 2.marketing(70:30비율, 트레인/테스트)

install.packages("datarium")
library(datarium)
data("marketing")
str(marketing)

set.seed(1234)
index<-sample(1:nrow(marketing),nrow(marketing)*0.7,replace = F)

marketingTrain <-marketing[index,]
marketingTest<-marketing[-index,]
nrow(marketingTrain)
nrow(marketingTest)

plot(marketing$youtube,marketing$sales)
abline(lm(sales~youtube,marketing))

plot(marketing$facebook,marketing$sales)
abline(lm(sales~facebook,marketing))

plot(marketing$newspaper,marketing$sales)
abline(lm(sales~newspaper,marketing))


head(marketing)
marketingTrainLabels <- marketing[index,4]
marketingTestLabels<-marketing[-index,4]


result<-lm(sales~youtube+facebook+newspaper,marketingTrain)
result$coefficients
# (Intercept)       youtube      facebook     newspaper 
# 3.3980812461  0.0460825893  0.1834389028 -0.0003929324 
dev.off()
par(mfrow=c(2,2))
plot(result)


head(marketing)
pred<- function(x){
  Pred<-predict(result,data.frame(youtube=x[,1],facebook=x[,2],newspaper=x[,3]))
}

marketingTestPred<-pred(marketingTest)

dev.off()
plot(marketingTestPred,marketingTestLabels,
     xlab='예측값',
     ylab='실제값',
     main='Test 예측값과 실제값 비교',)
abline(a=0,b=1)

dev.off()
plot(marketingTestLabels,type='l',
     ylab='sales',
     main='예측값, 실제값 비교')
lines(marketingTestPred,col='red')

#MSE 
mse<-sum((marketingTestPred-marketingTestLabels)^2)/length(marketingTestPred) 
mse #3.120579

#R^2
1-(mse/var(marketingTestLabels)) #0.9356762 
