#연관규칙(아프리오리 알고리즘)


#협업필터링 알고리즘: 추천대상 고객과 가장 높은 상관계수에 해당되는 고객들을 찾아서 상품 추천
#연관규칙: 동시 구매 규칙을 도출


#규칙?: if 조건 then 결과. if(조건->결과)


#특정 항목 집합이 발생했을 때 또 다른 항목 집합이 발생하는 규칙
#ex) {금요일, 남성, 맥주}->{기저귀}
#    특정항목집합          또 다른 항목 집합

#x, y를 항목집합, 연관규칙은 x-y(x구매한 사람은 y구매)

#n은 전체 거래 건수 ex) n(x): x항목집합의 거래 건수 

#연관규칙의 척도 





#지지도 ,신뢰도 등 개념 참고하기 좋은 사이트 
#https://needjarvis.tistory.com/59

#1)지지도 (support)
#두 항목 집합 x와 y의 지지도?
#분모에 전체 거래수, 분자에는 x와 y를 모두 포함하는 거래수
#동일한 물건을 여러번 거래한 것에 대해서는 참고하지 않음
#s(X->Y): x구매자가 y도 구매하는 규칙에 대한 지지도 

#=> (xUy)/N

# 전체 거래에서 특정 물품 A와 B가 동시에 거래되는 비중
# 
# 해당 규칙이 얼마나 의미있는지 보여줌.
# 
# 
# 
# 지지도 = P(A∩B) 
# 
# : A와 B가 동시에 일어난 횟수 / 전체 거래 횟수





#2)신뢰도 
#항목집합 x를 포함하고 있는 거래 중에서, 항목집합 y도 포함하는 거래비율
#맥주를 구매한 사람들 중에서 땅꽁도 구매한 사람들의 비율이 어떻게 되는지
#분모: 맥주 거래 건수, 분자: '
#분모: x의 구래한 사람의 건수, 분자: x를 산 사람 중에 y를 산사람

#m(XUY)/m(x)

#c(X->Y)
#lift(x,y)

#c(x->y)/s(y): 항목집합 y의 확률대비, 항목집합 x가 주어졌을 때 항목집합 
#y의 거래 비율

#향상도가 1보다크면 , 우연적인 기회보다 필연적인 가능성 높음
#향상도가 1보다작아도 , 우연적인 기회보다 필연적인 가능성 높음
#x,y가 독립=1



# A를 포함하는 거래 중 A와 B가 동시에 거래되는 비중
# 
# 
# 
# 신뢰도 =  P(A∩B) / P(A)  
# 
# :  A와 B가 동시에 일어난 횟수 / A가 일어난 횟수
# 
#


#3)향상도(lift)
#c(X->y)/s(y)
# A라는 상품에서 신뢰도가 동일한 상품 B와 C가 존재할 때, 어떤 상품을 더 추천해야 좋을지 판단.
# 
# A와 B가 동시에 거래된 비중을 A와 B가 서로 독립된 사건일 때 동시에 거래된 비중으로 나눈 값
# 
# 
# 
# 향상도 = P(A∩B) / P(A)*P(B) = P (B|A) / P (B)
# 
# : A와 B가 동시에 일어난 횟수 / A, B가 독립된 사건일 때 A,B가 동시에 일어날 확률
# 






#거래 id: 1,2,3,4,5
#거래된 상품: 첫번째 고객:계란, 우유
#             두번째 고객:계란, 기저귀, 맥주,사과
#             세번째 고객:우유, 기저귀 맥주, 콜라
#             네번째 고객:계란, 우유, 맥주 ,기저귀
#             다섯번째 고객:계란, 우유, 맥주, 콜라



#N=5(전체 거래건수)

#연관규칙: {계란, 맥주}->{기저귀}
#s(y)= n(y)/N==>   3/5 =>0.6



#1)지지도?
#s(x->y)=m(xUy)/N==>2(계란, 맥주, 기저귀 다 있는 항목)/5==>0.4


#2)신뢰도?
#c(x->y)=n(xUY)/m(x)=>   2(계란, 맥주, 기저귀)/3==>0.666...(계란, 맥주를 구매한 사람의 66%는 기저귀도 구매했다)


#3)향상도?
#lift(x->y)=c(x->y)/s(y)=> 0.666///0.6(3/5)==>1.111/...

#향상도의 값이 크면 클 수록 규칙이 매우 강력하다는 척도가 됨
#분모는: 기저귀 구매한사람, 분자: 계란 맥주 산 사람을 특정 했을 때 이 사람들이 기저귀를 얼마나 샀을 까?
#결과적으로 일반적으로 기저귀 구매한 비율 대비, 계란,맥주를 구매한 사람 대비 기저귀를 구매한 사람 비율


#is척도 = 루트(향상도 * 지지도)

#교차지도 = 최대 지지도에대한 최최지지도의 비율
#둘의 차이가 클수록 교차지지도 작아짐, 항목집합 x에 대해서 생성되는 연관규칙은 의미 없는 규칙일 가능성이 높아짐




#연관규칙(아프리오리 알고리즘)
#I={i,....,ik}
#부분집합= 2의 k승 -1(공집합은 빼야하니 -1)

#아프리오리 알고리즘의 핵심

#어떤 한 항목집합이 빈발-> 이 항목이 포함되어져있는 모든 부분집합 역시 빈발하다고 보룻 있다
#어떤 한 항목집합이 빈발하지 않다면 -> 이 항목이 포함되어져있는 모든 부분집합 역시 빈발하지 않다고 봄


df<-read.csv('groceries.csv', header=FALSE)
df
str(df)
head(df,10)

install.packages("arules")
library(arules)

groceries<-read.transactions('groceries.csv',sep=',')
groceries
summary(groceries)

# 9835 rows (elements/itemsets/transactions) and
# 169 columns (items) and a density of 0.02609146 
#169컬럼중 0.026...정도만 채워져있고 나머지 97-8퍼센트는 ..


# element (itemset/transaction) length distribution:
#   sizes
# 1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17 
# 2159 1643 1299 1005  855  645  545  438  350  246  182  117   78   77   55   46   29 
# 18   19   20   21   22   23   24   26   27   28   29   32 
# 14   14    9   11    4    6    1    1    1    1    3    1 
#장바구니에 아이템이 1개 담겨져 있는 경우 2159.,,,



class(groceries)  #희소행렬
#희소행렬 안의 데이터를 보려면 inspect사용

inspect(groceries[1:10])  #트랜잭션 단위로 구매 아이템 확인

itemFrequency(groceries[,])  #열단위로 확인할 때. 지지도나옴 (beef: 0.05246...정도(각각의 상품별로 거래 비율이 어떻게 되는지 나옴))

itemFrequencyPlot(groceries)


itemFrequencyPlot(groceries, support=0.1) #지지도가 0.1이상인 것들만 출력


itemFrequencyPlot(groceries, topN=25)  #가장 itemfrequency측면에서 빈도수가 높은 25가지 상품들 나타냄

image(groceries[1:10]) #점 하나하나가 아이템. 거래 데이터가 맣은 경우에 아이템들을 볼때 어느 쪽이 거래가 많았는지 쉽게 파악하기 위해 보는 함수
#168정도(오른쪽끝)에서 거래가 많이 발생했을 거라고 볼 수 있음



#랜덤하게 100개의 상품을 추출하여 행렬다이어그램 형식으로 출력

image(sample(groceries,100))


#연관규칙 구현

image(sample(groceries,100))
groceryrules<-apriori(groceries, list(support=0.006, confidence=0.25 , minlen=2))
#지지도 0.006, confidence가 신뢰도, 아이템항목의 최소길이는 2이상

groceryrules


apriori(groceries)
# set of 0 rules ->이 요건을 만족하는 rule이 없다(디폴트 적용: support=0.1,confidence=0.8에 만족하는 rule이 없다)



summary(groceryrules)
#size1개=>2159건

inspect(groceryrules[1:3])


inspect(sort(groceryrules, by='lift')[1:10])



berryrules<-subset(groceryrules, items %in% 'berries')  #items는 열의 lhs 의미
inspect(berryrules)
#lhs라고 주면 규칙의 왼쪽에 doc1또는 doc2가 있는 경우
#items는 규칙의 양쪽에 doc1또는 doc2가 있는 경우

byrules<-berryrules<-subset(groceryrules, items %in% c('berries','yogurt'))

inspect(byrules)



#pin  ==>아이템 이름에 대한 부분매칭
fruitrules<-berryrules<-subset(groceryrules, items %pin% 'fruit')
inspect(fruitrules)



#ain=> 조건이 모두 들어간 것 만 나옴
allbyrules<-berryrules<-subset(groceryrules, items %ain% c('berries','yogurt'))
inspect(allbyrules)




write(groceryrules,'groceryrules.csv',sep=',',quote=FALSE,row.names=FALSE)

#규칙->데이터 프레임으로 변환하고자 할 때
groceryrulesDF<-as(groceryrules,'data.frame')
groceryrulesDF







subset(groceryrules, items %in% 'berries')

#조건을 더 세분화 할 수 있음
inspect(subset(groceryrules, items %in% 'berries' & confidence>0.3))


#지금까지 내용:apriori알고르즘으로 연관규칙(association rules) 생성





#data자체가 transaction형태로 되어있어서 read안하고 바로 summary할 수 있음
help(Epub)
data(Epub)
summary(Epub)

inspect(Epub[1:10])


#1. Epub데이터 연관규칙
#-support, confidece 설정
#-minlen-2
#
#2. 정령
#lift, confidence, support 각각 기준으로 정렬해보기

#3. subset활용해 연관규칙 부분집합
#-support에서 ain,pin, in 등 활용












