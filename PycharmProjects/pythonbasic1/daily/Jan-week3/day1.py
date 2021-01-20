# 파이썬?
# 매우 인간적인 언어
# 프로그래밍(언어:파이썬...)->프로그램(appication,app())
# 프로그래밍? 우리의 생각을 컴퓨터에 지시하는 행앱
#
# 1001 000100001(2진수 x) ->
#블록 처리(주석) -> command + /
#print("hi")

#if 4 in[1,2,3,4]: print("4가 있어")
# alt +f10, ctrl+shift+f10
# 자료구조: 데이터를 저장, 관리하는 방
# 리스트:[], 튜플:(), 딕셔너리,셋:{}
# 리스트는 자료구조를 ''로 구분함

#languages = ['python', 'perl', 'c', 'java']
# 변수 = 데이터 ->데이터를 변수에 저장해라

# #for lang in languages:
#     # for ->반복해라,lang(변수), languages에 있는 길이 만큼(4번)
#     #if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")
# #
# # #   유틸리티, gui, web, db, 데이터분석(파이썬에 추가적으로 패키지를 설치,파이썬 + pandas)
# #
# #
# # print("hello, world");print('bye')
# #
# # a=1
# # a=1+2
# # # a=1 -->=는 assign(할당, 왼쪽<-오른쪽)
# # # 변수=1
# #
# # # 파이썬에서는 들여쓰기가 중요(들여쓰기가 문법임)
# # # backspace key: 엔터키 위에 <-
# # # 들여쓰기 안하면 indentationError뜸
# #
# # if a ==4:
# #     print('4')
# #     print('four')
# # print('코드블록 ')
# #
# # #코드블록 -> 코드가 모여있는 상태,들여쓰기만 동일하게 하면 다 출력(들여쓰기가 동일한 코드 집합)
# #
# # print(5//3) #1몫
# # print(6//3) #2
# # print(6//3.0) #2.0 ->3.0은 실
# #
# # print(7 % 4)
# # print(2 ** 3)
# # print(2 ** 10000)
#
# # print(int(3.3))
# # print(int(5/2))
# # print('10') #일영 이라고 읽음
# # print(int('10')+2) #문자열 일영-->숫자 10으로 변환 ->더하기 2 =>12
# #
# # print(type(10))
# # print(type('123'))
#
# print(divmod(9, 4)) #9를 4로 나눈 몫과 나머지
# #        함수(인수1,인수2)
#
# res=divmod(9, 4) #res =(2,1)
# print("결과:",res)
# print("1번째 요소: ", res[0]) #res튜플에 저장된 1번째 요소값을 출력
# #튜플(리스트)에서 데이터의 위치는 0번부터 시작~
# print("2번째 요소 :", res[1])
#
# res1, res2=divmod(9, 4)
# print("1번째 요소:", res1)
# print("2번째 요소 :",res2)
#
# #0~9
# #0~1
# #0~7
# #0~9abcdef
#
# print(11) #10진수
# print(0b11) #앞에 ob를 붙이면 뒤 숫자가 2진수로 변환 -->3
# print(0o10) #0o->8진수
#
# print(5)
# print(float(5))
# print(float(1+2))
#
# print(int('2'))
# print(float('3.14'))
# print(float(3.14)*2)
# print(type(3.14))
# #print(int('2'))
#
# print("kim's computer")
#
# print('hello')
# print("kim's computer")
#
# print('he said. "how are you?"')
#
# #print("안녕 ! 반가워요 잘있어요")
#
# print("안녕!\n반가워요 잘있어요")
# print("안\t녕!\n반가워요\n\n잘있어요")
# #naver$daum$samsung
# print("naver","kakao", "samsung", sep="$")
# print("안녕",end=" ");print("하세")
#
# print(1+2*3) #만약 1+2를 먼저 연산하고 싶다면 소괄호
#
# a=1
# b=2
# c=3

# a,b,c,d= 1,2,3,4
# print(a,b,c,d)
#
# a=b=c=d=1
# print(a,b,c,d)
#
#
# x,y=1,2
# a=y
# y=x
# x=a
# print(x,y) #2,1라고 출력하고 싶으면

# x,y =1,2
# x,y=y,x
# print(x,y)

# a=1 #메모리에 a라는 공간을 만들고, 1을 저장해라
# print(a)
#
# #메모리에 있는 변수를 제거
# del a
# print(a)

#변수만 만들고 값을 저장하고 싶지 않은 경우

# b=None
# print(b)
#
#
# x=10
# x=x+10
# print(x)
#
# b=None #사과바구니 자체가 없음
# b='' #사과바구니에 사과가 1개도 없음
#
# x-=5 #x=x-5
# x*=5 #x=x*5

# x=input("출력하고 싶은 값을 입력하고 엔터치세?") #입려기을 받은 뒤 엔터 키를 누르면 다음 문장으로 이동
# print("당신이 입력한 값은 :", x)

# x=imput("
#input함수로 입력받은 모든 데이터는 '문자'로 간


# x=int(input("첫 번째 수 입력: "))
# y=int(input("두 번째 수 입력: "))
# print("덧셈 결과는 ", x+y)

# x=float(input("첫 번째 수 입력: "))
# y=float(input("두 번째 수 입력: "))
# print("덧셈 결과는 ", x+y)


# a,b,c =input("세 단어를 입력하세").split()
# #3 2
# print(a)
# print(b)
# print(c)

# print("안 녕 하세 요.".split())
#
# 숫자 두 개 입력 : 1 2 (엔터)
# 3

# x,y=input("숫자 두 개 입력 : ").split()
# print(int(x)+int(y))


# input("숫자 두 개 입력 : ").split()

#mapping:사상, x->f->y

# 함수출력=map(함수, 함수입력 )
# x1,x2=map(int,['3','4'])
# print(x1+x2)

# print(map(int,input("숫자 두 개 입력 : ").split()))

# x1, x2 = map(int, input("숫자 두 개 입력 :").split(","))
# print(x1+x2)

# x='hello'

# x="""인생은 짧다, 그래서 파이썬이 필요하다."""
# print(x)


# x="""인생은
# 짧다
# 그래서 파이썬이
# 필요하다.
# """
# print(x)

# a="python"
# print(a*3) #a변수에 저장된 값을 3번 반복

# print("="*50)
# print("일기장")
# print("="*50)


# x="life is too short"
# print(x[8:-3])
# print(x[5]+x[6])
# print(x[ :4]) #범위를 지정하여 슬라이싱 [시작위치: 끝위치+1]
# print(len(x))
# print(x[0]) #위치(인덱스)는 0부터 시작
#
# #인덱싱: 변수에 저장된 문자열에 대해 위치를 지정하여 참조하는 행위
# print(x[-3])

#"20201229" =>년/월/일

# x ="pithon"
# # print(x)
# #에러 : 문자열의 요소값은 변경이 안됨
#
# print(x[0:1]+"y"+x[2:])

# x=2
# print("I eat %d eggs" % x)
#
# x="two"
# print("I eat %d eggd" % x)


# x="ten"
# d =2
# per=30
# print("I eat %s eggs. so i was sick for %d days. %d%%" % (x,d, per))print

# 1
# letters = 'python'
# print(letters[0],letters[2])
#
# 2
# cn ="24가 2210"
# print(cn[4:])
# 3
# s="파이썬파이썬파이썬"
# print(s[0], s[3], s[-3])
# 4
# num_str = "720"
# print(int(num_str))
# 5
# data = "15.79"
# print(float(data))

# 6
# price=48584
# month=36
# total=price*month
# print("에어컨이 월 %d원에 무이자 %d개월의 조건으로 홈쇼핑에서 판매되고 있습니.총 금액은 %d원 입니다." %(price,month,total))


