# # 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
#
# def is_odd(n):
#     if n%2==0:
#         print("짝수")
#     else:
#         print("홀수")
# # #
# # # 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# # 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# f=open("test.txt","a")
# f.write("Life is too short")
# f.close()
#
# f=open("test.txt","r")
# s=f.read()
# print(s)
# f.close()

# # #
# # #
# # 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# # Life is too short
# # you need java
# f=open("test.txt",'w')
# s=f.write("life is too short\nyou need java")
# f.close()
#
# f=open('test.txt','r')
# mod=f.read()
# f.close()
#
# mod=mod.replace("java","python")
#
# f=open('test.txt','w')
# f.write(mod)
# f.close()
# # #
# # #
# # 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
#
# def print_coin():
#     print("비트코인")
#
# # #
# # # #
# # 5. 4에서 정의한 함수를 호출하라.
# print_coin()
#
# # 6. 4에서 정의한 print_coin 함수를 100번호출하라.
# # for i in range(101):
# #     print_coin()
#
# # 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coins():
#     for i in range(100):
#         print("비트코인")
# print_coins()
#
# #
# # 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile(n):
#     print(n,":D")
#
# print_with_smile()
#
#
# # #
#
# # # 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# #
# def print_upper_price(n):
#     print(n*1.3)
#
# print_upper_price(130)
# # #
# #
# #
# #
# # # 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# #
#
# def print_even(n):
#     list=[]
#     for i in n:
#         if i%2==0:
#             list.append(i)
#     print(list)
# #
# #
# # print_even([1,2,3,4,5,6])
# #
# #
# # # def print_even(n):
# # #     for i in n:
# # #         if i%2==0:
# # #             print(i)
# # #
# # #
# # # print_even([4,5,6,7,8])
# # #
# # # # 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
#
# def print_key(dic):
#     print(dic.keys())
#
# print_key({1:2,3:4})

# #
# # # def print_keys(dic):
# # #     return dic.keys()
# # #
# # # print(print_keys({1:2,3:4}))
# # #
# # #
# # # 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
#
#
#
# def print_mxn(str, b):
#     cnt=0
#
#     for i in str:
#         print(i, end="")
#         cnt+=1
#
#         if cnt % b == 0:
#             print("")
#
#
#
# print_mxn('helloimchloe^^', 3)
# #
# #
# #
# # #
# # #
# # #
# # #
# # # 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# # # calc_monthly_salary(12000000)
# # # 1000000
#
# def calc_mothly_salary(annual_salary):
#     s=int(annual_salary/12)
#     return s
# print(calc_mothly_salary(4650000))
# # #
# # #
# # #
# # #
# # # #
# # # 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# # # make_url("naver")
# # # www.naver.com
# # #
# def make_url(n):
#     b="www."+n+".com"
#     return b
#
# print(make_url("naver"))
# #
# # #
# # # 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# # # make_list("abcd")
# # # ['a', 'b', 'c', 'd']
#
# def make_list(n):
#     s=[]
#     for i in range(len(n)):
#         s.append(n[i])
#         return s
# #
# #
# #
# #
# #
# # #
# # # def make_list(n):
# # #     s=[]
# # #
# # #     for i in range(len(n)):
# # #         s.append(n[i])
# # #     return s
# # #
# # #
# # #
# # # print(make_list("abcd"))
# # #
# # #
# #
# # #
# # #
# # 16. 게임 기업 입사문제
# # 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# #
# # 예를 들어
# # d(91) = 9 + 1 + 91 = 101
# # 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# # 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며,
# # 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# # 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
#
# #
#
# myList=[]
#
# for i in range(1,5001):
#     n=str(i)
#     cnt=0
#     for j in range(len(n)):
#         cnt+=int(n[j])
#     gen_list=i+cnt
#     myList.append(gen_list)
# print(myList)
#
#
#
# print(sum(set(range(1,5000)) - set(myList)))
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














#승혀니 풀
# mylist=[]
# for i in range(1,5000):
#     cnt=0
#     for j in str(i):
#         cnt+=int(j)
#     cnt+=i
#
# print(sum(set(range(1,5000))-set(mylist)))
#
#다른 분 풀이
# generator=[]
# for i in range(1,5001):
#
#     int_to_str = str(i) #int_to_str: i를 문자열로 변환
#
#     summ = 0
#
#     for j in range(len(int_to_str)): #각 자리수(1의자리, 10의자리,,..) 더하기 = summ
#
#         num_list =int(int_to_str[j])
#
#         summ+=num_list
#
#         gen_num= i+summ #원래 숫자 + 자리수 합
#
#         generator.append(gen_num)
#
#         print(generator)
#
# all_num = list(range(1,5001))
#
# final =list(set(all_num)-set(generator)) # (1~5000)에서 generator를 가진 숫자 제거

# #
#
# #
# myList = []
#
# for i in range(1,5000):
#     cnt = 0
#     for j in str(i):
#         cnt += int(j)
#     cnt += i


# print(sum(set(range(1,5000)) - set(myList)))

# #
# # # #
# # # # 17. 최대낙차
box=[7,4,2,0,0,6,0,7,0]
# # # # # 출력->최대 낙차: 7
#
# for i in range(len(box)): #0~9
#     for j in box:
#         if box[:
#




# # # #
# # # # # 17. 최대낙차
# box=[7,4,2,0,0,6,0,7,0]
# # # # # # 출력->최대 낙차: 7
# cnt=0
# list=[]
# for i in range(len(box)): #0~9
#     for j in box:
#
#         if box[j]<=i:
#             cnt+=1
#             c=len(box)-j-cnt
#             list.append(c)
#
# print(max(list))
#
# #
#
#
#
#
#
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # 단수를 입력 받아 구구단 계산
# # # 예)
# # # 구구단 단수 입력: 3
# # # 3x1=3
# # # 3x2=6
# # # .....
# # # 3x9=27
# #
# #
# # # a=int(input("구구단 단수 입력: "))
# #
# # for i in range(2,20): #i는 2부터 9까
# #     for j in range(1,10):  #j는 1부터 9까
# #         print("{}x{}={}".format(i,j,i*j))
# #     print("")
# #
# #
# #
# # #
# # # 12345
# # # 23456
# # # 34567
# # # 45678
# # # 56789
# #
# # #
# # # for i in range(1,6):            #   i =      1     /     2      /  3
# # #     for j in range(i,i+5):      #   j =  1 2 3 4 5 / 2 3 4 5 6 /
# # #         print(j,end="")
# # #     print("")
# #
# #
# # #
# # # 56789
# # # 45678
# # # 34567
# # # 23456
# # # 12345
# #
# # # for i in range(5,0,-1):
# # #     for j in range(i,i+5):
# # #         print(j,end="")
# # #     print("")
# #
# #
# #
# # # 시작 단 입력 : 2
# # # 끝 단 입력 : 7
# # #
# # # 2 x 1 = 2
# # # .....
# # # 7 x 9 = 63
# #
# #
# # #
# # # a=int(input("시작 단 입력 : "))
# # # b=int(input("끝 단 입력 : "))
# # #
# # # for i in range(a,b+1):
# # #     for j in range(1,10):
# # #         print("%dx%d=%d"%(i,j,i*j))
# # #     print("")
# #
# #
# #
# #
# # # *
# # # **
# # # ***
# # # ****
# # # *****
# #
# #
# # for i in range(1,6):
# #
# #
# #     for j in range(i):
# #         print("*",end="")
# #     print("")
# #
# #
# # #     *
# # #    **
# # #   ***
# # #  ****
# # # *****
# #
# # for i in range(1,6):
# #
# #     for j in range(5-i):
# #         print(" ",end="")
# #         for k in range(i):# # # 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# # # #
# # # # def is_odd(n):
# # # #     if n%2==0:
# # # #         print("짝수")
# # # #     else:
# # # #         print("홀수")
# # # #
# # # # # 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# # # # 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# # # f=open("test.txt","a")
# # # f.write("Life is too short")
# # # f.close()
# # #
# # # f=open("test.txt","r")
# # # s=f.read()
# # # print(s)
# # # f.close()
# # #
# # # #
# # # #
# # # # # 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# # # # # Life is too short
# # # # # you need java
# # # # f=open("test.txt",'w')
# # # # s=f.write("life is too short\nyou need java")
# # # # f.close()
# # # #
# # # # f=open('test.txt','r')
# # # # mod=f.read()
# # # # f.close()
# # # #
# # # # mod=mod.replace("java","python")
# # # #
# # # # f=open('test.txt','w')
# # # # f.write(mod)
# # # # f.close()
# # # #
# # # #
# # # # # 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# # # #
# # # # def print_coin():
# # # #     print("비트코인")
# # # #
# # # #
# # # # #
# # # # # 5. 4에서 정의한 함수를 호출하라.
# # # # print_coin()
# # # #
# # # # # 6. 4에서 정의한 print_coin 함수를 100번호출하라.
# # # # # for i in range(101):
# # # # #     print_coin()
# # # #
# # # # # 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# # # # def print_coins():
# # # #     for i in range(100):
# # # #         print("비트코인")
# # # # print_coins()
# # # #
# # # # #
# # # # # 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# # # # def print_with_smile(n):
# # # #     print(n,":D")
# # # #
# # # # print_with_smile()
# # # #
# # # #
# # # #
# # # #
# # # # # 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# # # #
# # # def print_upper_price(n):
# # #     print(n*1.3)
# # #
# # # print_upper_price(130)
# # #
# # #
# # #
# # #
# # # # # 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# # # #
# # #
# # # def print_even(n):
# # #     list=[]
# # #     for i in n:
# # #         if i%2==0:
# # #             list.append(i)
# # #     print(list)
# # #
# # #
# # # print_even([1,2,3,4,5,6])
# # #
# # #
# # # # def print_even(n):
# # # #     for i in n:
# # # #         if i%2==0:
# # # #             print(i)
# # # #
# # # #
# # # # print_even([4,5,6,7,8])
# # # #
# # # # # 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# # # #
# # # def print_key(dic):
# # #     print(dic.keys())
# # #
# # # print_key({1:2,3:4})
# # #
# # #
# # # # def print_keys(dic):
# # # #     return dic.keys()
# # # #
# # # # print(print_keys({1:2,3:4}))
# # # #
# # # #
# # # # # 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# # # #
# # # # # ("안녕하세요저는신준미",3)
# # # # # 안녕하
# # # # # 세요저
# # # # # 는신준
# # # # # 미
# # #
# # #
# # #
# # # def print_mxn(str, b):
# # #     cnt=0
# # #
# # #     for i in str:
# # #         print(i, end="")
# # #         cnt+=1
# # #
# # #         if cnt % b == 0:
# # #             print("")
# # #
# # #
# # #
# # # print_mxn('helloimchloe^^', 3)
# # #
# # #
# # #
# # # #
# # # #
# # # #
# # # #
# # # # # 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# # # # # calc_monthly_salary(12000000)
# # # # # 1000000
# # #
# # # def calc_mothly_salary(annual_salary):
# # #     s=int(annual_salary/12)
# # #     return s
# # # print(calc_mothly_salary(4650000))
# # # #
# # # #
# # # #
# # # #
# # # # #
# # # # # 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# # # # # make_url("naver")
# # # # # www.naver.com
# # # # #
# # # def make_url(n):
# # #     b="www."+n+".com"
# # #     return b
# # #
# # # print(make_url("naver"))
# # #
# # # #
# # # # # 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# # # # # make_list("abcd")
# # # # # ['a', 'b', 'c', 'd']
# # #
# # # def make_list(n):
# # #     s=[]
# # #     for i in range(len(n)):
# # #         s.append(n[i])
# # #         return s
# # #
# # #
# # #
# # #
# # #
# # # #
# # # # def make_list(n):
# # # #     s=[]
# # # #
# # # #     for i in range(len(n)):
# # # #         s.append(n[i])
# # # #     return s
# # # #
# # # #
# # # #
# # # # print(make_list("abcd"))
# # # #
# # # #
# # #
# # # #
# # # #
# # # # # 16. 게임 기업 입사문제
# # # # # 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# # # # #
# # # # # 예를 들어
# # # # # d(91) = 9 + 1 + 91 = 101
# # # # # 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# # # # # 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# # # # 그런데 반대로, 제네레이터가 없는 숫자들도 있으며,
# # # # # 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# # # # 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# # # # # 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
# # # # for i in range(1,5001):
# # # #     num=str(i)
# # # #     cnt=0
# # # #     for j in range(len(num)):
# # # #         num_int=int(num)
# # # #     cnt+=num_int
# # # #
# # #
# # # # mylist=[]
# # # # for i in range(1,5001):
# # # #     cnt=0
# # # #     n=str(i)
# # # #     for j in range(len(n)): #
# # # #         cnt+=int(j)
# # # #     d=i+cnt
# # # #     mylist.append(d)
# # # #     print(mylist)
# # #
# # #
# #
# #
# # # #
# mylist=[]
# for i in range(1,5001):
#     cnt=0
#     for j in str(i):
#         cnt+=int(j)
#     cnt+=i
#
# print(sum(set(range(1,5000))-set(mylist)))
# #
# #
# # generator=[]
# # for i in range(1,5001):
# #
# #     int_to_str = str(i) #int_to_str: i를 문자열로 변환
# #
# #     summ = 0
# #
# #     for j in range(len(int_to_str)): #각 자리수(1의자리, 10의자리,,..) 더하기 = summ
# #
# #         num_list =int(int_to_str[j])
# #
# #         summ+=num_list
# #
# #         gen_num= i+summ #원래 숫자 + 자리수 합
# #
# #         generator.append(gen_num)
# #
# #         print(generator)
# #
# # all_num = list(range(1,5001))
# #
# # final =list(set(all_num)-set(generator)) # (1~5000)에서 generator를 가진 숫자 제거
# # #
# # #
# # # #
# # # #
# # # myList = []
# # #
# # # for i in range(1,5000):
# # #     cnt = 0
# # #     for j in str(i):
# # #         cnt += int(j)
# # #     cnt += i
# #
# # #
# # # print(sum(set(range(1,5000)) - set(myList)))
# #
# # #
# # # # #
# # # # # 출력->최대 낙차: 7
# print("\n#17")
# # 17. 최대낙차
# # 최대 낙차 : 7
# box=[7,4,2,0,0,6,0,7,0]
# drop2=[]
# for i in range(len(box)):
#     drop1=[]
#     for j in box[i+1:]:
#         if box[i]>j:
#             drop1.append(j)
#     drop2.append(len(drop1))
# print("최대 낙차 :",max(drop2))
#
#
#
#
#
#
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # 단수를 입력 받아 구구단 계산
# # # # 예)
# # # # 구구단 단수 입력: 3
# # # # 3x1=3
# # # # 3x2=6
# # # # .....
# # # # 3x9=27
# # #
# # #
# # # # a=int(input("구구단 단수 입력: "))
# # #
# # # for i in range(2,20): #i는 2부터 9까
# # #     for j in range(1,10):  #j는 1부터 9까
# # #         print("{}x{}={}".format(i,j,i*j))
# # #     print("")
# # #
# # #
# # #
# # # #
# # # # 12345
# # # # 23456
# # # # 34567
# # # # 45678
# # # # 56789
# # #
# # # #
# # # # for i in range(1,6):            #   i =      1     /     2      /  3
# # # #     for j in range(i,i+5):      #   j =  1 2 3 4 5 / 2 3 4 5 6 /
# # # #         print(j,end="")
# # # #     print("")
# # #
# # #
# # # #
# # # # 56789
# # # # 45678
# # # # 34567
# # # # 23456
# # # # 12345
# # #
# # # # for i in range(5,0,-1):
# # # #     for j in range(i,i+5):
# # # #         print(j,end="")
# # # #     print("")
# # #
# # #
# # #
# # # # 시작 단 입력 : 2
# # # # 끝 단 입력 : 7
# # # #
# # # # 2 x 1 = 2
# # # # .....
# # # # 7 x 9 = 63
# # #
# # #
# # # #
# # # # a=int(input("시작 단 입력 : "))
# # # # b=int(input("끝 단 입력 : "))
# # # #
# # # # for i in range(a,b+1):
# # # #     for j in range(1,10):
# # # #         print("%dx%d=%d"%(i,j,i*j))
# # # #     print("")
# # #
# # #
# # #
# # #
# # # # *
# # # # **
# # # # ***
# # # # ****
# # # # *****
# # #
# # #
# # # for i in range(1,6):
# # #
# # #
# # #     for j in range(i):
# # #         print("*",end="")
# # #     print("")
# # #
# # #
# # # #     *
# # # #    **
# # # #   ***
# # # #  ****
# # # # *****
# # #
# # # for i in range(1,6):
# # #
# # #     for j in range(5-i):
# # #         print(" ",end="")
# # #         for k in range(i):
# # #             print("*",end="")
# # #     print("")
# # #
# # #
# # #
# # # #     i = 1~5
# # # #        print(1)
# # # #        j = 1~5
# # # #           print(2)
# # # #           k = 1~3
# # # #               print(3)
# # # #        print(4)
# # a)) # (1~5000)에서 generator를 가진 숫자 제거
# #             print("*",end="")
# #     print("")
# #
# #
# #
# # #     i = 1~5
# # #        print(1)
# # #        j = 1~5
# # #           print(2)
# # #           k = 1~3
# # #               print(3)
# # #        print(4)
# a)) # (1~5000)에서 generator를 가진 숫자 제거