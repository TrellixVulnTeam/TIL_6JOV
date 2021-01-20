# # # tel="010-1234-5678"
# # # print(tel.replace("-",""))
# # #데이터수집 -> 전처리 -> 분석->...
# # #replace힘수 : 문자(열)치환
# #
# # # -->대한민국, 한국, 코리아, korea,KOREA, southKorea,RebofKorea-->등을 모두
# # # korea로 바꾸고 싶을 때 유용
# # #
# # # 먹다(음식, 뇌물, 쥐어패다)
# # # eat
# #
# # # 자연어 처리할 때
# # # -->고객:xxxx 상담원: 모름
# # #
# # # print(1,2,3, sep="&")
# # #
# # # print(3>2)
# # # # -->비교연산자의 추론형태는 모두 true or false로 나옴
# # #
# # # print(2==2)
# # # print(3!=2)
# # #
# # # print('python'=='Python')
# # #
# # # print()
# # #
# # # print(1==1)
# # #
# # # a=1
# # # b=1
# # # print(a == b)
# # # print(a is b)
# #
# # #참고(몰라도 됨
# # # print(1==1.0) #정수와 실수라는 점에서 차이, 값은 같다. 따라서 ==로 비교하면 true가 나옴
# # # print(1 is 1.0) #is는 두 객체가 같은지 비교.1은 정수객체, 1.0은 실수객체
# #
# # # 논리 연산자 : and(모두 참 -> 참), or(하나 이상 참->참), not(참->거짓,거짓->
# #
# # # print(1==1 and 2!=1)
# # # print(3>1 or 1<2)
# # # print(not 1>2)
# # #
# # # # 0 : false, 1: true
# # #
# # # print(bool(1))
# # #
# # # print("="*50)
# # #
# # # print(bool('test'))
# # #
# # # print(bool(0 or 'test'))
# # # print(bool(0 and 'test'))
# #
# # # print("hi")
# # # print("    hi")
# # # print("hi     ")
# #
# # #
# # # print("%10s" %"hi")
# # # print("%-10shello" %"hi")
# # #
# # # print("%.4f")
# #
# # # num=3
# # # s="two"
# # # day="three"
# # # print("i eat %d apples"%num)
# # # print("i eat %s apples"%s)
# # # print("i eat {0} apples".format(num))
# # # print("i eat {0} apples".format(s))
# # #
# # # print("i ate {0} eggs. so i was sick for {1} days".format(num,day))
# # #
# # #
# # # print("{0}".format("hi"))
# # # print("{0:-<10}".format("hi")) #10자리 확보 후 왼쪽 정렬
# # # print("{0:->10}".format("hi")) #10자리 확보 후 오른쪽 정렬
# # # print("{0:-^10}".format("hi")) #10자리 확보 후 가운데 정렬
# # # print("{0:-^10}".format("hi")) #10자리 확보 후 가운데 정렬
# # #
# # # print("{0:.4f}".format(3.141592))
# # # print("{0:10.4f}".format(3.141592))
# # #
# # # a="hello"
# # # print(a.count('l'))
# # #
# # # print(a.find('l'))
# # # print(a.fint('x'))
# # #
# # # print(a.index('l'))
# # # print(a.index('x'))
# #
# #
# #
# # print(",".join("abcd"))
# #
# #
# #
# # a="hi"
# # print(a.upper())
# # a=a.upper()
# # print(a)
# #
# # print(a.lower())
# #
# # # "   대한민국" "대한민국   " "대한민국"....
# #
# #
# # # n1="   대한민국"
# # # n2="대한민국   "
# # # n3="   대한민국   "
# # # print(n1.lstrip())
# # # print(n2.rstrip())
# # # print(n3.strip())
# #
# #
# #
# # #replace:문자(열)을 치환
# # # s="life is too short"
# # # print(s.replace("life","your leg"))
# # # print(s.split()) #공백문자로 분
# # #
# # # s="life$is$too$short"
# # # print(s.split("s"))
# # #
# # # print(s.split('s')) #method(=funtion)
# #
# # # t=str.maketrans('aeiou','12345')
# # # print('apple'.translate(t)) #apple 문자열을 t변환 테이블을 참조하 변환하세
# # # # 문자바꾸기
# # # # str.maketrans('바꿀문자','새문자') 작성하여 변환테이블(t) 생성
# # #
# # # # 정규표현식 : 문자열 전처리
# # # str=", python,."
# # # print(str.lstrip())
# # # print(str.lstrip(","))
# # # print(str.lstrip(" "))
# # # # print(str.lstrip(", ")) 열큰따옴표 안에 제거대상 문자를 나
# # # print(str.lstrip(" ,"))
# # # print(str.rstrip(" ,."))
# # #
# # #
# # #
# # # import string
# # # print(string.punctuation)
# # # # # punctuation(구두점) : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# # #
# # #
# # # # print(str.strip(string.punctuation))
# # # # print(str.strip(string.punctuation+" ")
# # #
# # #
# # # print(str.strip(string.punctuation))
# # #
# # # # print('python'.ljust(10)) -->10자리 확보 후 좌측 정렬
# # # # print('python'.rjust(10)) --->10자리 확보 후 우측 정렬
# # # # print('python'.center(10))-->10자리 확보 후 가운데 정
# # #
# # # import random
# # # print("hi")
# # # print(random.random())
# # #
# # # print("="*50)
# # # # 함수중에는 import를 해야하는 게 있고 그러지 않아도 되는 것이 있다.
# # #
# # # print('pythin'.rjust(10))
# # # s='python'.rjust(10)
# # # print(s.upper())
# # #
# # # print('python'.rjust(10).upper())
# # #
# # # # 패딩(padding: 특정 값으로 빈자리를 채우는 것)
# # #
# # # print("hello".zfill(10))
# # # print("345".zfill(10))
# # #
# # # print("apple pineapple".find('p'))
# # # print("apple pineapple".find('pp'))
# # #
# # # print("apple pineapple".rfind('p'))
# # # print("apple pineapple".rfind('pp'))
# #
# #
# #
# # x=[10,20,30]
# # print(x)
# # print(x[1])
# #
# # y=['Life','is','too','shot']
# # print(y[0])
# #
# #
# # a=[1,2,['Life','is',['too','short']]]
# #
# # print(a[2][2][0])
# #
# #
# # b=[] #빈 리스트 생성
# # b=list()
# #
# # b=[1,2,3]
# #
# # print(b[0]+b[2])
# #
# #
# # 홍길동=[30, 1, ['코딩','산책','영화']]
# #
# #
# #
# # a=[1,2,['Life','is',['too','short']]]
# # print(a[2])
# # print(a[-1])
# print(a[-1][-1][-2])
# #
# #
# # # 리스트 slicing
# #
# # x=[1,2,3,4,5]
# # print(x[1:4])
# #
# # s='abcdefg'
# # print(s[2:5])
# #
# # a=[1,2,3,['x','y','z'],4,5]
# #
# # print(a[3][0:2])
# # print(a[3][:2])
# #
# #
# # range(5)
# # # 0~5-1까지 숫자를 생성
# #
# # print(list(range(5)))
# # print(list(range(3,10)))
# # print(list(range(3,10,2)))
# # print(list(range(10,0,-2)))
# #
# # # 리스트 연산
# # a=[1,2]
# # b=[3,4]
# # print(a+b)
# #
# #
# #
# # print("ab"+'cd')
# #
# # print(a*3)
# # print(len(a))
# #
# # print(str(a[0])+'hi')
# #
# #
# # a=[1,2,3]
# # a[2]=4
# # print(a)
# #
# # del a[2]
# # print(a)
# #
# #
# #
# # a=list(range(1,10))
# # print(a)
# # del a[:5]
# # print(a)
# #
# # a=[1,2,3]
# # print(a)
# # print(a+[4])
# # a.append([5,6,7])
# #
# # print(a)
# # a.extend([5,6,7])
# #
# # print(a)
# #
# # #정해진 순서로 데이터 나열(내림/오름, 0->9,ㄱ->ㅎ,a->z)
# #
# # a=[3,7,5,1]
# # a.sort()
# # print(a)
# #
# # a=[3,7,5,1]
# # print(a.sort())
# #
# # a=['b','k','d']
# # a.sort()
# # print(a)
# #
# #
# # a=[3,7,5,1]
# # a.sort()
# # a.reverse()
# # print(a)
# #
# #
# # a=[7,8,9]
# # a.insert(1,4)
# # print(a)
# #
# #
# # a=[10,20,30,10,20,30]
# # a.remove(30)
# # a.remove(30)
# # print(a)
# #
# #
# #
# # a=[10,20,30]
# # a.pop()
# # print(a)
# #
# #
# #
#
#
# # 1.다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"
# print(ticker.upper())
# #
#
# # 2.다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"
# print(ticker.lower())
# # 3.다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
# print(a.split(" "))
# # 4.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
# print(ticker.split("_"))
#
# # 5.다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-12-30"
# print(date.split("_"))

# # 6.문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "
# print(data.strip())
#
# # 7.
# # 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# # 이름: 김민수 나이: 10
# # 이름: 이철희 나이: 13
# print("이름: %s 나이: %d" %(name1,age1))
# print("이름: %s 나이: %d" %(name2,age2))
# print("이름: {0} 나이: {1}".format(name2,age2))
# # 8. 문자열의 format( ) 메서드를 사용해서 7번 문제를 다시 풀어보세요.
# print("이름: {0} 나이: {1}".format(name1,age1))
# print("이름: {0} 나이: {1}".format(name2,age2))
#
# # 9. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# price = "5,969,782,550"
# print(int(price.replace(",","")))

#
#
# # 10. 다음과 같은 문자열에서 '2020/12'만 출력하세요.
# 분기 = "2020/12(E) (IFRS연결)"
# print(분기[0:7])
# #
# # 11. 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# string = 'abcdfe2a354a32a'
# print(string.replace('a','A'))
#
# # 12.
# # 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
# pin = "881120-1068234"
# print(pin[-7])
# # 13.다음과 같은 문자열 a:b:c:d가 있다. a#b#c#d로 바꿔서 출력해 보자.
# a = "a:b:c:d"
# print(a.replace(':','#'))
#
# # 14. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# # (join 활용)
# print(" ".join(["life",'is','too','short']))
#

# # # 10. 다음과 같은 문자열에서 '2020/12'만 출력하세요.
# 분기 = "2020/12(E) (IFRS연결)"
# print(분기[0:7])

# str=", python,."
# import string
# print(string.punctuation)
#
# print(str.strip(string.punctuation + " "))

