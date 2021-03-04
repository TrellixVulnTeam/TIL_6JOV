# 1. Survived 열 요약
# - 생존자/사망자 전체 비율
titanic<-read.csv('train.csv',na.strings = "")
proportions(table(titanic$Survived))
str(titanic)
# - 성별에 따른 생존자/사망자

with(titanic,tapply(Survived,Sex,mean))
with(titanic,tapply(Survived,list(Sex),mean))

# 2. Pclass 열 요약
# - 등실 비율
str(titanic)
proportions(table(titanic$Pclass))
# - 등실에 따른 생존자/사망자 비율
proportions(table(titanic[,c('Pclass','Survived')]),1)
table(titanic[,c('Pclass','Survived')])
head(titanic[,c('Pclass','Survived')])
#or
with(titanic,tapply(Survived,list(Pclass),mean))

# 3. Age 열
# - 나이대를 구분한 후, 각 나이대별 생존율
titanic$ages<-cut(titanic$Age,
                  breaks = c(0,10,20,30,40,50,max(titanic$Age)+1),
                  right=FALSE,
                  labels=c('10s','20s','30s','40s','50s')
                  )

proportions(table(titanic[,c('ages','Survived')]),1)
#or
with(titanic,tapply(Survived,list(ages),mean))

# 4. Fare 열
# - 운임을 전체 5개 구간으로 분리한 후,
# 각 구간별 생존율
titanic$fares<-cut(titanic$Fare,
                  breaks = 5,
                  include.lowest = TRUE)

proportions(table(titanic[,c('fares','Survived')]),1)

# 5. Name 열 
# - 호칭을 제외한 이름에서 자음과 모음의 비율
# - 성별에 따른 자음과 모음의 비율
#자음/모음 -> consonant.vowel.ratio
titanic$Name
for (i in 1:nrow(titanic)){
  titanic$realname[i] <- gsub('\\s{1}.{2,}[.]',replacement = '',titanic$Name[i])
  lst<-unlist(strsplit(titanic$realname[i],split=''))
  lst<-grep('[a-zA-Z]{1}',lst,value=TRUE)
  vowel <- grep('[aeiouAEIOU]',lst,value=TRUE)
  titanic$consonant.vowel.ratio[i] <- (length(lst)-length(vowel))/length(vowel)
}

titanic
 

#자음/전체-> consonant.ratio, 모음/전체->vowel.ratio

for (i in 1:nrow(titanic)){
  titanic$realname[i] <- gsub('\\s{1}.{2,}[.]',replacement = '',titanic$Name[i])
  lst<-unlist(strsplit(titanic$realname[i],split=''))
  lst<-grep('[a-zA-Z]{1}',lst,value=TRUE)
  vowel <- grep('[aeiouAEIOU]',lst,value=TRUE)
  titanic$vowel.ratio[i] <- length(vowel)/length(lst)
  titanic$consonant.ratio[i] <- (length(lst)-length(vowel))/length(lst)
}

str(titanic)

# - 성별에 따른 자음과 모음의 비율

#자음/모음
with(titanic,tapply(consonant.vowel.ratio,list(Sex),mean))


#자음/전체, 모음/전체
aggregate(titanic[c('consonant.ratio','vowel.ratio')],list(sex=titanic$Sex),mean)

# 6. Embarked 열
# - 각 승선 항구별 생존율
with(titanic,tapply(Survived,list(Embarked),mean))
# 7. 캐글 가입
