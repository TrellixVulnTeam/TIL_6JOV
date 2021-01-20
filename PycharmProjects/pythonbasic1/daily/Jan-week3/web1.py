# #정규표현식 :복잡한 문자열 처리(퇴근시간을 대폭 단축)
#
# jumin="""
# park 850b01-12a4567
# kim 950202-2345678
# """
# #print(jumin)
#
# # jumin 데이터의 뒷 부분을 모두 *로 변환하여 출력
# # park 850101-*******
# # kim 950202-*******
# for line in jumin.split("\n"):
#     for word in line.split(" "):
#         if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
#             word=word[:6]+"-"+"*******"
#             print(word)
#
# #print(jumin.split("\n")) # \n : 엔터 문자(줄바꿈 문자)
#
#
#
# # s="pithon"
# # #s[1]="y"
# # #print(s)
# # print(s[0]+"y"+s[2:])
# #print(s)
#
# # d="12s34"
# # print(d.isdigit())
#
#
#
# # jumin="""
# # park 850101-1234567
# # kim 950202-2345678
# # """
# # import re #regular expression( 정규 표현식 모듈)
# # p=re.compile("(\d{6})[-]\d{7}") #정규식 작성
# # print(p.sub("\g<1>-*******",jumin))
# #
# # #정상적인 주민번호에 대한 일반적인 규칙을 정의(숫자6자리-숫자7)
# #
# # #re.match("패턴", "문자열")#문자열이 패턴에 부합되나요?
# #
# # print(re.match("hello", "hello, world"))
# # #"hello, world" 문자열에 hello 문자열이 있는지 판단
# # #출력(매치됨) : <re.Match object; span=(0, 5), match='hello'>
# #
# # print(re.match("hi", "hello, world"))
# # #출력(매치안됨) : None
# #
# # if re.match("hello", "hello, world"): #None은 거짓
# #     print("주어진 hello, world 문자열은 hello(문자열)패턴에 매치가 됐습니다")
# # else:
# #     print("매치되지 않았습니다.")
# #
# # print("hello, world".find("hello"))
# #
# # #특정 문자열이 맨앞/뒤 오는지 판단?
# # #문자열 맨 앞에 ^를 붙이면 맨 앞에 오는지 판단
# # #   "     끝에 $를     "   끝     "
# #
# # print(re.search("^hello", "hello, world")) #hello로 시작하는지 확인
# # print(re.search("world$", "hello, world")) #world로  끝나는지 확인
# #
# # #hello 또는 world 문자열이 포함되어 있는지 확인
# # print(re.match("hello|world", "hello"))
# # print(re.match("hi|world", "hello"))
#
# # 정규표현식 메타문자(메타:정보의 정보, 데이터(전화번호부)의 데이터(색인),...)
# #메타문자 종류 : ( ) { } [ ] \ | ? + * $ ^...
# """
# [] 메타문자:
# 대괄호 안에는 어떤 문자도 올 수 있음
# ex) [abcdef] 의미? a,b,...,f 중에서 어떤 한 개의 문자와 매치
# 'a' 문자는 정규표현식에 매치됨
# """
import re
# print(re.match("[abcdef]","a")) #매치됨
# print(re.match("[abcdef]","g")) #매치 안됨
# print(re.match("[abcdef]","abc")) #매치됨
# print(re.match("[abcdef]","c")) #매치됨
#
# print(re.match("my","hello, my world"))
# print(re.search("my","hello, my world"))
#
# #[from-to]
# #[a-d] 정규식 의미 : [abcd], [a-f]==[abcdef]
# #[0-5] == [012345]
#
# print(re.match("[0-9]","1234")) #1234는 0~9까지 숫자에 해당
# print(re.match("[0-9]*","1234")) #1234는 0~9까지 숫자에 해당, *은 문자(숫자)가 0개 이상 있는지 확인
# print(re.match("[0-9]","a1234")) #a1234에서 a는 [0-9] 범위가 아님.
# # 원래는 None이 나와야 함. 그러나, *이 있으므로 0개도 매칭이 된 것으로 출력
#
# print(re.match("[0-9]+","1234")) #1개 이상 있는지 확인
# print(re.match("[0-9]+","12a34"))
# print("="*50)
# print(re.match("[0-9]+","a12a34"))
# print(re.match("[0-9]*","a12a34"))
# #[a-z], [A-Z], [a-zA-Z], [^0-9]:0-9(숫자)를 제외한 문자
# #^hello, hello$
#
# print(re.search("^hi", "hello, hi")) #문자열이 hi로 시작해야 함(시작하지 않으므로 None)
# print(re.search("hi", "hello, hi")) #span=(7, 9), match='hi'
# print(re.match("hi", "hello, hi")) #None
#
# print(re.match("hello|hi|good", "good"))
# print(re.match("[0-9]", "12a3bcd"))
# print(re.match("[0-9]*", "12a3bcd")) #숫자가 0개 이상 있는지 판단
# print(re.match("[0-9]+", "12a3bcd")) #숫자가 1개 이상 있는지 판단
#
# print(re.match("[0-9]*", "a12a3bcd")) #숫자가 0개 이상 있는지 판단
# print(re.match("[0-9]+", "a12a3bcd")) #숫자가 1개 이상 있는지 판단
#
# print(re.match("[0-9]*", "123")) #숫자가 0개 이상 있는지 판단
# print(re.match("[0-9]+", "123")) #숫자가 1개 이상 있는지 판단
#
# print(re.match("[a-z]*", "12a3")) #알파벳 문자가 0개 이상 있는지 판단
# print(re.match("[a-z]+", "12a3")) #알파벳 문자가 0개 이상 있는지 판단
#
# print(re.match("[a-z]*", "aabb12a3")) #알파벳 문자가 0개 이상 있는지 판단
# print(re.match("[a-z]+", "aabb12a3")) #알파벳 문자가 1개 이상 있는지 판단
#
# print(re.match("ab","abcba"))
# print(re.match("ba","abcba"))
# print(re.search("ab","abcba"))
# print(re.search("ba","abcba"))
#
# print(re.match("a*", "b")) #*은 *앞에 있는 문자가 0개 이상 나왔을때 매치
# #a문자가 0개 이상 있으면 매치
# print(re.match("b*", "b"))
# #b문자가 0개 이상 있으면 매치
# print(re.match("a*b", "b")) #a문자가 0개 이상 있고 b가 나오면 매치
# print(re.match("a*b", "bb")) #a문자가 0개 이상 있고 b가 나오면 매치
#
# print(re.match("a+b", "b")) #a문자가 1개 이상나와야하고 반드시 b가 그 뒤로 나와야 함
# print(re.match("a+b", "ab"))
# print(re.match("a+b", "aaaab"))
# print(re.match("a+b", "aaaabb")) #aaaab까지만 매치
# print(re.match("a+cb+", "aaaaaaaaaaaaaaaaacbbbbbbbbbbbbbbbbb")) #aaaab까지만 매치
# print(re.match("a+b*k","aaaaaaabbbbbcccc"))
# #패턴이 문자열에 있는지만 보면 됨(문자열이 패턴을 반드시 가지고 있어야 함)
#
#
# #대한한한한민국 = 대한민국
#
# #print(re.match("대한+민국","대한한한한한한한한한한한한한한민국"))
#
#
#
