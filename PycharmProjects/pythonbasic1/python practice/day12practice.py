# # 1. 2. 음수가 아닌 수들이 주어졌을 때 그 수들을 이어서 만들 수 있는 가장 큰 수를 구하시오.
# # 예를 들어 [1,2,3]이 주어졌을 때 만들 수 있는 가장 큰 수는 321이고, [3, 30, 34, 5, 9] 가 주어지면 만들 수 있는 가장 큰 수는 9534330이다.
#
# #풀이1
#
#
# #다른 풀이
# #33,45,44,47,55,99
# #[3,45,4,47,5,9]
#
# # def maxNum(input_list):
# #     num_str=[str(i) for i in input_list] #문자열로 변경
# #     max_len=max(len(i) for i in num_str) #최대 자릿수
# #
# #     reshape = []
# #     for i in num_str: # 제일 큰 길이로 숫자 다시 만들기
# #         j = i + (i[-1]*(max_len-len(i)))
# #         reshape.append(j) #reshape = [33, 30, 34, 55, 99]
#
# #     dic = {}
# #     for i in range(len(input_list)):  #딕셔너리로 만들기
# #         dic[reshape[i]] = input_list[i] #dic = {'33': 3, '30': 30, '34': 34, '55': 5, '99': 9}
# #
# #     res = ''
# #     while reshape != []: #reshape이 빌 때 까지 반복
# #         max_num = reshape[0]
# #
# #         for i in range(1, len(reshape)):
# #             if int(max_num) < int(reshape[i]):
# #
# #                 max_num = reshape[i]
# #
# #         res += str(dic[str(max_num)]) #99 55 34 33 30 -> 9534330
# #         reshape.remove(max_num)
# #
# #     return res
# #
# # print(maxNum([3, 30, 34, 5, 9]))
# # print(maxNum([1,2,3]))
#
#
#
#
#
#
#다른 풀이    largest_num([878, 88, 85, 8])
def largest_num(num_list):
    def int_to_string():
        s_number = list(map(str,num_list))
        sorted_num=sorted(s_number,key=lambda x: x[0],reverse=True)
        return sorted_num
#sorted_num=['9','5','34','30','3']
    def make_largest():
        sorted_num = int_to_string()
        ls=[]
        while sorted_num:
            if len(sorted_num)!=1:
                num_dic=dict()
                if int(sorted_num[0][0]) > int(sorted_num[1][0]):
                    ls.append(sorted_num.pop(0))
                elif int(sorted_num[0][0]) == int(sorted_num[1][0]):
                    max_len = len(str(max(list(map(int, sorted_num)))))
                    for i in sorted_num:    #largest_num([878, 88, 85, 8])
                        original = i
                        while len(i) < max_len:
                            i = i + sorted_num[0][0]
                        num_dic[i] = original
                    aaa = sorted(list(num_dic.keys()), reverse=True)
                    max_num = num_dic.get(aaa[0])
                    ls.append(max_num)
                    sorted_num.remove(max_num)
                else:
                    ls.append(sorted_num.pop())
                print("".join(ls))
                make_largest()

largest_num([3, 30, 34, 5, 9])  # 9534330

        # largest_num([878, 88, 85, 8])  # 88887885
        # largest_num([9, 93, 78, 86, 85])  # 993868578
#
#
#
#
#
#
#
# #[3,30,34,5,9]
# # ex) x= 9 55 30 52 30
#
def maxcom(x):
    num_list = []

    for i in x:  # (9,52,30,55,30)

        num = str(i)

        num_split = list(num)

        num_list.append(num_split)  # [['9'], ['5', '2'], ['5', '5'], ['3', '0'], ['3', '0']]

    first_list = []

    for i in num_list:
        first_list.append(i[0])

    first_list.sort()

    first_list.reverse()  # ['9', '5', '5', '3', '3'] 맨 앞자리 내림차순 정렬

    final = list(range(len(num_list)))  # 숫자 개수만큼의 자리 만들기

    index_list = []

    for i in num_list:

        index = first_list.index(i[0])  # 맨 앞자리 배치 순서를 인덱스로 활용

        ## ===맨 앞자리의 값이 동일할 때 에러방지를 위해 인데스를 조정해주는 과정=============

        # 인덱스는 왼쪽에서부터 찾음

        if first_list.count(i[0]) >= 2:  # 맨 앞자리가 같은 수가 2개 이상이라면

            # ['9', '5', '5', '3', '3'] 에서 앞자리가 5인 수는 모두 인덱스가 1이 됨

            l = [j for j in num_list if i[0] in j[0]]

            sortnum = []

            for k in l:  # [['5', '2'], ['5', '5']]

                joinnum = "".join(k)

                sortnum.append(joinnum)  # ['52','55']

            sortnum.sort()

            sortnum.reverse()  # ['55','52'] 순서정렬

            id = "".join(i)

            addindex = sortnum.index(id)  # 여기서 추가인덱스가 55는 0, 52는 1이됨

            index += addindex  # 앞자리가 5인 숫자의 기존 인덱스인 1에 각각 0,1을 더함

            index_list.append(index)  # 따라서 55는 1+0=1, 52는 1+1=2 의 인덱스가 주어짐

            ## ===중복되는 수 에러방지 [['3', '0'], ['3', '0']]=========================

            # 중복되는 수가 있는 경우 두 수가 같은 인덱스를 갖게되어

            # 합쳐질 때 오류가 발생함

            if index in index_list:
                addadd = index_list.count(index) - 1

                # 동일한 값이 먼저 인덱스를 부여받으면

                # 뒤늦게 인덱스를 부여받는 숫자는 앞에 먼저 인덱스를 부여받은 동일값의

                # 개수만큼 인덱스를 더해줌

                index += addadd  # 30이 두개일 때 첫번째 30이 3이라는 인덱스를 부여받으면

                # 두번째 30은 3+1의 인덱스를 부여받게됨

                # 30이 4개 있다면 마지막 30은 3+ (4-1)의 인덱스를 부여받게 되는것

        final[index] = i

    print(final)

    solve = []

    for i in final:
        solve.extend(i)

    return "".join(solve)


num = [9, 55, 30, 52, 30]

maxcom(num)
# #
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
# # 2.
# # 4개의 직사각형이 평면에 있는데 밑변이 모두 가로축에 평행하다. 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
# # 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고 겹쳐 있을 수도 있다. 또한 하나가 다른 하나를 포함할 수도 있으며,
# # 변이나 꼭지점이 겹쳐질 수도 있다.
# #
# # 입력형식
# # 하나의 직사각형은 왼쪽 아래의 꼭지점과 오른쪽 위의 꼭지점의 좌표로 주어진다. 입력은 네 줄이며,
# # 각 줄은 네 개의 정수로 하나의 직사각형을 나타낸다.
# # 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭지점의 x좌표, y좌표이고,
# # 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭지점의 x좌표, y좌표이다.
# # 단, x좌표와 y좌표는 1 이상이고 1000 이하인 정수이다.
# #
# # 출력형식
# # 화면에 4개의 직사각형이 차지하는 면적을 출력한다.
# #
# # 입력예제
# # 1 2 4 4
# # 2 3 5 7
# # 3 1 6 5
# # # 7 3 8 6
# # #
# # # 출력예제
# # # 26
# def squareArea():
#     area=set()
#     for i in range(4):
#         sq = list(map(int, input().split()))
#         for x in range(sq[0],sq[2]):
#             for y in range(sq[1],sq[3]):
#                 area.add((x,y))
#     print(len(area))
#
#
# squareArea()
# # 1 2 4 4
# # 2 3 5 7
# # 3 1 6 5
# # 7 3 8 6
#
# # #
# # # 3. 현재 페이지에 출력된 질문의 '제목' 부분을 모두 추출하여 출력하시오.
# # # 참고주소)
# # # https://stackoverflow.com/questions/tagged/python
# # #
# # from selenium import webdriver
# # driver=webdriver.Chrome('/Users/junmishin/chromedriver')
# # import time
# # url="https://stackoverflow.com/questions/tagged/python"
# # driver.get(url)
# #
# # from bs4 import BeautifulSoup
# #
# # html=driver.page_source
# # soup=BeautifulSoup(html,"html.parser")
# #
# # sp=soup.select("div.summary > h3 > a")
# #
# # for i in sp:
# #     print("제목",i.string)
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
# # # 4. 검색 포털 사이트 '네이버'에 있는 영화 댓글을 추출하시오.(가능하면 여러 페이지 추출도 ok)
# # # https://movie.naver.com/movie/bi/mi/review.nhn?code=163834&page=1
# # #
# # #
# # #
# #
# # from selenium import webdriver
# # from bs4 import BeautifulSoup
# # driver=webdriver.Chrome('/Users/junmishin/chromedriver')
# #
# #
# # url="https://movie.naver.com/"
# # driver.get(url)
# #
# # #원더우면 상세페이지 접속 버튼 경로
# #
# # path="#RESERVE_tab > a > em"
# # driver.find
#
#
