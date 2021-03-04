# 1. mtcars데이터 weight열 추가, 무게가 중위수보다 큰 자동차는 heavy, 그렇지 않은 자동차는 light를 저장
# - 각 종류별 데이터 건수 출력, 비율
car<-mtcars
car$weight<-'light'
car$weight[car$wt>median(car$wt)]<-'heavy'
car
#or
mtcars$weight <- ifelse(mtcars$wt>median(mtcars$wt), 'heavy', 'light')
#건수
table(car$weight)
#비율

table(car$weight)/nrow(car)

# 2. mtcars 데이터셋 열들이 왼쪽에서 오른쪽으로 오름차순으로 배치되도록 작성

index<-sort(colnames(car))
car[,index]
#or
mtcars2<-mtcars[,order(colnames(mtcars))]
head(mtcars2)
#or
order(names(mtcars))
mtcars[,order(names(mtcars))]
# 3. iris데이터에서 70% 데이터를 무작위 표본추출
str(iris[sample(1:nrow(iris),nrow(iris)*0.7),])
#or
set.seed(1)
idx<-sample(1:nrow(iris),nrow(iris)*0.7)
iris[idx,]
# 4. ggplot2 패키지에는 미국 동북중부 437개 지역의 인구통계 정보를 담은 midwest라는 데이터가 포함되어 있음. 
# midwest 데이터를 사용하여,
# 불러오기 : midwest<-as.data.frame(ggplot2::midwest)
# - ggplot2 의 midwest 데이터를 데이터 프레임 형태로 불러와서 데이터의 특성을 파악
midwest<-as.data.frame(ggplot2::midwest)
head(midwest)
summary(midwest)
str(midwest)
View(midwest)
# - poptotal(전체 인구)을 total 로, popasian(아시아 인구)을 asian 으로 변수명을 수정
midwest<-rename(midwest,c(total=poptotal,asian=popasian))

# - total, asian 변수를 이용해 '전체 인구 대비 아시아 인구 백분율' 파생변수 생성
midwest$perasian<-midwest$asian/midwest$total
midwest
# - 아시아 인구 백분율 전체 평균을 구하고, 평균을 초과하면 "large", 그 외에는 "small"을 부여하는 파생변수 생성
midwest$average.asian<-'small'
midwest$average.asian[midwest$perasian>mean(midwest$perasian)]<-'large'
head(midwest)
#or
mean(per.asian)
size.asian<-ifelse(per.asian>mean(per.asian),"large","small")
# - "large"와 "small"에 해당하는 지역이 얼마나 되는지 빈도수를 출력
table(midwest$average.asian)


# 5. 타이타닉 데이터 분석
# -타이타닉 데이터 불러오기
titanic<-read.csv('train.csv',na.strings = '')
head(titanic)
# - 생존자 수, 사망자 수 출력
table(titanic$Survived)
#or
sum(titanic$Survived)
sum(!titanic$Survived)
#or
sum(!titanic$Survived)  #사망자 합계
sum(!titanic$Survived)  #사망자 합계
# - pclass, embarked 별 승객수 출력(비율)
table(titanic$Pclass)/nrow(titanic)
table(titanic$Embarked)/nrow(titanic)
#or
pclass.table <- as.data.frame(table(titanic$Pclass))
colnames(pclass.table) <- c("pclass","num")
pclass.table$ratio <- round((pclass.table$num / nrow(titanic)), digits = 3)
pclass.table

embarked.table <- as.data.frame(table(titanic$Embarked))
colnames(embarked.table) <- c("embarked","num")
embarked.table$ratio <- round((embarked.table$num/nrow(titanic)), digits = 3)
embarked.table
#or(pop.table함수 사용)
mydata<-matrix(sample(100,15),ncol=3)
colnames(mydata)<-LETTERS[seq(1,3)]
mydata

rownames(mydata)<-sprintf("s-%d",seq(5))
mydata

prop.table(mydata)
sum(prop.table(mydata))
library(dplyr)
prop.table(mydata) %>% sum  #왼쪽 수행한 결과에 대해서 sum적용 

prop.table(mydata,1)  #margin을 1이라고 주면 행 단위로 비율 구함
prop.table(mydata,2)  #margin을 2이라고 주면 열 단위로 비율 구함

rowSums(prop.table(mydata,1))
prop.table(mydata,1) %>% rowSums

#or
proportions(titanic$Survived)
proportions(titanic$Embarked)

prop.table


# - Name에서 호칭 종류 출력, 호칭 종류 별 승객수 출력
name2<-unlist(strsplit(titanic$Name,split=' '))
name2<-grep('^[A-Z][a-z]+[.]',name2,value=TRUE)
table(name2)
# - 호칭을 아래와 같이 변경하여 name2열에 추가
# * "Mlle", "Ms", "Lady", "Dona" 는 "Miss"로 변경
# * "Mme"는  "Mrs"로 변경
# * "Capt", "Col", "Major", "Dr", "Rev", "Don",  "Sir", "the Countess", "Jonkheer"는 "Officer"로 변경
# * "Mr", "Mrs", "Miss"는 그대로
# * 나머지 호칭은 "Others"
miss <-c("Mlle.", "Ms.", "Lady.", "Dona.",'Miss.')
mrs <-c('Mme.','Mrs.')
officer<-c("Capt.", "Col.", "Major.", "Dr.", "Rev.", "Don.",  "Sir.", "the Countess.", "Jonkheer.")
mr<-c('Mr.')
titanic$name2<-'Others'

titanic[name2 %in% miss,]$name2 <-'Miss'
titanic[name2 %in% mrs,]$name2 <-'Mrs'
titanic[name2 %in% officer,]$name2 <-'Officer'
titanic[name2 %in% mr,]$name2 <-'Mr'

titanic

#or
name.words <- gsub(pattern = "Mlle|Ms|Lady|Dona", 
                   replacement = "Miss",
                   x = name.words)
name.words <- gsub(pattern = "Mme",
                   replacement = "Mrs",
                   x = name.words)
name.words <- gsub(pattern = "Capt|Col|Major|Dr|Rev|Don|Sir|Countess|Jonkheer",
                   replacement = "Officer",
                   x = name.words)
name.words <- gsub(pattern = "Master",
                   replacement = "Others",
                   x = name.words)
train$name2 <- name.words
train

# -name2 열을 factor로(5가지 범주) 변환
titanic$name2<-as.factor(titanic$name2)
str(titanic$name2)
# -name2열의 호칭별 인원수 출력
table(titanic$name2)
# -호칭 정보를 바탕으로 나이(Age) 결측값 대체(호칭 별 나이의 평균값)
head(titanic)
mean.miss<-mean(titanic$Age[titanic$name2=='Miss'],na.rm = T)
titanic$Age[titanic$name2=='Miss'&is.na(titanic$Age)]<-mean.miss

mean.mrs<-mean(titanic$Age[titanic$name2=='Mrs'],na.rm = T)
titanic$Age[titanic$name2=='Mrs'&is.na(titanic$Age)] <-mean.mrs

mean.officer<-mean(titanic$Age[titanic$name2=='Officer'],na.rm = T)
titanic$Age[titanic$name2=='Officer'&is.na(titanic$Age)] <-mean.officer

mean.mr<-mean(titanic$Age[titanic$name2=='Mr'],na.rm = T)
titanic$Age[titanic$name2=='Mr'&is.na(titanic$Age)] <-mean.mr

mean.others<-mean(titanic$Age[titanic$name2=='Others'],na.rm = T)
titanic$Age[titanic$name2=='Others'&is.na(titanic$Age)] <-mean.others
#or
lev <- levels(factor(titanic$name2))
lev
for(i in 1:length(lev)){
  mean.age <- mean(titanic$Age[titanic$name2==lev[i]],na.rm=T)
  titanic$Age[titanic$name2==lev[i]&is.na(titanic$Age)] <- mean.age
}
#or
name2.mean <- function(x){
  res <- mean(na.omit(titanic$Age[titanic$name2==x]))
  return(res)
}
idx <- is.na(titanic$Age)
titanic$Age[idx] <- unlist(lapply(titanic$name2[idx], name2.mean))


# -age열의 구간별 인원수 출력
# 10대 미만, 10대, 20대, 30대, 40대, 50대 이상
max(titanic$Age)
table(cut(titanic$Age,breaks=c(0,10,20,30,40,50,81),right=FALSE))
# -cabin 컬럼의 1번째 글자 출력(NA는 제외)
substr(titanic$Cabin[complete.cases(titanic$Cabin)],1,1)
# - fare열 값에 대해 최대/최소/평균/표준편차 출력
summary(titanic$Fare)
sd(titanic$Fare)
# - sibsp + parch를 더하여 새롭게 family열에 저장
head(titanic)
titanic$family <- titanic$SibSp+titanic$Parch
titanic
