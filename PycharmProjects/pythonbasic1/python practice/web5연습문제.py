# # 1.
a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
# # 앞쪽 절반을 출력해 보세요.
print(a[:len(a)//2])



# # 뒤쪽 절반을 출력해 보세요.

print(a[len(a)//2:])

# # 거꾸로 출력해 보세요.
print(a[::-1])

# # 거꾸로 짝수 번째만 출력해 보세요.

print(a[::-2])

# # 거꾸로 홀수 번째만 출력해 보세요.

print(a[-2::-2])




# 2.
# 피보나치 수열 구하기
# 13
# 피보나치 수열이란, 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다.

# 예) 0, 1, 1, 2, 3, 5, 8, 13
#
# 인풋을 정수 n으로 받았을때, n 이하까지의 피보나치 수열을 출력하는 프로그램을 작성하세요
#풀이1
# def fibonacci(n):
#     li=[0,1]
#     p=0
#     while True:
#         if li[len(li)-1] >n:
#             del li[len(li)-1]
#             break
#         li.append(li[p]+li[p+1])
#         p=p+1
#     print(li)
#
# fibonacci(10)




#
# n=int(input("수를 입력하세요:"))
# li=[0,1]
# while n >= li[-1]+li[-2]:
#     li.append(li[-1]+li[-2])
# print(li)




# 승혀니 풀이
# 2. fibonacci
#
# def fib(n):
#     fib_list = []
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# n = int(input())
# myList = []
# i = 1
# while (1):
#     if fib(i) > n:
#         break
#     myList.append(fib(i))
#     i += 1
#
# print(myList)



# 3.
# 문자열 압축하기
# 19
# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.
#
# 입력 예시: aaabbcccccca
#
# 출력 예시: a3b2c6a1



# 승혀니 풀이

# aaabbcccccca
# 3
#bbba
# myStr = input()
# myList = []
# char = myStr[0]
# cnt = 1
# for i in range(1, len(myStr)):
#     if myStr[i] == char:
#         cnt += 1
#         if i == (len(myStr)-1):
#             myList.append(char)
#             myList.append(cnt)
#     else:
#         myList.append(char)
#         myList.append(cnt)
#         char = myStr[i]
#         cnt = 1
#         if i == (len(myStr)-1):
#             myList.append(char)
#             myList.append(cnt)
#
#
# for i in myList:
#     print(str(i), end='')



#abbbcc
#s=a/bbb/cc
# s=input('압축할 문자열 : ')
# k=0
# while s[k:]!='':
#     if k+1>=len(s):
#         break
#     if s[k]!=s[k+1]:
#         s=s[:k+1]+'/'+s[k+1:]
#         k+=2
#     else:
#         k+=1
# s=s.split('/')
# #a bbb cc
# converted=''
# for k in range(len(s)):
#     converted+=s[k][0]+str(len(s[k]))
# print(converted)





    # import re
    #
    # input_data = "aaabbcccccca"
    #
    # filted = re.findall("(\\w)(\\1*)", input_data)
    #
    # output = ""
    # for x, y in filted:
    #     output += x
    #     if not len(y) == 0:
    #         output += str(len(y) + 1)
    #
    # print(output)




# 4.
# 10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
# 14
# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
#
# 10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 15 = 1 * 5 = 5
#
# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

# 4
myList = []

for i in range(10, 1001):
    num = 1
    for j in str(i):
        # print(j)
        num *= int(j)
    myList.append(num)
print(sum(myList))

#다른풀이

# def mulSum(range1,range2):
#     mul=('*'.join(str(x)) for x in range(range1,range2+1))
#     sum=eval('+'.join(mul))




#
# def multi(list):
#     res=1
#     for i in list:
#         res*=i
#     return res
#
#
# def multi_sum(n1,n2):
#     res=0
#     for i in range(n1,n2+1):
#         res+=multi(map(int,str(i)))
#     print(res)
#
# multi_sum(10,1000)
#

# 5.
# 애니팡
# 타일판은 5 × 5
# 타일 종류는 1 ~ 4의 네 가지
# 가로나 세로로 3개 이상 같은 타일이 연속될 경우 펑! 사라지고, 그 자리에는 위쪽의 타일들이 내려와서 메꿉니다.
# 내려오면서 비게 된 자리는 0으로 채워집니다.
# 위의 규칙대로 동작하는 프로그램을 작성해주세요.
#
# 입력 형식
# 아래 예와 같은 5 × 5 숫자 배열을 리스트에 저장한 뒤 문제 해결하세요
#
# 2 4 1 2 1
# 3 4 2 3 3
# 2 4 1 2 2
# 4 4 4 1 2
# 4 2 3 3 2
#
# 출력형식
# 같은 타일들을 모두 처리한 후의 최종 5 × 5 숫자 배열
#
# 0 0 0 0 0
# 2 0 0 0 0
# 3 0 0 0 0
# 2 0 0 2 0
# 4 0 1 3 0



# 5.
# 애니팡
# 타일판은 5 × 5
# 타일 종류는 1 ~ 4의 네 가지
# 가로나 세로로 3개 이상 같은 타일이 연속될 경우 펑! 사라지고, 그 자리에는 위쪽의 타일들이 내려와서 메꿉니다.
# 내려오면서 비게 된 자리는 0으로 채워집니다.
# 위의 규칙대로 동작하는 프로그램을 작성해주세요.
#
# 입력 형식
# 아래 예와 같은 5 × 5 숫자 배열을 리스트에 저장한 뒤 문제 해결하세요
#
# 2 4 1 2 1
# 3 4 2 3 3
# 2 4 1 2 2
# 4 4 4 1 2
# 4 2 3 3 2
#
# 출력형식
# 같은 타일들을 모두 처리한 후의 최종 5 × 5 숫자 배열
#
# 0 0 0 0 0
# 2 0 0 0 0
# 3 0 0 0 0
# 2 0 0 2 0
# 4 0 1 3 0
# lis = []
# for i in range(5):
#     lis.append(list(map(int, input().split())))

lis = [[2, 4, 1, 2, 1], [3, 4, 2, 3, 3], [2, 4, 1, 2, 2], [4, 4, 4, 1, 2], [4, 2, 3, 3, 2]]


#1. 3개이상 만나면 팡되는 코드

pang = 0
for i in range ( 5 ):
    for j in range ( 2, 5 ):
        if lis[i][j] == lis[i][j - 1] == lis[i][j - 2]:   #가로줄 팡
            lis[i][j - 2] = 0
            lis[i][j - 1] = 0
            lis[i][j] = 0

        elif lis[j][i] == lis[j - 1][i] == lis[j - 2][i]:  # 세로줄 팡
            lis[j][i] = 0
            lis[j - 1][i] = 0
            lis[j - 2][i] = 0


# 2. 0이 되면 내려가는 코드

res = True
while res:
    for i in range ( 4, -1, -1 ):
        for j in range ( 4, -1, -1 ):
            if lis[i][j] == 0:   #5번째줄부터 0이 있다면
                if i == 0:     #첫번째줄이라면
                    lis[i][j] == 0   #0
                else:           #첫번째줄 아니면
                    for k in range ( i, 0, -1 ):   #한칸씩 내려오기
                        lis[k][j] = lis[k - 1][j]
                    lis[0][j] = 0
    #더 내려올 것이 없는지 확인
    for i in range ( 4 ):
        for j in range ( 5 ):
            if lis[4][j] == 0 and lis[i - 1][j] != 0:   # 마지막줄이 0인데 그 위가 0이 아닌 숫자라면
                res = True   # 과정 다시 반복
            else:
                res = False   #그렇지 않다면 while문 빠져나오기



# 1+2 합친코드
# 1과 2를 계속 반복하면 결과대로 나오지만, 두개를 합친 코드를 작성했을때 원활하게 작동하지 않습니다.
# 어떤 부분이 문제인지 잘 모르겠습니다.




lis = [[2, 4, 1, 2, 1], [3, 4, 2, 3, 3], [2, 4, 1, 2, 2], [4, 4, 4, 1, 2], [4, 2, 3, 3, 2]]

cont=True
while cont:
    # 3개 이상 만나면 팡되는 코드
    pang = 0
    for i in range ( 5 ):
        for j in range ( 2, 5 ):
            if lis[i][j] == lis[i][j - 1] == lis[i][j - 2]:   #가로줄 팡
                pang = 1
                lis[i][j - 2] = 0
                lis[i][j - 1] = 0
                lis[i][j] = 0

            elif lis[j][i] == lis[j - 1][i] == lis[j - 2][i]:  # 세로줄 팡
                pang = 1
                lis[j][i] = 0
                lis[j - 1][i] = 0
                lis[j - 2][i] = 0

    if pang==1:
        cont = True
    else:
        break
    # lis = [[2, 4, 1, 2, 1],
    #       [3, 4, 2, 3, 3],
    #       [2, 4, 1, 2, 2],
    #       [4, 4, 4, 1, 2],
    #       [4, 2, 3, 3, 2]]
    # 터트리고 내려오는 코드
    res = True
    while res:
        for i in range ( 4, -1, -1 ):
            for j in range ( 4, -1, -1 ):
                if lis[i][j] == 0:   #5번째줄부터 0이 있다면
                    if i == 0:     #첫번째줄이라면
                        lis[i][j] == 0   #0
                    else:           #첫번째줄 아니면
                        for k in range ( i, 0, -1 ):   #한칸씩 내려오기
                            lis[k][j] = lis[k - 1][j]
                        lis[0][j] = 0
        #더 내려올 것이 없는지 확인
        for i in range ( 4 ):
            for j in range ( 5 ):
                if lis[4][j] == 0 and lis[i - 1][j] != 0:   # 마지막줄이 0인데 그 위가 0이 아닌 숫자라면
                    res = True   # 과정 다시 반복
                else:
                    res = False   #그렇지 않다면 while문 빠져나오기

print(lis)




#강사님 코드


