# 1. 유클리드 호제법으로 구현(뺄셈, 나눗셈)
#

def getGcd(num1, num2):    #10 6
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1




def getLcm(num1, num2):
    lcm = (num1 * num2) // getGcd(num1, num2)
    return lcm


# 2.
# 정보통신처에서는 2016년 6월 4일 인하 광장에서 이벤트를 진행하려고 한다.
# 정보통신처에서 인하 광장에 올린 게시글에 N번째로 댓글을 단 모든 학생에게 상품을 지급하기로 하였다.
# 단, N은 약수의 개수가 홀수여야 한다. 인하 광장을 즐겨보는 찬미는 이 이벤트에 참가하기로 하였다.
# 찬미는 댓글을 작성한 후 자신이 상품을 받을 확률이 얼마나 되는지 궁금해졌다. 찬미가 댓글을 작성하기 전의 총 댓글 수가 a개이고,
# 댓글을 작성 후의 총 댓글 수가 b개일 때 찬미의 댓글은 a보다 크고 b보다 작거나 같은 범위 안에 존재한다고 한다.
# 예를 들어 a가 1이고, b가 4인 경우 [2, 3, 4] 중 한 곳에 댓글이 존재한다.
# 이 중 약수의 개수가 홀수인 숫자는 4, 한 개이므로 상품을 받을 확률은 1/3이다.
# 찬미를 도와 찬미가 상품을 받을 확률을 구하는 프로그램을 작성하라.
#
# 입력
#
# 입력의 첫 줄에는 정수 a와 b가 주어진다. (1 ≤ a, b ≤ 2^60) b는 a보다 항상 크다
#
# 출력
#
# 찬미가 상품을 지급받을 확률을 기약분수 형태로 출력한다. 만약 확률이 0인 경우 0을 출력한다.
#
# 예제 입력
#
# 1 4
# 예제 출력
#
# 1/3
import fractions
def event(a,b):
    for i in range(a+1,b+1):  #i=2,3,4
        cnt=0
        case=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1

        if cnt%2!=0:
            case+=1
    if case!=0:
        res=fractions.Fraction(case,(b-a))
    else:
        res=0

    return res

print(event(1,3))





#
#
# 3.
# John과 Mary는 "J&M 출판사"를 설립하고 낡은 프린터 2대를 구입하였다.
#
# 그들이 첫번째로 성사시킨 거래는 N개의 페이지로 구성된 문서를 출력하는 일이었다.
#
# 그들이 구입한 두 대의 프린터는 각기 다른 속도록 문서를 출력하고 있다고 한다. 하나는 한 페이지를 출력하는 데 X초가 걸리고 다른 하나는 Y초가 소요된다고 한다.
#
# John과 Mary는 두 대의 프린터를 이용하여 전체 문서를 출력하는 데 드는 최소한의 시간이 알고 싶어졌다.
#
# 입력과 출력
#
# 입력데이터의 첫번 째 라인은 테스트케이스의 갯수를 뜻하고 그 갯수만큼의 라인이 추가로 입력된다. 추가되는 각 라인은 세 개의 정수값 X Y N 으로 구성된다.
# X는 첫번째 프린터가 한 페이지를 출력하는 데 드는 소요시간, Y는 두번째 프린터가 한 페이지를 출력하는 데 드는 소요시간을 뜻하고
# N은 출력할 문서의 총 페이지 수를 의미한다. (단, 출력할 문서의 총 페이지 수는 1,000,000,000개를 초과하지 않는다.)
#
# 출력은 프린팅에 드는 최소한의 시간을 테스트케이스의 갯수만큼 공백으로 구분하여 출력하도록 한다.
#
# 입출력의 예는 다음과 같다:
#
# input data:
# 1 1 5
# 3 5 4

#3 6 9 12
#5 10 15 20

# answer:
# 3 9

#3 6 9 12
#5 10 15 20
#다른 분 풀이

def printTime(p1,p2,page):

    prt_page=0
    time=0
    while prt_page<page:
        time+=1
        if time%p1==0:
            prt_page+=1
        if time%p2==0:
            prt_page+=1
    return time


n=int(input("테스트 케이스의 갯수를 입력하세요 :"))

test_case=[]
for i in range(n):
    test_case.append(list(map(int,input("테스트케이스를 입력하세요:").split())))
for j in test_case:
    print(printTime(j[0],j[1],j[2]),end="")



# #다른 분 풀이
# def printTime(x,y,n):
#     timeX=[x*i for i in range(1,n+1)]
#     timeY=[y*i for i in range(1,n+1)]
#     time=sorted(timeX+timeY)
#     print(time[n-1])
#
# printTime(1,1,5)
# printTime(3,5,4)


# 1 1 5


# 3 5 4

#3 6 9 12
#5 10 15 20

#승혀니풀이
printer = []
num = int(input())
for i in range(num):
    printer.append(list(map(int, input().split())))

def printerf(printer):  # 3 5 4
    n = 1
    cnt = 0  #cnt=1
    while(1):
        if n % printer[0] == 0:
            cnt += 1
        if cnt == printer[2]:
            break
        if n % printer[1] == 0:
            cnt += 1
        if cnt == printer[2]:
            break
        n += 1

    return n

for j in printer:
    print(printerf(j), end=" ")



#e다른 분 풀이


#전체소요시간//한 페이지를 출력하는 데 드는 소요시간 = 전체 소요시간 내 프린트 가능한 페이지 수


#
# time//X + time//X >= N 을 만족하는 시간을 구하기 위해 time을 1부터 차례대로 계산하기로 했으나
#
# 비효율적이라고 판단
#
#
#
# -> 반복문을 줄이기 위해 아래와 같이 time변수를 설정함
#
#
#
# 한장을 프린트할 때 걸리는 시간-> X, Y
#
# 단위시간당 프린트 수 -> 1/X, 1/Y
#
# N장을 뽑기 위해 필요한 최소 시간 -> N / (1/X + 1/Y)
#
# 최소시간을 올림처리(해야 하지만 math 모듈을 불러오지 않고 내림처리함) -> time


def printing(num,*line):  #line은 가변인자
    # print(num,line)  #num=2, line=("1 1 5", "3 5 4")
    for i in line:
        x,y,n=[int(j) for j in i.split(" ")]

        time=int(n/(1/x+1/y))  #계산수를 줄이기 위해 최소시간을 구함 #2.5 7.5
        while time//x + time//y < n:
            time+=1
        print(time,end=" ")

printing(3,'1 1 5','3 5 4')  #3 9