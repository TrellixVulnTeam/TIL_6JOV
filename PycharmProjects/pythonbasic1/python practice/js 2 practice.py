# 1. 숫자 및 문자열 분리 (파이썬)
# 문자와 숫자가 섞인 문자열을 입력받은 후, 숫자와 문자를 분리하시오.
# input:
# "c910m6ia 1ho"

# output:
# str : cma ho
# int : 91061

import re

# a=input()
#
# num=""
# st=""
# for i in a:
#     if i>='0' and i <='9':
#         num+=i
#     else:
#         st+=i
#
# print('str:',st)
# print('int:',num)



# 2. 가위바위보(파이썬)
# 사용자 입력과 random함수를 사용하여, 사용자와 컴퓨터가 대결하는 가위 바위 보 게임을 만들어보자.
#
# 입력: [문자열] "가위", "바위" 혹은 "보" 출력: [문자열] 결과 반환
# 출력: 컴퓨터는 바위, 컴퓨터(가위/바위/보)가 이겼(졌)습니다
# import random
#
#
#
# rpsli=['가위','바위','보']
# com=random.randint(0,2)
# while True:
#     a = input("가위,바위,보 중 하나를 입력하세요:")
#     if a in rpsli:
#         break
#     else:
#         print("잘못 입력하셨습니다. 다시 입력해주세요.")
#
# if rpsli[com]==a:
#     print("컴퓨터는 {}, 컴퓨터와 비겼습니다.".format(rpsli[com]))
# elif (com==0 and a=='보') or (com==1 and a=='가위') or (com==2 and a=='바위'):
#     print("컴퓨터는 {}, 컴퓨터가 이겼습니다.".format(rpsli[com]))
# else:
#     print("컴퓨터는 {}, 컴퓨터가 졌습니다.".format(rpsli[com]))















# 다른사람 풀이

# import random
# choice = ["가위","바위","보"]
# while True:
#     winner = "사용자"
#     comp_num = random.randint(0,2)
#     comp_choice = choice[comp_num]
#     user_choice = input("골라주세요(가위, 바위, 보): ")
#     user_num = choice.index(user_choice)
#     if comp_num == 0 and user_num == 2:
#         winner = "컴퓨터"
#     elif comp_num == 2 and user_num == 0:
#         pass
#     else:
#         if comp_num > user_num:
#             winner = "컴퓨터"
#     print("컴퓨터: %s, 사용자: %s" % (comp_choice, user_choice))
#     if comp_num == user_num:
#         print("비겼습니다.")
#     else:
#         print("%s가 이겼습니다." % winner)








# 3.로또(파이썬)
# 렌덤으로 1부터 45 까지의 무작위로 섞인 6개의 숫자와 당첨 번호로 생성해 저장한 뒤
# 로또를 몇 개 살지 입력받고 입력된 번호의 수에 따라 렌덤으로 뽑힌 번호를 당첨 번호와 비교한다.
# 만약 당첨이 되면 당첨된 번호와 당첨금을 출력해주자

# #1회차
# 예시 : 로또를 몇개 구매하시겠습니까? : 5
# 현재 당첨번호는 43,2,35,16,4,6입니다.
#
# 구매하신 추첨번호는 43,2,41,18,19,21 입니다.
# 구매하신 추첨번호는 28,20,1,4,32,5 보너스번호는 8입니다
# 구매하신 추첨번호는 11,4,35,2,43,16 2등입니다
# ...
#
#
# #2회차
# ...
# #10회차
#
# 1 등 : 6개 일치(10억원)
# 2 등 : 5개 일치(2백만원)
# 3 등 : 4개 일치(5만원)
# 4 등 : 3개 일치(5천원)


# 중복불가

import random
a=set()
while len(a)<7:
    num=random.randint(1,45)
    a.add(num)
print("현재 당첨번호는 {}입니다".format(list(a)[0:6]))


b=int(input("로또를 몇 개 뽑으시겠습니까?"))
n=0
while 1:
    s=set()
    while len(s)<7:
        num=random.randint(1,45)
        s.add(num)




    print("구매하신 추첨번호는{}입니다".format(list(s)[0:6]))
    cnt=0
    for i in s:
        if i in a:
            cnt+=1

    if cnt==6:
        print("1 등 : 6개 일치(10억원)")
    elif cnt==5:
        print("2 등 : 5개 일치(200만원)")
    elif cnt==4:
        print("3 등 : 4개 일치(5만원)")
    elif cnt==3:
        print("4 등 : 3개 일치(5천원)")


    n+=1
    if n==b:
        break


#

# import random
# a=set()
# while len(a)<7:
#     num=random.randint(1,45)
#     a.add(num)
# print("현재 당첨번호는 {}입니다".format(list(a)[0:6]))
#
#
# b=int(input("로또를 몇 개 뽑으시겠습니까?"))
#
# for i in range(b):
#     s=set()
#     while len(s)<7:
#         num=random.randint(1,45)
#         s.add(num)
#
#     print("구매하신 추첨번호는{}입니다".format(list(s)[0:6]))
#     cnt=0
#     for i in s:
#         if i in a:
#             cnt+=1
#
#     if cnt==6:
#         print("1 등 : 6개 일치(10억원)")
#     elif cnt==5:
#         print("2 등 : 5개 일치(200만원)")
#     elif cnt==4:
#         print("3 등 : 4개 일치(5만원)")
#     elif cnt==3:
#         print("4 등 : 3개 일치(5천원)")





#
# import random
#
# a = int(input("로또를 몇개 구매하시겠습니까?"))
# num1=set()
# for i in range(7):
#     numbers=random.randint(1,45)
#     num1.add(numbers)
#     num2=set()
#
#     numbers = random.randint(1, 45)
#     num2.add(numbers)
#     print("구해하신 추첨번호는{}입니다".format(num2))
#
# for i in range(a):
#     a=sorted(num1)
#     b=sorted(num2)
#     if a==b:
#         print("6개일치(10억원)")
#     elif a[0:4]==b[0:4]:
#         print("5개 일치(2백만원)")
#     elif a[0:3]==b[0:3]:
#         print("4개 일치(5만원)")
#     elif a[0:2]==b[0:2]:
#         print("3개 일치(5천원)")
















#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
