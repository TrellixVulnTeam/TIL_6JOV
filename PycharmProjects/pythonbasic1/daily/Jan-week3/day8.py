#1.
# number_list = [1, 3, 4, 8, 13, 17, 20]
# def find_shortest(number_list):
#     result = 0
#     min_val = max(number_list)-min(number_list) #20-1=19
#     for i in range(len(number_list)-1): #0~5
#         val = number_list[i+1] - number_list[i]
#         if min_val > val:
#             min_val = val
#             result = i
#     return print(number_list[result], number_list[result+1])
# find_shortest(number_list)

#2.
# w=input("단어 입력 : ")
# isPalindrome=True #회문 여부, 초기값은  true
#
# #중간 공백 제거
# w=w.replace(" ","")
#
# for i in range(len(w)//2):
#     if w[i] != w[-1-i]: #왼쪽문자와 오른쪽문자가 다른 경우
#         isPalindrome=False
#         break
# print(isPalindrome)

#nurses run => nursesrun
#공백문자 -> 전처리(제거)

#
# w=input("단어 입력 : ")
# #공백제거 전처리
# # print(w==w[::-1])
# # print(w)
# # print(w[::-1])
#
# print(list(w)==list(reversed(w)))
# #level=> [l,e,v,e,l]
#문자열을 리스트에 저장하면 문자 하나 하나가 리스트 요소

# w='level'
# print(w)
# print(''.join(reversed(w)))
#
# print(w==''.join(reversed(w)))

#map(함수, 자료)

#퀴즈1. 카페 제출
#def twoTimes(n):
    #1.
#   return [2*i for i in n]
#2.
    # nlist = []
    # for x in n:
    #     x *= 2
    #     nlist.append(x)
    # return nlist

#3.
    # res = list(map(lambda x: x * 2, n))
    # return res

#4. map활용
# def twoTimes(n):
#     return n*2
# res=list(map(twoTimes, [1,2,3]))
# print(res) #[2,4,6]
#
# print(list(map(lambda x: x * 2, [1,2,3])))

print(pow(3,2))
print(3**2)

print(round(3.141592,4))

print(list(zip([1,2],[3,4],[5,6],[7,8])))

# filter:특정 조건으로 걸러진 요소들을 묶어서 리턴, map과의 차이점이라면, 함수의 결과가 참/거짓인지에
# 따라 요소를 포함할지를 결정

t=list(range(1,11))
print(t)
#짝수 리스트를 출력
#1. for
def isEven(n):
    return True if n % 2==0 else False   #n이 2로 나누어 떨어지면 True, 아니면 False 리턴
# res=[]
# for v in t:
#     if isEven(v):
#         res.append(v)
# print(res)

#2. filter
print(list(filter(isEven, t)))

#3. lambda
print(list(filter(lambda x: x%2==0, t)))

#os 모듈:디렉토리, 파일의 경로 등 확인/제어
import os
print(os.environ)

print(os.getcwd()) # 현재 작업 경로
#os.mkdir("sample") #현재 작업 위치에 폴더 생성
#os.rmdir("sample")
#os.rename("sample", "test") #폴더명 변경
#os.renames("hello.txt", "hi.txt")

import shutil
shutil.copy("hi.txt", "hicopy.txt") #파일 복사

#특정 폴더 내에 있는 폴더 또는 파일 목록 등을 조사
import glob
#모든 파일 목록 출력
#print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*"))

#파일 확장자가  py인 파일들을 출력
print(glob.glob("C:/Users/i/PycharmProjects/pythonBasic/*.py"))




ß









