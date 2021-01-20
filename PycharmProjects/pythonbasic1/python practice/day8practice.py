# # # 1. 문자열 바꾸기
# # # 다음과 같은 문자열이 있다.
# # # a:b:c:d
# # # 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
# # # a#b#c#d
# #
# # string="a:b:c:d"
# # b=string.split(":")
# # print("#".join(b))
# #
# #
# # # 2. 리스트 총합 구하기
# # # 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 60점 이상 점수의 평균을 구하시오.
# # #
# # A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# #
# # li=[]
# # for i in A:
# #     if i>=60:
# #         li.append(i)
# #     b=sum(li)
# # print(b/len(li))
# #
# #
# # 3. 평균값 구하기
# # 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# # #
# # 70
# # 60
# # 55
# # 75
# # 95
# # 90
# # 80
# # 80
# # 85
# # 100
#
# # li=[70,60,55,75,95,90,80,80,85,100]
# # with open("sample.txt","w") as f:
# #     for i in li:
# #         f.write(str(i)+"\n")
# # with open("sample.txt","r") as j:
# #     score_sum=0
# #     for i in j:
# #         score_sum+=int(i)
# #     avg=score_sum/len(li)
# # with open("result.txt","w") as result:
# #     result.write(str(avg))
# #
# #
# # #
# # #
# # 4. 모스 부호 해독
# # 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
# #
# # 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# # 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# # …. .  … .-.. . . .—. …  . .- .-. .-.. -.—
# # 모스부호 규칙 표
# # .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
#
# #
# # mos = input()
# # dic = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
# #     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
# #     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
# #     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
# #     '-.--':'Y','--..':'Z'
# # }
# # # 내가 풀다 만거...
# #
# # mos1=mos.split(' ')
# # print(mos1)
# #
# # for i in mos1:
# #     for k in dic:
# #         if i==k:
# #             print(dic.get(i),end="")
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
# # mos1 = mos.split(" ")
# # print(mos1)
# #
# #
# # for i in mos1:
# #     if i == '':
# #         print(" ", end="")
# #     elif i in dic:
# #         char = dic.get(i)
# #         print(char, end="")
# # #
#
# #
# #
# #
# #
# #
# #
#
# # # 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
# # #
# # # 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# # # 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.\
# # # .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
# #
# # # mos=input("모스부호를 입력하세요:")
# # # 다르 풀
# # # word=mos.split("  ")
# # #
# # # for i in word:
# # #     letter=i.split(' ')
# # #     for j in letter:
# # #         print(dic[j],end='')
# # #     print('',end=' ')
# #
# #
# # # st=""
# # # for i in mos.split("  "):
# # #     for w in i.split(" "):
# # #         st+=dic[w]
# # #     st+=" "
# # # print(st)
# # #
# #
# #
# #
# # # # 5. ngram 기반 두 문장 유사도 구하기(n=2, 3)
# # # # "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# # # # "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# # #
#강사님 풀이

a = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
b = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"

def ngram(s,num):
    res=[]
    slen=len(s)-num+1
    for i in range(slen):
        ss= s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa,sb,num):
    a=ngram(sa,num)
    b=ngram(sb,num)
    # print(a)
    # print(b)
    cnt=0
    r=[]
    for i in a:
        for j in b:
            if i==j:
                cnt+=1
                r.append(i)
    print(cnt/len(a),r)

# 수정사항
# 1)중복 허용 안되도록...
# 2)두 문장에서 길이가 긴 문장의 단어 개수를 분모





r2, word2=diff_ngram(a,b,2)
print("2-gram",r2,word2)

# # #
# # # #오늘,늘멀,멀티,티캠---
# # #
# # # #멀티,티캠,캠퍼....
# #
# def seperate(a, b, n):
# 	a1 = a.replace(" ", "")
# 	b1 = b.replace(" ", "")
#
# 	li1 = list(a1[i:i + n] for i in range(len(a1) - 1))
#
# 	li2 = list(b1[i:i + n] for i in range(len(b1) - 1))
# 	li3 = li1 + li2
# 	cnt = (len(li3) - len(set(li3)))
#
# 	if len(a) > len(b):
# 		longcnt = len(list(a1[i:i + n] for i in range(len(a1) - 1)))
# 	else:
# 		longcnt = len(list(b1[i:i + n] for i in range(len(b1) - 1)))
#
# 	return cnt / longcnt
#
# #
# str1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# str2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
#
# print(f"두 문장의 유사도 : {seperate(str1, str2, 2) * 100} % 입니다.")
# print(f"두 문장의 유사도 : {seperate(str1, str2, 3) * 100} % 입니다.")
# # # str1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# # # str2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# # #
# #
# #
# # #
# # #
# # # a = seperate(str1, str2, 2)
# # # num = (len(a) - len(set(a)))
# # #
# # # print(num)
# #
# #
# # #
# # # #
# # # #
# # # a="오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# # # b="멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# # # #
# # #
# # # def ngram(a,b,n):
# # # 	a1=a.replace(" ","")
# # # 	b1=b.replace(" ","")
# # #
# # # 	li1=[]
# # # 	for i in a1:
# # # 		c=a1[i:i+n]
# # # 		li1.append(c)
# # # 	li2=[]
# # # 	for j in b1:
# # # 		d=b1[j:j+n]
# # # 		li2.append(d)
# # # 	lf=set(li1)-set(li2)
# # # 	if len(li1)>=len(li2):
# # # 		print((len(li1)/len(lf))*100,"의 유사도")
# # # 	else:
# # # 		print((len(li2)/len(lf))*100,"의 유사도")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #다른 분 풀
# # # # class 굳이 필요 없음...
# # # class Ngram:
# # #     def __init__(self, s1, s2):
# # #         self.n = 0
# # #         self.s1 = s1
# # #         self.s2 = s2
# # #
# # #     def similarity(self, n):
# # #         self.n += n
# # #
# # #         s1_n=set(self.s1[i:i+self.n] for i in range(len(self.s1)-(self.n-1)))
# # #         s2_n=set(self.s2[i:i+self.n] for i in range(len(self.s2)-(self.n-1)))
# # #         if len(s1_n) > len(s2_n):
# # #             length = len(s1_n)
# # #         else:
# # #             length = len(s2_n)
# # #
# # #         similarity = int((len(s1_n & s2_n) / length)*100)
# # #         print("두 문장의 유사도는 {}%입니다.".format(similarity))
# # #
# # # sen1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# # # sen2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
# # #
# # # sentences = Ngram(sen1, sen2)
# # # sentences.similarity(2)         #68%
# # # sentences.similarity(3)         #53%
# #
# #

# #추가 풀이
#
# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }
# def morse(src):
#     res=[]
#     for word in src.split("  "): #입력된 문장에 저장된 단어 3개
#         for c in word.split(" "): #c에는 문자가 저
#             print(c)
#             res.append(dic[c])
#
#         res.append(" ") #단어와 단어가 공백문자로 구분
#
#     return"".join(res)
#
#
#
# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


