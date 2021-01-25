# 1. IT기업 코딩 테스트문제

# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

#

names="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

import re

# 김씨와 이씨는 각각 몇 명 인가요?

list1=names.split(",")

# print(list1)

kim=[]

lee=[]

for i in list1:

    if i[0]=="김":

        kim.append(i)

    elif i[0]=="이":

        lee.append(i)

lkim=len(kim)

llee=len(lee)

print("김씨는 {0}명, 이씨는 {1}명 입니다.".format(lkim,llee))



# "이재영"이란 이름이 몇 번 반복되나요?

cnt=0

for i in lee:

    if i=="이재영":

        cnt+=1

print("{0}번 반복됩니다.".format(cnt))


# 중복을 제거한 이름을 출력하세요.

li=set(list1)

print(li)

# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

print(sorted(li))


print("="*30)




# 2. 토지 원고 데이터


file = open('toji.txt',encoding='utf-16').read()

# print(file)


# #

# 1) 저자명 추출


from bs4 import BeautifulSoup


soup=BeautifulSoup(file,"html.parser")

print(soup.find("author").string)

# 2) 제목 추출

title=soup.select("title")

print("제목:",title[1].string)

# 3) 출판사명 추출

print("출판사명:",soup.find("publisher").string)


# 4) 인용부호(큰 따옴표)로 묶여있는 내용을 모두 추출하여 리스트에 저장



pt=str(soup.select("p"))


print(re.findall("[\"]+[\s\w.,?]+[\"]",pt))




# 5) 토지 원고 전체에서 한글에 해당되는 내용만 추출하여 저장, 가장 많이 사용된 단어

# 100개를 출력


dic = {}

hangul = re.findall("[가-힣]+", file)

for i in hangul:

    if dic.get(i):

        dic[i] += 1

    else:

        dic[i] = 1


res = []

li = []

res = sorted(dic, key=dic.get, reverse=True)

for i in range(100):

    li.append(res[i])

print(li)







# 6) 각 장의 제목 저장 및 출력


res=soup.find_all("head")

#print(res)


for i in res:

print(i.string)


﻿