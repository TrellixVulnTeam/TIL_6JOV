# # 16. 게임 기업 입사문제
# # 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# # 예를 들어
# # d(91) = 9 + 1 + 91 = 101
# # 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# # 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# # 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# # 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# # 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
# # not_self_num=set()
# # for i in range(1,5000):
# #    num=i+sum(map(int,str(i)))   # 자기자신 + 각 자리 숫자
# #    not_self_num.add(num)
# # self_num=set(range(1,5000))-not_self_num
# # print(self_num)
# # print(sum(self_num))
# #
#
#
#
#
#
# # 17. 최대낙차
# # 최대 낙차 : 7
# # box=[7,4,2,0,0,6,0,7,0]
# # drop2=[]
# # for i in range(len(box)):
# #     drop1=[]
# #     for j in box[i+1:]:
# #         if box[i]>j:
# #             drop1.append(j)
# #     drop2.append(len(drop1))
# # print("최대 낙차 :",max(drop2))
# #
# #
# #
# # box=[7,4,2,0,0,6,0,7,0]
# # num=0
# # lres=[]
# # for j in range(len(box)):
# # for i in box:
# # if box[j] <= i:
# # num+=1
# #
# # res = len(box)-j-num
# #
# # lres.append(res)
# #
# # print(max(lres))
#
# #파이썬 라이브러리:수 많은 파이썬 함수
#
# # #abs함수
# # print(abs(-1.2))
# #
# # #all함수:모두 참 -> True
# # print(all([1,2,3])) #1,2,3 모두 다 참
# # print(all([1,2,3,0])) #1,2,3,0 거짓이 있으므로 전체가 거짓이 됨
# #
# # #any함수 :어느 하나라도 참 => 참, 모두 거짓 => 거짓
# # print(any([1,2,3,0])) #1,2,3,0 참이 있으므로 전체가 참이 됨
# # print(any([0, ""])) #모두 거짓
# # print(any([])) #비어있는 리스트는 거짓 => 거짓
# #
# # #chr함수 : 아스키 코드 -> 문자를 출력 함수
# # print(chr(65)) #A
# #
# # #ord함수 : 문자 => 아스키 코드 출려 함수
# print(ord('A'))
# #
# # #enumerate : 열거형 데이터를 표현하는 함수, for 문과 함께 사용,
# # #리스트, 튜플, 문자열(시퀀스) 데이터 -> 입력 -> 인덱스를 포함하는 enumerate 객체 생성
# #
# for i in ['aaa','bbb','ccc']:
#     print(i)
# #
# for idx, i in enumerate(['aaa','bbb','ccc']):
#     print(idx, i)
# #
# # #인덱스 : 자료의 위치(순서)번호, 0번 부터 사용
# # #a=[10,20,30]
# #
# # #eval():문자열로 구성된 수식 -> 입력 -> 문자열을 실행한 결과를 출력
# print("10+20")
# print(type("10+20"))
# print(eval("10+20"))
# print(eval("10+20*(3+10)")) #stack사용
# print(type(eval("10+20")))
# #x="10+20" => 30
# #
#print(eval())
# print(eval("divmod(5,3)"))
# #
# #
# # #filter():원하는 데이터를 걸러내는 함수
# # #filter(함수이름, 1번째 인수에 있는 함수에 입력될 반복 가능한 자료형)
# # #filter함수의 리턴값이 True(참)인 값들만 묶어서 돌려준다
# #
# # #1.
# # def pos(a):
# #     # 구현
# #     res=[]
# #     for i in a:
# #         if i>0:
# #             res.append(i)
# #     return res
# #
# # print(pos([1,3,-5,-7,9])) #[1,3,9]
# #
# # #2. filter함수
# # #filter(함수이름, 1번째 인수에 있는 함수에 입력될 반복 가능한 자료형)
# # #filter함수의 리턴값이 True(참)인 값들만 묶어서 돌려준다
# # def pos2(a):
# #     return a>0
# # print(list(filter(pos2,[1,3,-5,-7,9])))
# #
# # #3. filter + 람다 함수
# # print(list(filter(lambda a:a>0,[1,3,-5,-7,9])))
# #
# # #hex함수:16진수로 변환
# # print(hex(234))
# # #16진수 ea = e*16+a*1=14*16+10*1=234
# #
# # #int함수 : '3' -> 3
# print(int('3'))
# print(float('3.4'))
# print(int('ea',16))

# #
# #
# #
# #
# #
# # #일반적인 리스트 저장 표현
# # num=[]
# # for n in range(11):
# #     num.append(n)
# # print(num)
# #
# # #리스트 내포(컴프리헨션)
# # print([n for n in range(11)])
# # #
# print([n*2 for n in range(11)])
# #
# # #1~10까지 짝수만 저장
# # evenNum=[]
# # for i in range(1,11):
# #     if i % 2 == 0:
# #         evenNum.append(i)
# #
# # #1~10까지 짝수만 저장(리스트 컴프리헨션)
# print([i for i in range(1,11) if i % 2 == 0])
# #
# # #리스트
# # #[(메뉴,후식),...]
# # # [('쌈밥', '사과'),
# # #  ('쌈밥', '아이스크림'),
# # #  ('쌈밥', '커피'),
# # #  ('치킨', '사과'),
# # #  ('치킨', '아이스크림'),
# # #  ('치킨', '커피'),
# # #  ('피자', '사과'),
# # #  ('피자', '아이스크림'),
# # #  ('피자', '커피')]
# # #
# # # ['쌈밥', '치킨', '피자']
# # # ['사과', '아이스크림', '커피']
# #

# print([(x,y,z) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['사', '아', '커']])
# #
# # # li=[]
# # # for x in ['쌈밥', '치킨', '피자']:
# # #     for y in ['사과', '아이스크림', '커피']:
# # #       for z in ['사','아','커']:
# # #         li.append((x,y,z))
# # # print(li)
# #
# # #0~9까지 수 중에서 5보다 작으면서 2로 나누어 떨어지는 수를 리스트에 저장하시오.[0, 2, 4]
# # print([x for x in range(10) if x < 5 or x % 2 ==0])
# # print(type([x+y for x in range(10) for y in range(10)]))
# # # 셋{} 컴프리헨션
# print(type({x+y for x in range(10) for y in range(10)}))
# # # 딕셔너리{} 컴프리헨션    {키:값, 키:값,...}
# print({x+y:"값" for x in range(10) for y in range(10)})
# # print(type({x+y:"값" for x in range(10) for y in range(10)}))
# #

# scores={'철수':50, '영희':70, '순신':100}
# print({name:score for name, score in scores.items() if name != '순신' })
# #
# scores={'철수':50, '영희':70, '순신':100}
# # #점수가 60점 이상이면 pass, 미만이면  fail
# # #출력={'철수':fail, '영희':pass, '순신':pass}
# # #출력 성공한 교육생은 코드를 카페에 업로드 해주세요
# print({name:"pass" if score>=60 else "fail"  for name, score in scores.items() })
# #
# # # for name, score in scores.items():
# # #     if score >= 60:
# # #     else:
# #
# # #일반적인 구문 :   [표현식 for 변수명 in 시퀀스 ]
# #
# # words=['Computer', 'Coke', 'Bread']
# # #리스트 컴프리헨션으로 표현
# # #['computer', 'coke', 'bread']
# # #print("Computer".lower())
# # print([w.lower() for w in words])


a= [1, -5, 4, 2, -2, 10]
# # #a에 저장된 값이 0보다 크면 a값을, 작으면 0을 출력
# # #[1,0,4,2,0,10]

# print([i if i>0 else 0 for i in a])



# # a=[1,2,3,4,5]
# # #a값이 1이면 "pass", 2이면 "fail", 나머지는 "no"
# # #[pass,fail,no,no,no]
# # for i in a:
# #     if i==1:
# #         print("pass")
# #     elif i==2:
# #         print("fail")
# #     else:
# #         print("no")

# # print(["pass" if i==1 else "fail" if i==2 else "no"  for i in a])
# # #if i==1 이면 "pass", else if i==2 이면 "fail" else 이면 "no"
# #
# #
#딕셔너리 응용
# x={'a':10,'b':20,'c':30}
# print(x)
# x['aa']=40
# print(x)
# x.setdefault('d') #키 d가 추가, 값이 None저장
# print(x)
#
# x['a']=100
# print(x)
# x.update(b=200)
# print(x)
# # #
# x['z']=99
# print(x)
# # #
# x.update(c=300, s=50, k=80)
# print(x)
#
# x.update({'a':10, 'd':30})
# print(x)
# #
# print(list(zip([1,2],['one','two'])))
# x.update(zip(['aa','c'],[999,777]) )
# print(x)

# x={'a':10, 'b':20, 'c':30, 'd':40}
# x.pop('a')
# print(x)
#
# x={'a':10, 'b':20, 'c':30, 'd':40}
# v=x.pop('b')
# print(v)
# # #
# x={'a':10, 'b':20, 'c':30, 'd':40}
# print(x.pop('z',0))#키가 없을때는 0을 리턴
# if x.pop('z',0)==0:
#
# else:


# x={'a':10, 'b':20, 'c':30, 'd':40}
# del x['b']
# print(x)
# #
# x.clear()
# print(x)
# #
# # #리스트(튜플) -> 딕셔너리 생성
# li=['a','b','c'] #키리스트
# # d=dict.fromkeys(li)
# # print(d)
#
# d2=dict.fromkeys(li, 10)
# print(d2)
# #

# from collections import defaultdict #collections 모듈에서 defaultdict함수를 가져옴
# #print(d2['z']) 키가 없으므로 에러
# d2=defaultdict(int)
# print(d2['z'])


# d3={'a':10, 'b':20}
# #키만 출력
# #값만 출력
# #키,값 쌍을 출력
# # for k in d3:
# #     print(k)
# # for k in d3.keys():
# #     print(k)
#
# # for v in d3.values():
# #     print(v)
#
# # for k,v in d3.items():
# #     print(k,v)
#
keys=['a','b','c','d']
print(dict.fromkeys(keys))
#
# for key, value in dict.fromkeys(keys).items(): #dict.fromkeys(keys)는 딕셔너리
#     print(key, value)

# d4={key:value for key, value in dict.fromkeys(keys).items()}
# print(d4)
#
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e':20}
#
# #newx는 x에 저장된 데이터에서 'b'를 뺀 나머지를 저장
# newx={k:v for k, v in x.items() if k!='b'}
# print(newx)
#
# #newx는 x에 저장된 데이터에서 값이 '20'인 자료를 뺀 나머지를 저장
# newx={k:v for k, v in x.items() if v!=20}
# print(newx)
#
#
# #딕셔너리={키1: {키a:값a,키b:값b}, 키2:{키c:값c,키d:값d}}
#
영화평점={'BTS':{'머큐리':4.5,'매트릭스':4.0},'소녀시대':{'머큐리':3.5,'매트릭스':3.0}}
# print(영화평점['BTS']['매트릭스'])
#
# 영화평점['BTS']['매트릭스']=5
# print(영화평점['BTS']['매트릭스'])
#
x={'a':0,'b':1}
y=x #실제로는 딕셔너리가 1개 만들어짐
print(x is y) #변수 이름만 다를 뿐 x, y는 같은 객체

# x['a']=100
# print(y)
#
# y=x.copy() #완전히 다른 2개의 딕셔너리가 만들어짐
# print(x is y)
# print(x==y)
# x['a']=111
# print(x)
# print(y)
#
# x={'a':{'python':'3.8'}, 'b':{'python':'2.7'}}
# y=x.copy()
# #
# y['a']['python']="2.77777"
# print(y)
# #
# print(x)

# #중첩 딕셔너리에서는 copy메서드 대신 copy모듈의 deepcopy함수를 사용
# x={'a':{'python':'3.8'}, 'b':{'python':'2.7'}}ㄴ
# import copy
# y=copy.deepcopy(x) #깊은 복사
# y['a']['python']="2.77777"
# print(y)
# print("="*50)
# print(x)
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
