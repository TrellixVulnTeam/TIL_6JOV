# 1~10000 까지 8의 개수?
# 1~9999
#
# 0001
# ...
# 9999
# 1000 * 4 = 4000개
#
# 1~9999


#8128 => 8이 2개
#count : 문자열 관련하여 특정 문자의 개수를 세는 함수

#print(8128.count())

#print("hello".count('l'))


# sum=0
# for i in range(10001):
#     sum+=str(i).count('8')
# print(sum)
#
#print(str(list(range(1,10001))).count('8'))


# a=[111,222,321] #정수 리스트
# #print(a[0]+10)
# #print(str(a[2]).count('1'))
#
# a=str(a)
# print(a)
# print(a.count('1'))


"""
입출력 종류: 표준, 파일, 네트워크
파일 입출력
-파일 열기(open) -> 파일 입력(read)/출력(write) -> 파일 닫기(close)
휴대폰-메모리(램) 2GB-게임(1GB),음악(500MB),인터넷(500MB) => 외부 전화가 걸려옴(전화앱 실행)
=>결론 : 메모리 관리를 소홀히 하지 말자!
"""

# #파일에 문자열 출력(쓰기)
# f=open("hello.txt","w") #파일을 쓰기 용도로 열기
# #open(파일명,모드)
# #프로그램 상에서는 쓰기 모드로 열려있는 hello.txt파일이 f라는 이름으로 사용됨
# f.write('hello world')
# f.close()
#
#
# #파일로부터 문자열 입력(읽기)
# f=open("hello.txt", "r")
# s=f.read()
# print(s)
# f.close()

#with ~ as 구문은 파일을 사용한 뒤에 자동으로 파일을 닫아줌
# with open(파일이름, 모드) as 파일변수:
#     코드

# with open("hello.txt", "r") as f:
#     s=f.read()
#     print(s)
#close 작업을 자동으로 수행

#파일에 여러 줄 출력

# hello world 1
# ...
# hello world 10

#w모드로 열게되면 기존에 작성되어 있던 내용은 사라짐
# with open("hello.txt", "w") as f:
#     for i in range(10):
#         f.write("hello world {0}\n".format(i+1))

#리스트의 내용을 파일에 출력
# lines=['hello\n', 'nicetomeetyou\n', 'bye\n']
# with open("hello.txt", "w") as f:
#     f.writelines(lines)

# with open("hello.txt", "r") as f:
#     s=f.read() #read함수는 1글자씩 읽어들임
#     print(s)

# with open("hello.txt", "r") as f:
#     line=None
#     while line !="":
#         line=f.readline() #readline함수는 1줄씩 읽어들임(for 또는 while 문과 함께 사용)
#         #print(line) #2줄이 바뀜
#         print(line.strip("\n")) #\n을 삭제

# with open("hello.txt", "r") as f:
#     line=f.readlines()
# #    for i in range(len(line)):
#     for i in line:
#         print(i.strip("\n"))


#인코딩 에러 발생시
#file->settings->editor->file encodings->project encoding -> utf-8로 변경


#피클(pickle):파이썬 객체를 파일로 저장하고자 하는 경우에 사용되는 모듈
# 피클링 : 객체 -> 파일
# 언피클링 : 파일 -> 객체

# hello
# nicetomeetyou
# bye

#kim, 단팥
#서울시 강남구, 노랑
#23, 너비(20)
#컴퓨터, 높이(10)

#lee, 크림
#서울시 강북구, 파랑
#33, 너비(21)
#국어, 높이(12)


#객체를 파일로 저장
import pickle
내용물="단팥"
색상="파랑"
너비="20센티"
높이="10센티"
가족명단={"잉어":30, "꽃게":10, "상어":40}
#객체 저장할때는 wb 모드로 파일 열기
with open("myfish.p", "wb") as f:
    pickle.dump(내용물, f)
    pickle.dump(색상, f)
    pickle.dump(너비, f)
    pickle.dump(높이, f)
    pickle.dump(가족명단, f)

import pickle
with open("myfish.p", "rb") as f:
    내용물=pickle.load(f)
    색상=pickle.load(f)
    너비=pickle.load(f)
    높이=pickle.load(f)
    가족명단=pickle.load(f)

    print(내용물)
    print(색상)
    print(너비)
    print(높이)
    print(가족명단)

f=open("hello.txt", "a")
for i in range(3):
    f.write("%d번째 줄 추가\n" % (i+1))
f.close()




# 클래스?붕어빵기계
# 객체?붕어빵
# 메서드(동작)?굽는다,...뒤집는다, ...
# attribute(속성)?내용물, 크기, 모양,...너비, 높이

# res=0
# def add(n):
#     global res
#     #n에 전달된 값을 res에 저장
#     res+=n
#
# add(3)
# print(res)
# add(4)
# print(res)


res1=0 #전역변수
res2=0
#편의점->계산대->계산기 2대->

#1번째 계산대
def add1(n): #지역변수
    global res1
    #n에 전달된 값을 res에 저장
    res1+=n
    #res=res*0.9
    return res1
print(add1(3000))
print(add1(5000))

#2번째 계산대
def add2(n): #지역변수
    global res2
    #n에 전달된 값을 res에 저장
    res2+=n
    return res2
print(add2(1500)) #막걸리
print(add2(2000)) #두부

#클래스 : 각각의 계산대를 객체로 간주하고, 계산대의 특성 또는 동작등을 일반화시켜 놓은 틀
# 정/부정관사
# the car(객체)
# a car(클래스)

# 사람(클래스): 실체가 없음
# 사람홍길동(객체), 사람임꺽정(객체) : 실체가 있음
#
# 자동차(클래스) : 실체가 없음
# 내자동차(객체), 네자동차(객체)

class Calculator: #클래스명은 대문자로 시작, 붕어빵기계
    def __init__(self): #현재 객체를 self라고 함
        self.res=0
        print("init함수가 호출됐네?")
    def add(self, n):
        self.res+=n
        #10%할인 코드를 여기에 작성-> 모든 계산대에 공통적으로 적용
        return self.res

#Calculator():붕어빵기계에서 붕어빵을 제작 -> __init__자동호출 ->res(내용물)=msg
cal1=Calculator() #클래스로부터 객체를 생성(init 함수 자동 호출, res=0으로 초기화). 계산대(클래스)로부터 계산대1(객체==cal1)을 생성
#Calculator():붕어빵기계에서 붕어빵을 제작 -> __init__자동호출 ->res(내용물)=msg
cal2=Calculator()#클래스로부터 객체를 생성(init 함수 자동 호출). 계산대(클래스)로부터 계산대2(객체==cal2)을 생성

print(cal1.add(3000)) #붕어빵.크기(20)    크기를 20으로...
print(cal1.add(5000)) #붕어빵.너비(10)   너비를 10으로

print(cal2.add(1500))
print(cal2.add(2000))

#객체지향프로그래밍





#모듈?변수, 함수, 클래스 등을 모아 놓은 파이썬 파일. 다른 프로그램에서 모듈을 불러올 수 있음













#print(madd(1,2)) 에러

# import mod1
# print(mod1.madd(1,2))

# import mod1 as m #as : 모듈(패키지)명이 길때 축약해서 표현
# print(m.madd(1,2))

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#폴더안에는 파일/서브폴더

#import 모듈이름

#import mod1

# from mod1 import msub
# #mod1 모듈에 정의되어 있는 msub 메서드만 가져와라
# print(msub(2,1))

# from mod1 import madd
# from mod1 import msub
from mod1 import madd, msub
from mod1 import * #모든 함수를 다 가져와라



















