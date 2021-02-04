# # 1. 임의의 두 수를 입력 받은 후 최소공배수/최대공약수 출력
#
# def solution(n,m):
#     for i in range(1,n+1):
#         if n%i==0:
#             if m%i==0:
#                 num1=i
#
#     if num1==1:
#         num2=n*m
#     else:
#         num2=num1*(n//num1)*(m//num1)
#     return (num1,num2)
#
# print(solution(2,5))
#
#
#
# #유클리드 호제법
# def getGcd(num1, num2):
#     while num2 != 0:
#         r = num1 % num2
#         num1 = num2
#         num2 = r
#     return num1
#
# def getLcm(num1, num2):
#     lcm = (num1 * num2) // getGcd(num1, num2)
#     return lcm
#
# #다른 분 풀이
# #재귀
# num1=20
# num2=35
# import copy
# def getc_mm(small,big):
#     if small>big:small,big=big,small
#     if big%small==0: return small,num1*(num2/small)
#     res=divmod(big,small)[1]
#     big=copy.copy(small)
#     small=res
#     return getc_mm(small,big)
#
# print(getc_mm(20,35))
#
# #반복문
# num1=20
# num2=35
# import copy
# def getc_mm(small,big):
#     if small>big:small,big=big,small
#     for i in range(small):
#         res = big % small
#         if res==0:return small,num1*(num2/small)
#         big=copy.copy(small)
#         small=res
# print(getc_mm(20,35))
#
#
#
# # 2.
# #  1~1000에서 각 숫자의 개수 구하기
# #
# # 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
# #
# # 10 = 1, 0
# # 11 = 1, 1
# # 12 = 1, 2
# # 13 = 1, 3
# # 14 = 1, 4
# # 15 = 1, 5
#
# # 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
# dic={}
# for i in range(1,1001):
#     for j in str(i):
#         if j in dic:
#             dic[j]+=1
#         else:
#             dic[j]=1
#
# print(dic)
#
#
#
# #dic = {i:0 for i in range(0,10)}
# # for i in range(1,16):
# #     for n in str(i):
# #         dic[int(n)]+=1
# # print(dic)


#강사님 풀이

count={x:0 for x in range(0,10)}

for x in range(10,16):
    for i in str(x):
        count[int(i)]+=1
print(count)
#
#
# # 3.
# # 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
# # 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는
# # (여기서는 예를 들 때 3으로 지정하였다)알파벳이 출력되는 것이다.
# # 예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
# #
# # 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을
# # 작성해라.
# #
# def Juci(str,n):
#     al="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     str=list(str)  #['c','a','t']
#     for a,b in enumerate(str):  #{0:c,1:a,2:t}
#         addw=al.index(b)+n
#         str[a]=al[addw]
#     print(''.join(str))
#
# Juci('CAT',5)
#
#
# ########################################
#
# #
# # def caesar(s, n):
# #     pre_defined = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# #     n = n % len(pre_defined)
# #     transform = pre_defined[n:] + pre_defined[:n]
# #     return ''.join([transform[pre_defined.find(_)] for _ in s])
#
# ##########################다른 분 풀이(좋은 풀이)
def caeser(sen,n):
    sen="CAAT"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t=str.maketrans(alpha,alpha[n%26:]+alpha[:n%26])
    return sen.translate(t)
print(caeser("CAT",5))
#
#
#
#
#
#
#
#
#
# # 4. 절대값의 합 구하기 (수업 시간에 설명)
# #
# import random
# lis = [[random.randint(0,5) for _ in range(5)] for _ in range(5)]
# res = 0
# for i in range(5):
#     for j in range(5):
#         if i-1 >= 0 :
#             res+=abs(lis[i][j]-lis[i-1][j])
#         if i+1<5 :
#             res+=abs(lis[i][j]-lis[i+1][j])
#         if j-1>=0:
#             res+=abs(lis[i][j]-lis[i][j-1])
#         if j+1<5 :
#             res += abs(lis[i][j]-lis[i][j+1])
# print(res)
#
#
#
#
# #다른 분 풀이
#
# #변수 지정
# #
# # - ls: 5*5 행렬
# #
# # - for문: 열 (column)의 값끼리 묶은 것을 ls에 추가함
# #
# #     ex) 원래 값: [[1, 2, 1, 4, 2], [3, 5, 2, 2, 4], [5, 5, 4, 2, 5], [3, 5, 3, 2, 1], [5, 5, 2, 4, 1]]
# #
# #           추가한 값: [1, 3, 5, 3, 5], [2, 5, 5, 5, 5], [1, 2, 4, 3, 2], [4, 2, 2, 2, 4], [2, 4, 5, 1, 1]
# #
# #
# #
# # for 문
# #
# # - ls 길이(5*2=10)만큼 for 문을 돌면서 각 행의 앞뒤 요소((0,1), (1,2), (2,3), (3,4))의 차이값의 절대값에 *2 한 것을 모두 더한 값을 출력
#
#
# def abs_sum():
#     import random
#     ls = []
#     for i in range(5):
#         ls.append([random.randint(1, 5) for _ in range(5)])
#     for i in range(5):
#         col = []
#         for j in range(5):
#             col.append(ls[j][i])
#         ls.append(col)
#
#     res = 0
#     for i in range(len(ls)):
#         for j in range(4):
#             cal = abs(ls[i][j] - ls[i][j+1]) * 2
#             res+=cal
#     return res
#
# print(abs_sum())
#
# # ls = [[1, 2, 1, 4, 2], [3, 5, 2, 2, 4], [5, 5, 4, 2, 5], [3, 5, 3, 2, 1], [5, 5, 2, 4, 1]]
# # print(abs_sum()) # 122 (검산은 안 해봤어요 ㅎㅎ)
