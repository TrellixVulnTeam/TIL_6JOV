#1. Epub데이터 연관규칙
#-support, confidece 설정
#-minlen-2
#
#2. 정령
#lift, confidence, support 각각 기준으로 정렬해보기

#3. subset활용해 연관규칙 부분집합
#-support에서 ain,pin, in 등 활용

rule1<-apriori(Epub, list(support=0.003, confidence=0.20,minlen=2))
rule1

rule2<-apriori(Epub, list(support=0.002, confidence=0.20,minlen=2))
rule2
summary(rule2)




rule3<-apriori(Epub, list(suppor=0.0015, confidence=0.01, minlen=2))
rule3
summary(rule3)
inspect(rule3)


rule4<-apriori(Epub,list(support=0.0008,confidence=0.25,minlen=2))
rule4 #set of 89 rules 
summary(rule4)
# rule length distribution (lhs + rhs):sizes
# 2  3 
# 65 24 



rule5<-apriori(Epub,list(support=0.0005,confidence=0.25,minlen=2))
rule5 #set of 1048 rules 
summary(rule5)
# 2    3    4  5    6 
# 149 613 220  60   6 
inspect(rule5)

# 2. 정렬
#-lift, confidence,support 기준으로 어떤 아이템이 높은지

#rule3 17 rules 
inspect(sort(rule3,by='lift')[1:10])



inspect(sort(rule3,by='confidence')[1:10])
#lhs 의 책을 다운로드할때, rhs 의 책까지 포함할 확률(80%-70%)  높음




#rule4
inspect(sort(rule4,by='lift')[1:10])
# doc_6e7,8,...의 책끼리 lift 높다 -> 같은 시리즈의 책일거라고 예상할수있다.
# 같은 시리즈라면, 연관되는 것이 당연하기 때문에 무의미함



#rule5 1048 rules

inspect(sort(rule5,by='lift')[1:10])




inspect(sort(rule5,by='support')[1:10])

#support, lift 를 각각 내림차순으로 정렬헀을대 상위 10개의 목록
#support 상위 10개 중 5위까지는 1000명중 2-4명이 다운로드함, lift도 높은 편
#lift 상위 10개는 10000명 중 5-10명정도가 다운로드하지만, lift 매우 높음 , 아이템 이름이 비슷해서 같은 시리즈의 책일 가능성 있음




#3. 연관규칙 부분집합


inspect(subset(rule5,lhs %in% 'doc_4ac'))




inspect(subset(rule5,rhs %in% 'doc_4ac'))



inspect(subset(rule5, items %pin% 'doc_6e')[1:10])
# doc_6e7,8,9,a -> 연관도 높음 


inspect(subset(rule5, items %ain% c('doc_6e8','doc_6e9')))


