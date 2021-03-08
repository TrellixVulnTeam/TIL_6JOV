#데이터전처리(S-A-C) 패키지: dplyr
#데이터 분할(S)->분할 자료에 대해 함수를 적용(A)->결과를 취합(C)

#arrange(정렬), filter(행추출), select(열추출), mutate(열 추가), summarise(요약)

head(airquality)
library(dplyr)

#방법 2가지
airquality[airquality$Month==6,]
subset(airquality,subset=(Month==6))
#filter이용
air<-filter(airquality,Month==6)
head(air)

#Month가 6이면서 temp>90 초과(and연결은 ,또는 &기호를 사용)
air<-filter(airquality,Month==6 & Temp>90)
filter(airquality,Month==6, Temp>90)

#or연산
air<-filter(airquality,Temp>90 | Ozone>80)
air

#slice():단순히 특정 위치의 행데이터 추출
slice(airquality, 6:10) #추출하고자 하는 행 번호

#arrange():데이터프레임을 정렬 할 때 사용(지정한 열을 기준으로...)
#Temp기준으로 오름차순,내림차순, 두번째 기준Month(오름차순)
arrange(airquality,Temp)
arrange(airquality,desc(Temp), Month,Day)

#퀴즈1, order함수로 변경
airquality[order(airquality$Temp,airquality$Month,airquality$Day,decreasing = c(T,F,F)),]
#or
airquality[order(-airquality$Temp,airquality$Month,airquality$Day),]
#or
with(airquality,airquality[order(-Temp,Month,Day),])


#select():열 추출(,는 여러 개의 떨어진 열을 추출, :는 연속인 열을 추출,-는 특정 열을 제외하고 추출할 때)
air<-select(airquality, Month, Day, Temp)
air
head(airquality)

air<-select(airquality, Temp:Day)
air

air<-select(airquality, -(Ozone:Wind))
air

#열 이름 바꾸고 싶을 때(그렇지만 열 이름 변경은 select보다는 renaem을 쓰는 걸 권장)
air<-select(airquality, Solar=Solar.R)
air

air<-rename(airquality,Solar=Solar.R)
head(air)


#특정 열에 포함된 중복되지 않은 데이터 추출:select+distinct함수 조합(unique함수와 유사)
distinct(select(airquality,Month))

unique(airquality$Month)

#mutate:새로운 열(파생변수)추가
airquality$Temp
#화씨->섭씨:(화씨-32)/1.8(열 추가)
head(mutate(airquality,Temp.c=(Temp-32)/1.8))

#mutate로 새로운 열을 동일한 함수 내에서(Diff) 사용 가능
head(mutate(airquality,Temp.c=(Temp-32)/1.8,Diff=Temp.c-mean(Temp.c)))

#transfrom함수에서는 에러 발생(새로운 열을 동일한 함수 내에서(Diff) 사용 불가하기때문에)
transform(airquality,Temp.c=(Temp-32)/1.8,Diff=Temp.c-mean(Temp.c))


#요약 통계:summarise함수
summarise(airquality,mean(Temp))

airquality

summarise(airquality,
          Min=min(Temp,na.rm=T),
          Median=median(Temp,na.rm=T),
          Mean=mean(Temp,na.rm=T),
          Sd=sd(Temp,na.rm=T),
          Max=max(Temp,na.rm=T),
          N=n(),
          Distinct.Month=n_distinct(Month),
          First.Month=first(Month),
          Last.Month=last(Month),
          )
summary(airquality)

#sample_n:표본 추출(개수)
#sample_frac:표본 추출(비율)
#옵션: replace=TRUE (복원추출)

sample_n(airquality,5)

sample_frac(airquality,0.1)

#!!group_by함수:그룹별로 분할
air.group<-group_by(airquality, Month) #월별로 그룹화
air.group



#월별 통계량
summarise(air.group,
          mean_Temp=
            mean(Temp,na.rm=T),
          )
#위의 결과와 동일
air.group.Temp<-summarise(group_by(airquality, Month),
          mean_Temp=
            mean(Temp,na.rm=T),
)
air.group.Temp


#ctrl+shift+m ->파이프 연산자: %>% 한 함수로부터 연산 결과가 다음 함수의 인수로 전달되도록 하는 연산자 
#장정: 중간중간 저장하는 작업을 할 필요 없음
head(iris)
iris %>% head


1:10 %>% mean

#1:10 %>% mean %>% sqrt

a1<-select(airquality,Ozone,Temp,Month)
head(a1)
  
a2<-group_by(a1, Month)
a2

a3<-summarise(a2,
          Mean.Ozone=mean(Ozone,na.rm=TRUE),
          Mean.Temp=mean(Temp,na.rm=TRUE),
          )

#a3자료 중 Ozoen이 40초과하거나 Temp가 80초과인 데이터(행)을 추출

a4<-filter(a3,Mean.Ozone>40 | Mean.Temp>80)
a4

#1)파이프 연산자를 사용한 경우

air<-airquality %>% 
  select(Ozone,Temp,Month) %>%   #a1
  group_by(Month) %>% 
  summarise(Mean.Ozone=mean(Ozone,na.rm=TRUE),  #a2
            Mean.Temp=mean(Temp,na.rm=TRUE)) %>%   #a3
  filter(Mean.Ozone>40 | Mean.Temp>80)  #a4
  

#as.data.fram:tibble-<data frame

air_df<-as.data.frame(air)
air_df


#data frame ->tibble
tbl_df(air_df)



install.packages("Lahman")  
library(Lahman)

str(Batting)
tail(Batting)




Batting.tbl.df<-tbl_df(Batting)
Batting.tbl.df



#데이터 변환


#데이터의 외형상 특징: 와이드형, 롱형

#롱형
# subject       var     value
# abercada01    stint     1
# abercada01    teamID    1
# abercada01    ...
# abercada01    ..





#melt함수: 와이드형<->롱 형 변환, reshape2 패키지 설치
install.packages("reshape2")
library(reshape2)
 


smiths #reshape2 에 포함된 데이터,
#melt: 와이드 형식으로 저장=>롱포맷 변환
smiths.long<-melt(data=smiths)
smiths.long

#variable을 명시하려면 id.vars 옵션
smiths.long<-melt(smiths, id.vars ='subject')
smiths.long

str(smiths) #subject가 팩터로 되어 있으므로
#melt함수를 이용하여 와이드->롱형으로 변환시, 
#자동으로 subject변수를 식별자로 사용하게 됨.




#dcast:롱포맷->와이드포맷
#변수 배치는 formula로 지정
#x~y: x에는 식별자 변수, y에는 측정변수, 변수가 여러개 일때는 +로 연결

smiths.wide<-dcast(smiths.long, formula = subject ~ variable)
smiths.wide


#airquality는 와이드 형 자료(매일 측정, 행 단위로 일 측정 결과)
airquality
#롱형으로 변환
aq.long<-melt(airquality)

tail(aq.long)

#month와 day를 묶어서 식별자로 사용

aq.long<-melt(airquality, id.vars = c("Month","Day"))
head(aq.long)
tail(aq.long)

#aq.long->와이드 형 변환
#dcast:롱포맷->와이드포맷
#변수 배치는 formula로 지정
#x~y: x에는 식별자 변수, y에는 측정변수, 변수가 여러개 일때는 +로 연결

dcast(aq.long, formula = Month + Day ~ variable)



#left_join(): 열 데이터 합치기(cbind)
#bind_rows(): 행 데이터 합치기(rbind)

exam<-read.csv("csv_exam.csv")
exam

#exam에서 class가 1인 자료들만 추출( %>% )
exam %>%
  filter(class==1)

#exam에서 class가 1이 아닌 자료들만 추출( %>% )
exam %>%
  filter(class!=1)

#수학점수가 50점을 초과한 데이터만 추출
exam %>%
  filter(math>50)

#수학점수가 50점을 초과하면서 반이 1반인 데이터만 추출

exam %>%
  filter(math>50, class==1)

#수학점수가 90점 이상이거나 영어점수가 90점 이상인 데이터 추출
exam %>%
  filter(math>90 | english>90)


#1반 2반 3반 자료만 추출
exam %>%
  filter(class==1 | class==2 |class==3 )

exam %>%
  filter(class %in% c(1,2,3))


class1<-exam %>%
  filter(class==1)


class2<-exam %>%
  filter(class==2)


#1반, 2반 수학점수의 평균 출력
mean(class1$math)
mean(class2$math)

#class가 1반인 행만 추출한 다음 enligh열 추출

exam %>% filter(class==1) %>% select(english)

#id열과 math열 추출, 앞부분 6개만 출력
exam %>% 
  select(id, math) %>% 
  head()

#exam에서 math 기준으로 오름차순 정렬
exam %>% 
  arrange(math)
#내림차순
exam %>% 
  arrange(desc(math))

#수학, 영어, 과학점수를 모두 더하여 total변수 추가 및 출력

exam %>% 
  mutate(total=math,english+science,
         mn=total/3) 

#science가 60점 이상이면 pass, 미만이면, fail을 test열에 추가

exam %>% 
  mutate(test=ifelse(science>=60,'pass','fail')) %>% 
  head

#수학, 영어, 과학점수를 합하여 total열을 추가
#total열을 기준으로 오름차순 정렬하여 출력

exam %>% 
  mutate(total=math+english+science) %>% 
  arrange(total)


#그룹단위 요약
#exam에서 반별 수학점수 평균 출력


exam %>% 
  group_by(class) %>% 
  summarise(Math_Mean=mean(math))

#그룹단위 요약
#exam에서 반별 수학점수 합계, 평균, 중위수, 학생수 출력


exam %>% 
  group_by(class) %>% 
  summarise(Math_Mean=mean(math),
            Math_Sum=sum(math),
            Math_Median=median(math),
            cnt=n()  #또는 length(math)
            )


mpg
#manutacturer,drv
#회사별 구동방식별 그룹화
#cty 평균 출력

head(mpg)

mpg %>% 
  group_by(manufacturer, drv) %>%  #첫번째 그룹화 기준 : manufacturer ,두번째 그룹화 기준: drv
  summarise(Mean_City=mean(cty)) 


#제조사: 15 * 구동방식: 3=45


#mpg 에서 회사별로 그룹화
#회사별로 class가 suv를 추출
#cty와 hty의 평균을 구하여 tot라는 새로운 열을 추가
mpg %>% 
  group_by(manufacturer) %>%  
  filter(class=='suv') %>% 
  mutate(tot=(cty+hwy)/2) %>% 
  summarise(mean_tot=mean(tot))  %>%  #그룹별 통합 연비의 평균 출력
  arrange(desc(mean_tot)) %>% 
  head(5)

  
  
# 중간고사 데이터 생성
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85))
# 기말고사 데이터 생성
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 80))
  

test1
test2

#id기준으로 합치기
total<-left_join(test1,test2,by='id')
total


name <- data.frame(class = c(1, 2, 3, 4, 5),
                   teacher = c("kim", "lee", "park", "choi", "jung"))



total

#class기준으로 합치기
name
exam
examNew<-left_join(exam,name, by="class")
examNew




# 학생 1~5 번 시험 데이터 생성
group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85))
# 학생 6~10 번 시험 데이터 생성
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(70, 83, 65, 95, 80))

group_a
group_b


group_all<-bind_rows(group_a,group_b)
group_all

