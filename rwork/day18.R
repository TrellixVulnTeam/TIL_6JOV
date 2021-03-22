mydata<-read.csv('examscore.csv',encoding = 'euc-kr')
x<-6:10
sum(x)/length(x)
mean(x)

mean(mydata$midterm)


hist(mydata$midterm,
     xlab='중간고사 성적',
     ylab='빈도',
     main='중간고사 성적 분포')


abline(v=mean(mydata$midterm),col='red')
abline(v=median(mydata$midterm),col='blue')

#
mydata$midterm[20]<-100
mydata$midterm[22]<-100



hist(mydata$midterm,
     xlab='중간고사 성적',
     ylab='빈도',
     main='중간고사 성적 분포')


abline(v=mean(mydata$midterm),col='red')
abline(v=median(mydata$midterm),col='blue')





#
quantile(mydata$midterm)

# 0%    25%    50%    75%   100% 
# 24.00  35.25  44.50  51.75 100.00 

quantile(mydata$midterm)[2]



#분산, 표준편자
set.seed(1234)
x<-sample(1:10,6)
x

xBar<-mean(x)
x
sum((x-xBar)^2)/(length(x)-1)

#표준편차
sqrt(sum((x-xBar)^2)/(length(x)-1))
sd(x)

#최빈수: 데이터 셋에서 가장 빈도가 높은 수 
x<-c(1,3,9,7,1,2,2,5,3,3,3)
result<-table(x)
result


names(sort(-result)[1])







mydata<-read.csv('examscore.csv',encoding = 'euc-kr')

mycorr<-cor(mydata$midterm, mydata$final)
mycorr

n<-length(mydata$midterm)
n
xbar<-mean(mydata$midterm)
ybar<-mean(mydata$final)
sx<-sd(mydata$midterm)  #표준편차
sy<-sd(mydata$final)
zx<-(mydata$midterm-xbar)/sx
zy<-(mydata$final-ybar)/sy

#공분산: 2개의 확률변수의 상관정도 
#양수:2개의 변수 중 하나의 값이 상슿하는 경향일때 다른 값도 상승하는 경향의 상관관계
#음수:2개의 변수 중 하나의 값이 상슿하는 경향일때 다른 값도 하강하는 경향의 상관관계
#공분산이 0보다 크면 양의 상관관계이고 공분산이 0보다 작으면 음의 상관관계, 0이면 상관이 없다는 뜻이다. 즉 상관관계가 양인지 음인지를 수치로 나타낸 것이다. 
rxy<-sum(zx*zy)/(n-1)
rxy  #양의상관관계

dev.off()

plot(mydata$midterm, mydata$final,
     xlab='중간',
     ylab='기말',
     main='시험점수')

title(sub=paste('상관관계수 : ',round(mycorr,4)),adj=1,col.sub='red')
abline(v=xbar)
abline(h=ybar)


#표준점수 분포
dev.off()
plot(zx, zy,
     xlab='중간',
     ylab='기말',
     main='시험점수')

title(sub=paste('상관관계수 : ',round(mycorr,4)),adj=1,col.sub='red')
#표준편차는 0이 평균임.
abline(v=0)
abline(h=0)



zx
zy

#면적
zx*zy


sign(zx*zy)  #양수는1, 음수는 -1로 나옴


#양수는 빨, 음수는 파로 시각과 다시 해보기

dev.off()

dev.off()
plot(zx, zy,
     xlab='중간',
     ylab='기말',
     main='시험점수',
     col=c('blue','red')[as.factor(sign(zx*zy))])  #factor는 -1,1순으로 구분됨



title(sub=paste('상관관계수 : ',round(mycorr,4)),adj=1,col.sub='red')
abline(v=0)
abline(h=0)


as.factor(sign(zx*zy))

#c('blue','red')[as.factor(sign(zx*zy))]


abs(zx*zy)




#
dev.off()

plot(zx, zy,
     cex=abs(zx*zy),   #멀리 떨어질수록 점의 크기 더 크게 
     xlab='중간',
     ylab='기말',
     main='시험점수',
     col=c('blue','red')[as.factor(sign(zx*zy))])  #factor는 -1,1순으로 구분됨

title(sub=paste('상관관계수 : ',round(mycorr,4)),adj=1,col.sub='red')
abline(v=0)
abline(h=0)








#회귀분석
install.packages('datarium')   #help에서 marketing 검색
library(datarium)
data('marketing')
marketing



dev.off()

plot(mydata$midterm, mydata$final,
     xlab='중간',
     ylab='기말',
     main='시험점수')

abline(5,1)#직선, y절편(교차점):5 , 기울기:1
  abline(-15,1.5, col='red')
#빨간색 직선이 데이터를 더 잘 설명함


#y=1*x+5

#기말점수(y)=1*c(50,60,100,90,85)+5



#회기 직선을 그리는 방법
#주어진 y데이터를 x데이터로 예측했을 경우, 
#예측값과 실제값 사이에서 차이의 제곱들의 합이
#가장 작은 직선을 선택하면됨

#잔차(residual):예측값과 실제값 사이에서 차이
#잔차 제곱의 합: residual sum of square(rss)


#중간고사(x)를 모델에 입력했을 때 기말고사 점수 예측(yhat)
#잔차=실제값(y)- 예측값(yhat)
#데이터가 30개니깐 잔차는 1~30, 이걸 다 더 함(잔차의 합)= 잔차의 합의 제곱근
#잔차의 합을 최소로 갖는 y절편과 기울기를 찾는 것 

rss<-function(data,lineInfo){
  x<-data[,1]  #mid 
  y<-data[,2]  #final
  intercept<-lineInfo[1]  #y절편
  slope<-lineInfo[2]  #기울기
  yhat<-intercept+slope*x
  result<-sum((y-yhat)^2)
  result
}

rss(mydata[,3:4],c(5,1))  #6421
rss(mydata[,3:4],c(-15,1.5))  #8293.25



#우리의 목표: 잔차제곱의 합을 최소로 하는 y절편과 기울기를 찾는 것


#기울이가 1이고 y절편이 5인 직선을 회귀 직선으로 
#사용한다면,  mydata[,3:4]에 대한 rss를 구해보자.

#optim함수: y절편과 기울기를 변경해가면서 최적의 값을 찾아내는 함수#
#par가 lineInfo에 들어가고 data가 data에 들어감(par값을 바꾸면서 가장 작은 기울기를 갖는 y절편과 기울기 값을 par에 저장하고 
#value값에는 )

#최적의 회귀직선: yhat=13.88+0.98x

result<-optim(par=c(1,1), fn=rss, data=mydata[,3:4])  
result$par
result$value
result

#[1] 13.8833436 :절편  0.8967623:기울기
dev.off()

plot(mydata$midterm, mydata$final,
     xlab='중간',
     ylab='기말',
     main='시험점수')
abline(5,1)  #y절편이 5, 기울기:1
abline(-10,1.5,col='red')
#최적의 회귀직선
abline(result$par,col='blue')
#최적의 회귀식: yhat=13.88+0.98x



#2. 회귀모델 작성
lm(final~midterm, mydata)

#3. 통계학자들이 찾아낸 회귀모델 수식
#기울기= 상관계수 *표준편차(y) / 표준편차(x)
x<-mydata$midterm
y<-mydata$final
#둘의 상관계수
cor(x,y)

b<-cor(x,y)*sd(y)/sd(x)

#절편= y평균-기울기*x평균
mean(y)-b*mean(x)

 







mydata<-read.csv('examscore.csv')



# yhat=기울기 * x(중간)+ 절편 + 노이즈
# 노이즈? 기말고사 점수들에 잡음이 섞여있다고 가정




result<-lm(final~midterm, mydata)
attributes(result)


#직선 정보
result$coefficients  #기울기, 절편


dev.off()
plot(mydata$midterm, mydata$final,
     xlab='중간',
     ylab='기말',
     main='시험점수')
abline(result$coefficients)





summary(result)

result$call




#중간소가 점수를 ->회귀모델->예측결과르 ㄹ확인하고자 할때
result$fitted.values


#잔차(예측갑소가 실제값사이의 차이)
#잔차= 실제값(y=final)-예측값(yhat=result$fitted.values)
mydata$final-result$fitted.values
#or
result$residuals




summary(result$residuals)





result


plot(result)



dev.off()
par(mfrow=c(2,2))

plot(result)




dev.off()






#성별 고려 
head(mydata)


plot(mydata$midterm, mydata$final,
     col=c('red','blue')[as.factor(mydata$gender)],
     pch=c(16,17)[as.factor(mydata$gender)],  #16:세모, 17:원
     xlab='중간',
     ylab='기말',
     main='시험점수')

#20,80좌표 기준으로 범례상자 만들기
legend(20,80,
       legend=c('여자','남자'),
       col=c('red','blue'),
       pch=c(16,17))


dataFemale<-mydata[mydata$gender=='F',]

dataMale<-mydata[mydata$gender=='M',]


#회귀모델: lm(종속~ 독립, 데이터)
model1<-lm(final~midterm, dataFemale)
model2<-lm(final~midterm, dataMale)

model1$coefficients  #여학생

model2$coefficients  #남학생





plot(mydata$midterm, mydata$final,
      col=c('red','blue')[as.factor(mydata$gender)],
      pch=c(16,17)[as.factor(mydata$gender)],  #16:세모, 17:원
      xlab='중간',
      ylab='기말',
      main='시험점수')

#20,80좌표 기준으로 범례상자 만들기
legend(20,80,
       legend=c('여자','남자'),
       col=c('red','blue'),
       pch=c(16,17))

abline(model1$coefficients, col='red')
abline(model2$coefficients, col='blue')




#예측함수: predict
#중간고사 50점인 여학생의 기말고사 점수를 예측
#1
model1
predict(model1, data.frame(midterm=50))

#2
param<-as.numeric(model1$coefficients)

param[1]+50*param[2]







#다중회귀분석(성별, 중간고사-->기말예측회귀모델)

model3<-lm(final~midterm+gender, mydata)
model3

#기말고사= intercept+중간기울기 * 중간점수+성별기울기* 성별+노이즈
#젠더가 자체적으로 숫자로 계산되서 나옴

#c(0,1)[as.factor(mydata$gender)] 과정을 거쳐서, 
#F->0, M->1로 수치변환


#여학생, 중간고사 40점, 기말고사?
#기말고사= intercept+중간기울기 * 중간점수+성별기울기* 성별+노이즈
#기말고사= 18.9774+0.8808*40


par<-as.numeric(model3$coefficients)
par

yhat<-par[1]+par[2]*40+par[3]*0
yhat
#54점 예상

#or

predict(model3, data.frame(midterm=40, gender='F'))


#남학생?
yhat<-par[1]+par[2]*40+par[3]*1
yhat
#or
predict(model3, data.frame(midterm=40, gender='M'))




