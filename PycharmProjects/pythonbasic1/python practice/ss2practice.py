# # 1.
# # 초기 투자액과 투자 기간, 그리고 투자 기간 중 날짜별 가치 변동율이 주어질 때 순이익과 이익 여부를 구합니다.
# #
# # 입력
# # 첫째 줄에 투자액이 정수로 주어집니다. 두번째 줄에 투자기간이 정수로 주어집니다.
# # 세번째 줄에 투자기간 중 일별 전일 대비 가치 변동이 각각 퍼센트 단위의 정수로 주어집니다.
# #
# # 투자액은 100 이상 10000 이하의 정수입니다.
# # 투자 기간은 1 이상 10 이하의 정수입니다.
# # 일별 변동폭은 -100 이상 100 이하의 정수로 주어집니다.
# # 출력
# # 첫째 줄에 순이익을 소수점 첫째자리에서 반올림한 값으로 나타냅니다.
# # 두번째 줄에 이익인지 손해인지 여부를 good, same, bad로 나타냅니다.
# # 이익이면 good, 손해이면 bad, 첫째줄에서 출력한 순이익이 0이면 same울 출력합니다.
# #
# # 예시
# # 입력 예시
# # 10000
# # 4
# # 10 -10 5 -5
# #
# # 출력 예시
# # -125
# # bad
#
# # invest = int(input())
# # period = int(input())
# # daily = list(map(float, input().split(' ')))
# #
# #
# # def investment(invest, daily):
# #     invest2 = invest
# #     for i in daily:
# #         if i != 0:
# #             invest2 = invest2 * ((100 + i) / 100)
# #         else:
# #             pass
# #
# #     return (round(invest2) - invest)
# #
# #
# # res = investment(invest, daily)
# # print(res)
# #
# # if res > 0:
# #     print("good")
# # elif res < 0:
# #     print("bad")
# # else:
# #     print("same")
#
# # 2.
# # 골드바흐의 추측(Goldbach's conjecture)은 오래전부터 알려진 정수론의 미해결 문제로,
# # # 2보다 큰 모든 짝수는 두 개의 소수(Prime number)의 합으로 표시할 수 있다는 것이다.
# # # 이때 하나의 소수를 두 번 사용하는 것은 허용한다.
# # #
# # # 2보다 큰 짝수 n을 입력 받으면, n=p1+p2 를 만족하는 소수 p1,p2의 페어를 모두 출력하는 프로그램을 작성하시오.
# #
# # 입력예1: n=26
# #
# # 출력예1: [[3, 23], [7, 19], [13, 13]]
# #
# # 입력예2: n=48
# #
# # 출력예2 [[5, 43], [7, 41], [11, 37], [17, 31], [19, 29]]
# #
# # n=int(input('Input a number...'))
# # li=[]
#
# # for i in range (2,n+1): #   i=5
# #     j=2
# #     while (j<=i):
# #         if i%j==0:
# #             if i==j:
# #                 li.append(j)
# #             else:
# #                 break
# #         j+=1
# #
# # result=[]
# # for n1 in range(2,int(n/2)+1):
# #     temp=[]
# #     if n1 in li:
# #         n2=n-n1
# #         if n2 in li:
# #             temp.append(n1)
# #             temp.append(n2)
# #             result.append(temp)
# #
# # print (result)
#
#
# #숭혀니 풀이
#
#
# num = int(input())
#
# #소수를 구하는 함수
# def prime(num):
#     myList = []
#     if num < 2:
#         return myList
#     else:
#         for i in range(2, num):
#             if i == 2:
#                 myList.append(2)
#             else:
#                 for j in range(2, i):
#                     if i % j == 0:   #나눠지는 수가 있으면 break
#                         break
#                     elif j == i - 1:  #마지막까지 돌아도 나눠지는 수 없으면 append
#                         myList.append(i)
#     return myList
#
#
# myList2 = prime(num)
#
# def Goldbach(myList2):
#     ans = []
#     for i in range(len(myList2)):
#         for j in range(i, len(myList2)):
#             if myList2[i] + myList2[j] == num:
#                 ans.append([myList2[i], myList2[j]])
#
#     return ans
#
#
# print(Goldbach(myList2))
#
# # num = int(input('2보다 큰 짝수를 입력해주세요 : '))
# # ans = []
# #
# # def chk(n): #소수구하는 함수
# #     for i in range(2,n):
# #         if n%i==0: #2부터 n-1까지 나누어지는 수가 있다면
# #             break #break
# #     if i==(n-1): #위의 break에 걸리지 않았다면 소수
# #         return n #n을 리턴
# #     else:
# #         return False #아니라면 False
# #
# # for j in range(3, num//2+1): # 3부터 입력받은 수의 절반까지 for문
# #     if chk(j): # 만약 j가 소수라면
# #         if chk(num-j): # 입력받은 수 - j가 소수라면
# #             ans.append([j, num-j]) # 답 집어넣기
# #
# # print(ans)
#
#
# #다른 분 풀이
# def getPrime(n):
#     primes = [2]
#     for i in range(2, n+1):
#         a = 0
#         for j in primes:
#             if i % j == 0:
#                 a = 1
#                 break
#         if a != 1:
#             primes.append(i)
#     return primes
#
# def getPrimePair(n):
#     primes = getPrime(n)
#     prime_pair =[]
#     for i in primes:
#         if n-i in primes and i <= n-i:
#             prime_pair.append([i, n-i])
#         if i > n-i:
#             break
#     return prime_pair
#
# # 3.
# # 아마존 면접문제
# #
# # 다음과 같은 형태의 배열을
# #
# # [a1,a2,a3...,an,b1,b2...bn]
# #
# # 다음과 같은 형태로 바꾸시오
# #
# # [a1,b1,a2,b2.....an,bn]
# #
# #
# #1번풀이
# def sort(li):
#     return sorted(li,key=lambda x:x[1])
#
# print(sort(['a1','a2','a3','an','b1','b2','bn']))
#
#
# #2번풀이
#
# def amazon(li):
#     res=[]
#     new=[]
#
#     for i in li:
#         new.append((i[1],i[0]))
#
#     for i in sorted(new):
#         res.append((i[1]+i[0]))
#     return res
#
# print(amazon(['a1','a2','a3','an','b1','b2','bn']))
#
#
#
#
# #
myList = ['a1', 'a2', 'a3', 'an', 'b1', 'b2', 'bn']

for j in range(len(myList)):
    for i in range(len(myList) - 1):
        if myList[i][1] > myList[i + 1][1]:
            temp = myList[i]
            myList[i] = myList[i + 1]
            myList[i + 1] = temp

print(myList)