# def 함수명(매개변수 0개 이상):
#     문장1
#     문장2
#함수 정의 구문

#함수 호출 구문
#
# def add(a, b): #사용자 함수(매개변수)
#     sum=a+b
#     print("add함수")
#     return sum
#
# print("호출전")
# res=add(1,2) #parameter(인수)
# print("호출후")
# print(res)
# # 수행순서
# # 함수는 스스로 수행하지 않는다. 호출해야만 수행
# # 1) add(1,2) 호출
# # 2) add함수 수행 -> sum 리턴
# # 3) sum이 res에 저장
#
#
# #입력값이 없는 함수
# def say():
#     return "안녕"
# s=say()
# print(s)
#
# #출력값이 없는 함수(return문이 없는 함수)
# def add(a,b):
#     print("두 수의 합은 : ",a+b)
#
# res=add(3,4)
# print(res)
#
# #입력값/출력값 없는 함수
# def say():
#      print("안녕")
#      #return 생략
# say()
#
# #매개변수의 초기값을 설정하여 함수 호출
# def add(a,b):
#     print(b)
#     print(a)
#     return a+b
# res=add(2,3)
# print(res)


# def add(a,b=3):
#     print(b)
#     print(a)
#     return a+b
# res=add(2)
# print(res)


# def add(a=1,b=3): #외부에서 전달되는 값이 있으면 저장, 없으면 기본값 3이 저장
#     print(b)
#     print(a)
#     return a+b
# res=add(10,20)
# print(res)
#
#
# #함수로 전달되는 인수의 개수가 정해져 있지 않은 경우
# def add(*arg): #매개변수(agruments) 명 앞에 *을 붙이면 튜플로 인식
#     print(arg)
#     res=0
#     for i in arg:
#         res+=i
#     return res
# r=add(1,2,3,4,5)
# print(r)
#
#
# def mul(*arg):
#     res=1
#     for i in arg:
#         res*=i
#     return res
# #     구문 완성
# res=mul(1,2,3) #인수가 가변적
# print(res) #6출력
#
#
# def addmul(op, *arg):
#     if op=="add":
#         res=0
#         for i in arg:
#             res+=i
#
#     elif op=="mul":
#         res=1
#         for i in arg:
#             res*=i
#     return res
#
# #addmul(연산종류(add/mul), 피연산자들)
# res=addmul("add",1,2,3,4) #인수가 가변적
# print(res) #1+2+3+4의 결과가 출력
#
# res=addmul("mul",1,2,3,4,5) #인수가 가변적
# print(res) #1*2*3*4*5의 결과가 출력


# def am(a,b):
#     return a+b, a*b #함수의 결과는 항상 1개. 튜플형식으로 (덧셈,곱셈) 리턴
# # res=am(3,4)
# # r1=res[0]
# # r2=res[1]
# #print(r1)
#
# r1,r2=am(3,4)
# print(r1)
# print(r2)

#return 문은 1개 작성
# def am(a,b):
#     return a+b
#     return a*b
# print(am(1,2))

#
# def prn():
#     print("안녕")
#     return #생략 가능
#
# prn()
# print("하세요")



# def prn(a):
#     if a=="안녕":
#         return
#     print("반가워")
#
# prn("잘 있었니?")
#
#
# def say(name, old, man=True):   #매개변수를 작성하세요
#     #코드를 구현하시오
#     print("내 이름은", name)
#     print("나이는 ", old)
#     if man:
#         print("성별은 남")
#     else:
#         print("성별은 여")
# #say('홍길동', 25)
# #say('홍길동', 25, True)
# #say('김말순', 26, False)
# say('김말순', 26)
# #
# # # 내 이름은 홍길동
# # # 나이는 25
# # # 성별은 남
# # say('홍길동', 25, True)
# # # 내 이름은 홍길동
# # # 나이는 25
# # # 성별은 남
# # say('김말순', 26, False)
# # # 내 이름은 김말순
# # # 나이는 26
# # # 성별은 여
# # say('김말순', 26)
# # # 내 이름은 김말순
# # # 나이는 26
# # # 성별은 남
#
#
# a=1 #함수 밖에 있는 a
# def mytest(a): #매개변수 a는 함수 안에서만 사용되는 변수임. 함수 밖에 있는 a가 아님
#     a=a+1
# mytest(10)
#
#
# def mytest2(z):
#     z=z+1
#     print(z)
# mytest2(3)
# z=5
# print(z)
#
# #scope
#
#
# a=1
# def mytest3(a):
#     a=a+1 #함수 안에서 밖에 있는 변수를 증가하고 싶다면? 2가지 방법 존재( , global)
# mytest3(a)
# print(a) #2가 출력됐으면...
#
# #1. return사용
# a=1
# def mytest3_1(a):
#     a=a+1 #함수 안에서 밖에 있는 변수를 증가하고 싶다면? return
#     return a
# a=mytest3_1(a)
# print(a) #2가 출력
#
# #2. global 사용 : 함수 안에서 함수 밖의 변수를 직접 사용 가능
# a=1
# def mytest3_2():
#     global a
#     a=a+1
# mytest3_2()
# print(a)
#
# #lambda:def와 동일한 기능 수행하는 예약어
# #함수 정의시 일반적으로는 def를 사용. 함수가 복잡하거나 def를 사용하지 못하는 곳에서는 람다 사용
# print("="*50)
# #1. def를 이용한 일반적인 함수 정의
# def myadd(a,b):
#     return a+b
# res=myadd(2,3)
# print(res)
#
# #2. 람다를 이용한 함수 정의
# myadd2=lambda a,b:a+b
# #함수명=lambda 매개변수1, 매개변수2, ...:매개변수를 이용한 계산식
# res=myadd2(2,3)
# print(res)

#퀴즈:카페에 업로드
# def mymax(*arg): #구현
#     #print(max(arg))
#     #for문 구현
#     m=0
#     for i in range(len(arg)):
#        if m<arg[i]:
#            m=arg[i]
#     return m
# print("최대값 : ",mymax(5,1,3,2)) #5
# print("최대값 : ",mymax(2,7,9)) #9


#일반 함수 형식
# def pt(x):
#     return x+10
# print(pt(1))

#람다 함수 형식
# pt=lambda x:x+10
# print(pt(1))

#람다 함수 자체를 바로 호출
#(lambda 매개변수들:수식)(인수들)
print((lambda x:x+10)(1))

print((lambda x,y:x+y)(1,2))

#람다 함수 내에서는 변수를 생성할 수 없음
#print((lambda x:y=2; x+y)(1)) 문법 오류,   아래와 같이 작성해야 함
# y=2
# print((lambda x:x+y)(1))
#
# print((lambda x,y=3:x+y)(1))

#함수의 인수 부분에 간단한 함수를 적용하고자 하는 경우
# def pt(x):
#     return x+10
# print(list(map(pt,[1,2,3] ))) #map -> list

def pt2(x):
    return x+10
print(list(map(pt2, [1,2,3])))
#map(함수, 데이터)

print(list(map(lambda x: x+10, [1,2,3])))

#람다식으로 매개변수가 없는 함수 표현
print((lambda : 1)())

x=10
print((lambda : x)())

#퀴즈2
fl=['test.c', 'test2.h', 'sample.py', 'sample2.c']
#확장자가 c이거나 h인 파일 이름을 모두 화면에 출력#
#코드를 카페에 업로드

fl=['test.c','test.h','sample.py','sample2.c']
# 확장자가 c이거나 h인 파일 이름을 모두 화면에 출력
for k in fl:
    c=k.split('.')[1]
    if c=="c" or c=="h":
        print(k)

fl=['test.c','test.h','sample.py','sample2.c']
for f_name in fl:
    if f_name.endswith('.c') or f_name.endswith('.py'):
        print(f_name)

