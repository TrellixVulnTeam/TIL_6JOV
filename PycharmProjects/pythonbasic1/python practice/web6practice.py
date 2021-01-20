# # 1.
# # A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
# #
# # 버전은 다음처럼 "." 으로 구분된 문자열이다.
# #
# # 버전 예) 1.0.0, 1.0.23, 1.1
# #
# # 두 개의 버전을 비교하는 프로그램을 작성하시오.
# #
# # 다음은 버전 비교의 예이다.
# #
# # 0.0.2 > 0.0.1
# # 1.0.10 > 1.0.3
# # 1.2.0 > 1.1.99
# # 1.1 > 1.0.1
# ##############################################################################
# #
# def version(ver1, ver2):
#     for i in range(len(ver1)):
#         if ver1[i] > ver2[i]:
#             return ">"
#         elif ver1[i] < ver2[i]:
#             return "<"
#         else:
#             pass
#
# a = input().split()
# ver1 = a[0]
# ver2 = a[1]
# print(str(ver1), version(ver1.split('.'), ver2.split('.')), str(ver2))
#
# #############################################################################
#
# # def comnum(a,b):
# #     a1=list(map(int,a.split('.')))
# #     b1=list(map(int,b.split('.')))
# #     for i in range(min(len(a1),len(b1))):
# #         if a1[i]>b1[i]:
# #             return a+">"+b
# #
# #         elif a1[i]==b1[i]:
# #             continue
# #         else:
# #             return a+"<"+b
# #
# # print(comnum("1.0.3","1.0.3"))
#
#
# #############################################################################
#
#
# # 2.
# # 약 2,000년 전에는 전쟁에서 병사들이 적들에 의해 동굴에 갇히게 되는 경우가 종종 있었다고 한다.
# # 그들은 포로가 되는것을 방지하기 위해 동그랗게 서서 마지막 한 사람이 남을 때 까지 순서대로 돌아가며 세번째에 해당되는 사람을 죽여 나갔다고 한다.
# # 마지막으로 남게되는 사람은 자살하기로 약속되어 있었지만 보통 적들에게 항복을 하는 경우가 많았다고 한다.
# # 여러분이 풀어야 할 문제는 총 인원수(N)와 간격(K)이 주어졌을 때 가장 마지막에 살아남는 병사의 위치(the safe position)를 알아내는 것이다.
# # 예를 들어 병사수가 총 10명이고 돌아가며 세번째에 해당되는 병사를 제거하는 경우는 다음과 같다:
# # N = 10, K = 3
# # 위의 경우 다음과 같은 순서로 병사들이 제거된다. (괄호는 제거되는 병사를 의미한다)
# # 1st round: 1 2 (3) 4 5 (6) 7 8 (9) 10
# # 2nd round:                            1 (2) 4 5 (7) 8 10
# # 3rd round:                                                (1) 4 5 (8) 10
# # 4th round:                                                               4 (5) 10
# # 5th round:                                                                        4 (10)
# # 위 예에서 끝가지 살아남는 병사는 4, 즉 4번째 병사이다.
# # 입력 데이터는 총 병사수 N과 간격 K이다.
# # 출력 데이터는 마지막까지 살아남는 병사의 위치이다.
# # (단, 최초 시작은 1번 병사부터이다.)
# # 입출력 예는 다음과 같다:
# #
# # initial data:
# # 10 3
# #
# # answer:
# # 4
#
# #10
# #3 6 9
#
#
# #강사님 풀이(요세푸스 문제)
#
# def sol(n,k): #n=10, k=3
#     a=list(range(1,n+1)) #a=(1,2,3,4,5,6,7,8,9,10)
#     j=k-1 #j=3-1=2
#     b=0
#     while(len(a)>1):
#         b=(len(a)+b)%k  # (5+2)%3 => 나머지=1, b=1
#         del a[j::k]   #a[0::3]
#         j=k-b-1 #j=3-1-1=0   => j=1
#     return a #마지막살아남은1명병사
# print(sol(10,3)) #총 10명 병사, 3명 간격으로 자살
#
#
#
#
#
# #다른사람 풀
# N,K = input("N K: ").split(" ")
#
# N=int(N)
#
# K=int(K)
#
# humanlist=list(range(1,N+1))
#
# build =[]
#
# temp=[]
#
# while True:
#
#     for i in humanlist:
#
#         build.append(i)
#
#         if len(build)== K:
#
#             temp.append(build.pop())
#
#             build=[]
#
#             humanlist = [x for x in humanlist if x not in temp]# 차집합처럼human-temp 해주기
#
#         if len(humanlist)==1:
#
#             break
#
#             print(humanlist)
#
#
#
#
# #############################################################################
#
#             a, b = map(int, input().split())
#             myList = []
#             for i in range(1, a + 1):
#                 myList.append(i)
#
#             cnt = b - 1 #k=3이면 제거해야 할 인덱스 값은 2
#             cnt2 = 0
#             while len(myList) != 1:
#                 del (myList[cnt - cnt2])
#                 cnt += b
#                 cnt2 += 1 #제거한 수 만큼 인덱스 더해줌
#
#                 print(myList)
#                 if cnt >= a: #제거해야할 인덱스 넘버가 전체 길이 이상이되면
#                     cnt -= a #cnt를 인덱스 넘버에서 전체길이를 빼준 값으로 초기화시켜서 다시 while문에 넣음
#                     a = len(myList) #a도 제거한 값을 빼준 리스트로 초기화
#                     cnt2 = 0
#
#             print(myList)
#
#
#
#
#
#
#
#
#
# # 3.
# # 텍스트가 입력으로 주어질 때, 단어의 개수를 세는 프로그램을 작성한다.
# # "문자 세기"와 "단어 세기"는 프로그래밍 입문에 성공했는지를 가늠하는 문제라고 할 수 있습니다.
# #
# # 입력
# # 아래 내용을 가진 텍스트파일을 미리 만들어 두고, 프로그램을 실행하면 파일 내용을 읽어들인다(출처: Wikipedia).
# # As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service.
# #
# # 출력
# # 구분자(Separator)는 마침표 '.', 쉼표 ',', 공백 ' ' 이다.
# # 가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도를 출력한다.
# # 빈도가 같은 단어들 사이의 순서는 무시한다.
# #
# # in 12
# # the 10
# # Bolikango 5
# # a 4
# # of 4
# # and 3
# # to 3
# # his 3
# # became 2
# # government 2
#
# line="As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service."
#
#
# import re
#
# with open("a.txt", 'r') as f:
#     txt = f.read()
#
# p = re.compile('[a-zA-Z0-9]+')
# myList = p.findall(txt)
#
# dic = {}
#
# for i in myList:
#     if dic.get(i):
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# ans = {}
# cnt=0
# for j in sorted(dic, key=dic.get, reverse=True):
#     ans[j] = dic[j]
#     cnt += 1
#     if cnt == 10:
#         break
# print(ans)
#
# #다른사람 풀이
# with open("q3.txt","r") as r:
#
#     intext=r.readline()
#
#
# import re
#
# lis = re.findall("[\w]+",intext)
#
#
# d1={}
#
# for word in lis:
#
#     d1[word] = d1.get(word,0)+1
#
#     sdict = sorted(d1.items() , key=lambda x:x[1], reverse=True)
#
#     print(sdict[0:10])
#
#
# #강사님풀이
#
# from collections import Counter
# with open("input.txt","r") as f:
#     words=[w.strip(".," for w in f.read().split())]
# for w,c in counter(words).most_common(10)   #가장 많이 사용된 단어 10개를 뽑아내는것
#     print(w,c)
#
#
#
#
# # 4. 테이블문제 1
# #배경색은 흰색으로
#
# #
# # <html>
# #
# # <head>
# #     <style>
# #         table{
# #         border:1px solid #000ff; border-collapse:collapse;}
# #
# #         th,td{
# #         border:3px solid #0000ff;
# #         }
# #         th{background-color:skyblue;}
# #         td{background-color:pink;}
# #
# #     </style>
# #
# #
# # </head>
# #
# # <body>
# # <h1 align="center">24회 전국정보과학창의성대</h1>
# #
# # <table align="center" width="400px" height="200px">
# #     <tr>
# #     <th>부문</th>
# #         <td>웹프로그래밍</td>
# #         <td rowspan="3" width="150px" align="center">사진</td>
# #     </tr>
# #
# #
# #      <tr>
# #     <th>수강번호</th>
# #         <td>1234</td>
# #     </tr>
# #
# #      <tr>
# #     <th>성명</th>
# #         <td>홍길동</td>
# #     </tr>
# #
# #
# #      <tr>
# #     <th>좌우명</th>
# #         <td colspan="2" align="center">화이팅!</td>
# #     </tr>
# #
# #
# #
# # </table>
# #
# #
# # </body>
# #
# # </html>
#
#
#
#
#
#
# #
# # 5. 테이블문제 2
#
#
#
