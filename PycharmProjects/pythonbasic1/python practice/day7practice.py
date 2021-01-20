# # 1. 다음 입사문제
# # 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# # (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# # 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
# s = [1,3,4,8,13,17,20]
# def short_pair(n):
#     list=[] #list=[2,1,4,5,5,3]
#     for i in range(len(n)-1):
#         list.append(n[i+1]-n[i])
#     for j in range(len(list)):
#         if list[j]==min(list):
#             return print(n[j],n[j+1])
# short_pair(s)
#
# 다른 사람 풀이
# number_list=[1,3,4,8,13,17,20]
def find_shortest(number_list):
    result=0
    min_val= max(number_list)-min(number_list)
    for i in range(len(number_list-1)):
        val=number_list[i+1]-number_list[i]
        if min_val>val:
            min_val =val
            result=i
    return print(number_list[result],number_list[result+1])
# find_shortest([1,3,4,8,13,17,20])








#
#
#
# myList=[]
# myList2=[]
# n = 0
# myList.append(s[1]-s[0])
# for i in range(len(s)-1):
#     n = s[i+1] - s[i]
#     if n < myList[-1]:
#         myList.append(n)
#         myList2.append((s[i],s[i+1]))
#
# print(myList2[-1])
#
#
#
#
# #입출력
#
#
#
# # 2.
# # 회문(palindrome)? 순서를 거꾸로 해서 읽어도 제대로 읽을때와 같은 단어 or 문장
# # rotator, sos, abba (nurses run)
# # 문제: 임의의 단어(문장)을 입력받아 회문 여부를 출력 => True or False 출력
# #
#  강사님 풀이
# w=input("단어 입력: ")
# ispalindrome=True
# w=w.replace(" "."")
# for i in range(len(w)//2):
#     if w[i] != w[-1-i]: #왼쪽문자와 오른쪽 문자가 다르경우
#         ispalindrome=False
#         break
# print(ispalindrome)





# w=input("단어 입력: ")
# # print(w==w[::-1])
# # print(w)
# # print(w[::-1])
#
#
# # reverse로 처리하는 법
# # list(w)
# print(list(w)==list(reversed(w)))


w='level'
print(w)
print(''.join(reversed(w)))
print(w==''.join(reversed(w)))
#
#
# d=input("입력하세요:")
# if d==d[::-1]:
#     print("Ture")
# else:
#     print("False")
#
#
#
# # 3. 어제 문제 풀어서 제출
#
#
#
# a = input("단어 혹은 문장을 입력하세요 : ")
# b = ""
#
# for i in a:
#     if i != " ":
#         b += i
#
#
# if b == b[::-1]:
#     print("True")
# else:
#     print("False")

#
#
# a=input("단수를 입력하세요:")
# for i in range(2,int(a)+1):
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)


#
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다.
# 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
#
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면,
# # 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.


# list1=[]
# a,b=input("두 수를 입력하세요: ").split(" ")

# if a[0][::-1]>a[1][::-1]:
#     print(a[0][::-1])
# else:
#     print(a[1][::-1])

# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

#
#
# a=input("단어를 입력하세요:")
# word_list=set(a)   #['a','b']
# myList=[]
# dict={}
# for i in a:
#     myList.append(i) #mylist=['a',b',b','b']
# for j in word_list:
#      dict[j]=myList.count(j)
#
#
# for k,v in dict.items():
#     if v==max(dict.values()):
#         print("{}의 개수는 {}입니다.".format(k,v))
#
#
# #2번째 풀이
#
# a=input("단어를 입력하세요:")
# mylist = []
# for i in a :
#     mylist.append(i)
# print(mylist)
#
# print(max(a), "의 개수 =", mylist.count(max(a)), "개")






























