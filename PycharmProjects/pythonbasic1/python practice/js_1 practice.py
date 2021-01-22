# 1.
# 3개의 각으로 삼각형의 예각, 직각, 둔각을 구별하는 프로그램을 만들어라.
#
# [60, 60, 60] = 예각삼각형
# [30, 60, 90] = 직각삼각형
# [20, 40, 120] = 둔각삼각형
# [0, 90, 90] = 삼각형이 아니다
# [60, 70, 80] = 삼각형이 아니다
# [40, 40, 50, 50] = 삼각형이 아니다
#
# 예각삼각형 : 3개의 각이 모두 예각인 삼각형
# 직각삼각형 : 1개의 각이 직각인 삼각형
# 둔각삼각형 : 1개의 각이 둔각인 삼각형
# ① 각이 3개가 아닐 경우 삼각형이 아니다.
# ② 3개의 각의 합이 180°가 아닐 경우 삼각형이 아니다.


def triangle_idf(n):
    if sum(n)==180 and len([i for i in n if i > 0])==3 :
        for i in range(len(n)):
            if n[i] == 90:
                print("직각삼각형")
                break
            elif n[i] > 90:
                print("둔각삼각형")
                break
            elif i == len(n) - 1:
                print("예각삼각형")

    else:
        print("삼각형이 아닙니다.")


n = list(map(int, input().split()))  # input = 30 60 90
triangle_idf(n)


# angles=list(map(int,input("3개의 각을 입력하세요: ").split(" ")))
# if len(angles) != 3 or sum(angles) != 180 or min(angles) == 0:
#     print("삼각형이 아닙니다.")
# else:
#     if max(angles) < 90:
#         print("예각삼각형")
#     elif max(angles) == 90:
#         print("직각삼각형")
#     elif max(angles) > 90:
#         print("둔각삼각형")


 # 2.
# 아래는 괄호를 이용한 연산식이다.
# (5+6)∗(7+8)/(4+3)
# 우리는 여는 괄호가 있으면 닫는 괄호가 반드시 있어야 한다는 것을 잘 알고 있다.
# 다음은 정상적인 괄호 사용의 예이다.
# (()()()())
# (((())))
# (()((())()))
# 다음은 비정상적인 괄호 사용의 예이다.
# ((((((())
# ()))
# (()()(()
# (()))(
# ())(()
# 괄호의 사용이 잘 되었는지 잘못 되었는지 판별 해 주는 프로그램을 작성하시오.
#


def bri(st):
    li=[]
    brilist=list(st)
    for i in range(len(st)):
        if i=="(":
            li.append(i)

        if i==")":
            li.pop()





# 8
# (((())))
def parenthesis(data):
    cnt1, cnt2 = 0, 0
    for i in range(len(data)):
        if cnt2 > cnt1:  #())(() 이런 경우에는 비정상이기 때문에
            print("비정상")
            break
        if data[i] == "(":
            cnt1 += 1
        elif data[i] == ')':
            cnt2 += 1
        if i == len(data) - 1:
            if cnt1 == cnt2:
                print("정상")
            else:
                print("비정상")


data = input()
parenthesis(data)





















#

def bracket(add):
    repo=[]
    for i in range(len(add)):
        if add[i]=='(':
            repo.append('(')
        else:
            if len(repo)==0:
                return "비정상"
            else:
                repo.pop()
    if len(repo)==0:
        return "정상"
    else:
        return "비정상"
bracket('((()(')






#다른사람 풀이
def brk(brckString):
    l = []
    brckList = list(brckString)  # "("보다 ")"가 많을 경우를 생각해야 하므로
    for i in range(len(brckString)):
        if brckString[i] == "(":
            l.append(brckString[i])
            brckList.remove(brckString[i])  # l에 추가된 기호는 삭제
        elif brckString[i] == ")":
            if len(l) > 0:
                l.pop()
                brckList.remove(brckString[i])  # l에 추가된 기호는 삭제
            else:  # "("보다 ")"이 먼저, 많이 나온 경우
                break  # 실행을 멈추므로 l에 추가된 기호를 brckList에서 지우던 것도 중단
    if len(l) == 0 and len(brckList) == 0:  # 정확히 매치가 되었다면 brckList에 어떤 문자도 남지 않았을 것
        print("정상적인 괄호 사용입니다")
    else:
        print("비정상적인 괄호 사용입니다")

brk("((((((())")  # 비정상적인 괄호 사용입니다
brk("()))")  # 비정상적인 괄호 사용입니다
brk("(()()(()")  # 비정상적인 괄호 사용입니다
brk("(()))(")  # 비정상적인 괄호 사용입니다
brk("())(()")  # 비정상적인 괄호 사용입니다
brk("(()((())()))")  # 정상적인 괄호 사용입니다

def brk(brckString):
    l = []
    brckList = list(brckString)
    for i in range(len(brckString)):
        if brckString[i] == "(":
            l.append(brckString[i])
            brckList.remove(brckString[i])
        elif brckString[i] == ")":
            if len(l) > 0:
                l.pop()
                brckList.remove(brckString[i])
            else:
                break
    if len(l) == 0 and len(brckList) == 0:
        print("정상적인 괄호 사용입니다")
    else:
        print("비정상적인 괄호 사용입니다")









def bracket(text):

    temp=[]
    for i in text:
#print(i)
        if i=='(':
            temp.append('(')
        else:
            if len(temp)==0:
                return("비정상")
            elif(len(temp)>0):
                temp.pop()
                if len(temp)==0:
                    return("정상")
                else:
                    return("비정상")