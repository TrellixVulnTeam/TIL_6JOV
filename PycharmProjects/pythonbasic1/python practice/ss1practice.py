# # # 1.
# # #
# # # 리스트에 있는 숫자들의 최빈값을 구하는 프로그램을 만들어라.
# # #
# # # [12, 17, 19, 17, 23] = 17
# # # [26, 37, 26, 37, 91] = 26, 37
# # # [28, 30, 32, 34, 144] = 없다
# # #
# # # 최빈값 : 자료의 값 중에서 가장 많이 나타난 값
# # # ① 자료의 값이 모두 같거나 모두 다르면 최빈값은 없다.
# # # ② 자료의 값이 모두 다를 때, 도수가 가장 큰 값이 1개 이상 있으면 그 값은 모두 최빈값이다.
# #
# # def mode(nums):
# #     dic={}
# #     for i in nums:
# #         dic[i]=nums.count(i)
# #     res=[]
# #     for k,v in dic.items():
# #         if v==max(dic.values()) and 1<len(dic)<len(nums):
# #             res.append(k)
# #         elif len(dic)==1 or len(dic)==len(nums):
# #             res="없다"
# #     print(res)
# #
# # mode([12, 17, 19, 17, 23])
#
#
# #
# # def mostCommen(num_list):
# #     num_set = list(set(num_list))
# #     cnt = 0
# #     most_commen_num = []
# #     for i in num_set:
# #         if cnt <= num_list.count(i):
# #             l = len(most_commen_num)
# #             if cnt < num_list.count(i) and l > 0:
# #                 for j in range(l):
# #                     most_commen_num.pop()
# #             cnt = num_list.count(i)
# #             most_commen_num.append(i)
# #     if cnt == 1 or len(most_commen_num) == len(num_set):
# #         print("없다")
# #     else:
# #         print(most_commen_num)
#
#
#
# #
# from collections import Counter
# def mostCommen2(num_list):
#     cnt = Counter(num_list)
#     cnt_list = cnt.most_common()
#     max_num = cnt_list[0][1]
#     most_commen_num = []
#     for num in cnt_list:
#         if num[1] == max_num:
#             most_commen_num.append(num[0])
#     if len(cnt_list) == len(num_list):
#         print("없다")
#     else:
#         print(most_commen_num)
# mostCommen2([12, 17, 12, 19, 17, 19, 19, 23])
# #
# # # 2.
# # # 약수를 모두 찾는 수학 문제를 풀다가 지친 X는 컴퓨터의 도움을 받아 문제를 풀어 보기로 하였다. 하지만 계산기를 이용하자니 계산기로 하고 싶지만 찾기도 어려우며, 쉽게 찾아낼 수도 없었다.
# # #
# # # 풀이에 지친 그는 결국 약수들이 가지고 있는 특징을 찾아 결국 몇시간에 걸쳐 복잡한 수라도 약수를 찾아줄 수 있고 개수도 알려주는 프로그램을 짜게 된다.
# # #
# # # 다음은 약수를 얻기 위한 입력과 출력 예제들이다.
# # #
# # # 입력 1
# # #
# # # 24
# # # 출력 1
# # #
# # # { 1, 2, 3, 4, 6, 8, 12, 24}
# # # 약수의 개수는 8개 입니다.
# # # 입력 2
# # #
# # # 36
# # # 출력 2
# # #
# # # { 1, 2, 3, 4, 6, 9, 12, 18, 36 }
# # # 약수의 개수는 9개 입니다.
# # # 입력 3
# # #
# # # 2468013579
# # # 출력 3
# # #
# # # { 1, 3, 9, 61, 183, 549, 4495471, 13486413, 40459239, 274223731, 822671193, 2468013579 }
# # # 약수의 개수는 12개 입니다.
# # # 사용한 소스코드를 풀이에 넣어 입력과 출력이 나왔음을 보이고,
# # # 소스코드를 디버깅하여 123456789를 입력해 출력된 결과를 '{ a, b, ... } / 약수의 개수는 ~개 입니다' 형식으로 하시오.
# # #
# # #
# # # n=int(input("양의 정수를 입력하세요:"))
# # # li=[]
# # #
# # # for i in range(1,n+1):
# # #     if n%i==0:
# # #         li.append(i)
# # #
# # # print(li)
# # # print("약수의 개수는 {0}개 입니다.".format(len(li)))
# #
# #
# #
# # #
# # # 3. 당신은 A 인터넷 카페 운영자이다.
# # #
# # # 당신의 인터넷 카페에는 휴대폰 번호 게시가 금지되어 있다.
# # #
# # # 하지만 일부 회원들이 편법을 동원하여 휴대폰 번호를 게시 후 불법 거래를 시도한다.
# # #
# # # 이를 체크하여 자동 삭제를 할 수 있도록 휴대폰 번호 검사 알고리즘을 작성하시오.
# # #
# # # (011~019 는 10자리여도 휴대폰 번호이다. 010은 11자리여야만 한다.)
# # #
# # # Input
# # #
# # # 영일영-구구칠8-일구팔사
# # # 0일영.칠칠칠팔.이삼사
# # # 영 일 칠 삼 칠 오 팔 이 팔 이
# # # 영일일 34구구 4 오 9 이
# # # Output
# # #
# # # 01099781984 true
# # # 0107778234 false
# # # 0173758282 true
# # # 01134994592 true
# # #
# #
# #
# # # def check_pnum(li):
# # #     han=['영','일','이','삼','사','오','육','칠','팔','구']
# # #     num=[str(i) for i in range(10)]
# # #     li=li.replace('-','').replace('.','').replace(' ','')
# # #     for i in range(10):
# # #         li=li.replace(han[i],num[i])
# # #     if li[0:3]=='010' and len(li)!=11:
# # #         print(li,False)
# # #     else:
# # #         print(li,True)
# # #
# # # check_pnum("영일일 34구구 4 오 9 이")
# #
# #
# #
def num_change(num):
    import re
    ko_tel = re.sub("[-. ]+", "", num)
    t = str.maketrans("영일이삼사오육칠팔구", "0123456789")
    num_tel =ko_tel.translate(t)
    while re.match("^01[1-9][\d]{7,8}|^010[\d]{8}",num_tel):
        print(num_tel,"true")
        break
    else:
        print(num_tel,"false")
num_change("영일영-구구칠8-일구팔사")
#
# #
# # # 4. 카프리카 수
# # # 카프리카 수란 인도의 수학자 D.R.카프리카의 의해 정의한 수이다.
# # #
# # # 어떤 수의 제곱수를 두 부분으로 나누어 더하였을 때 다시 원래의 수가 되는 수들을 의미한다.
# # #
# # # 예를 들어 45는 카프리카 수인데, 45² = 2025이고, 20+25 = 45이기 때문이다.
# # #
# # # 1)어떤 수를 입력 받고 그 수가 카프리카 수인지 아닌지를 출력하는 함수를 만드시오.
# # # 2)어떤 수를 입력 받고 자릿수가 그 수인 모든 카프리카 수를 출력하시오.
# #
# # # 3)어떤 수를 입력 받고 어떤 수 이하의 모든 카프리카 수를 출력하시오.
# #
# #
# #
# # #1)어떤 수를 입력 받고 그 수가 카프리카 수인지 아닌지를 출력하는 함수를 만드시오.
# # # def checknum(n):
# # #     num=n**2
# # #     lennum=len(str(n))
# # #
# # #     if n==1:
# # #         return True
# # #
# # #     for i in range(1,lennum):
# # #         if int(str(num)[i:])>0:
# # #             if (int(str(num)[:i])+int(str(num)[i:])) == n:
# # #
# # #                 return True
# # #             else:
# # #                 return False
# #
# # #2)어떤 수를 입력 받고 자릿수가 그 수인 모든 카프리카 수를 출력하시오.45
# # # def checknum2(n):
# # #     lennum=len(str(n))
# # #     result=[]
# # #     for i in range(10**(lennum-1),10**lennum):
# # #         if checknum(i)=='True':
# # #             result.append(i)
# # #     return result
# #
# #
# #
# #
# #
# #
# #
# # # 이 셋중에서 원하는 유형 하나를 골라 푸시오.
# # #
# # # 입력 (유형 1)
# # #
# # # print(kaprekar_number(1))
# # # print(kaprekar_number(45))
# # # print(kaprekar_number(297))
# # # print(kaprekar_number(3213))
# # # 출력 (유형 1)
# # #
# # # True
# # # True
# # # True
# # # False
# # # 카프리카 상수
# # # 카프리카 상수도 마찬가지로 인도의 수학자 카프리카가 발견한 상수이다.
# # #
# # # 이 상수의 생성법은 다음과 같다.
# # #
# # # 숫자 하나로만 이루어지지 않은 4자리 수를 정한다. (예: 1000은 인정하되, 1111은 인정하지 않는다.)
# # # 첫 자리에 0이 와도 무방하다.
# # # 이 숫자를 크기 순으로 배열하여 두 수를 만든다. 하나는 큰 순, 하나는 작은 순으로 배열한다.
# # # 큰 쪽에서 작은 쪽을 빼 준다. 이때 나온 0은 유지한다.
# # # 이 과정을 반복하면 7번 이내로 6174가 나온다.
# # # 어떤 수를 입력 받고 몇번이내로 6174가 완성 되었는지 출력하는 함수를 입력하시오
# # #
# # # 단, 입력값은 정수여야 한다.
# # #
# # # 입력
# # #
# # # print(kaprekar_constant(4371))
# # # print(kaprekar_constant(21))
# # # print(kaprekar_constant(1))
# # # print(kaprekar_constant(1111))
# # # 출력
# # #
# # # 7
# # # 3
# # # 5
# # # False
# #
# # def kaprekar_constant(num):
# #     str_num=str(num)
# #     cnt=0
# #
# #     if len(set(str_num))!=1 or len(str_num)!=4:
# #         while str_num!='6174':
# #             low=''.join(sorted(str_num)).zfill(4)
# #             high=low[::-1]
# #
# #             str_num=str(int(high)-int(low)).zfill(4)
# #             cnt+=1
# #
# #         print(cnt)
# #     else:
# #         print(False)
# #
# #
# #
# # kaprekar_constant(4371)
# # kaprekar_constant(21)
# # kaprekar_constant(1)
# # kaprekar_constant(1111)
#
#
# # import re
# # def kaprekar(num):
# #     if len(num) > 4 or re.match("0000|1111|2222|3333|4444|5555|6666|7777|8888|9999", num):
# #         return False
# #     else :
# #         for i in range(4-len(num)):
# #             num += "0"
# #         cnt = 0
# #         while True:
# #             numList = list(num)
# #             numList.sort()
# #             up = int("".join(numList.copy()))
# #             numList.reverse()
# #             down = int("".join(numList.copy()))
# #             num = str(down - up)
# #             cnt += 1
# #             if num == "6174" or cnt > 7:
# #                 break
# #         if num == "6174":
# #             return cnt
# #         elif cnt > 7:
# #             return False
# #
# # print(kaprekar("4371"))  #7
# # print(kaprekar("21"))  #3
# # print(kaprekar("1"))  #False
# # print(kaprekar("1111"))  #False