# 1. 카카오 입사 코딩테스트 기출문제 (조금 어려움)
#
# 카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로,
# 모두가 간단히 즐길 수 있다.
# 갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.
#
# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수^1 , 점수^2 , 점수^3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
#
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
#
# 입력 형식
# “점수|보너스|[옵션]”으로 이루어진 문자열 3세트.
# 예) 1S2D*3T
#
# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
#
# 출력 형식
# 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# 예) 37
#
# 입출력 예제
# 예제	dartResult		answer	설명
# 1	1S2D*3T		37	1^1 * 2 + 2^2 * 2 + 3^3
# 2	1D2S#10s	9	1^2 + 2^1 * (-1) + 10^1
# 3	1D2S0T		3	1^2 + 2^1 + 0^3
# 4	1S*2T*3S	23	1^1 * 2 * 2 + 2^3 * 2 + 3^1
# 5	1D#2S*3S	5	1^2 * (-1) * 2 + 2^1 * 2 + 3^1
# 6	1T2D3D#		-4	1^3 + 2^2 + 3^2 * (-1)
# 7	1D2S3T*		59	1^2 + 2^1 * 2 + 3^3 * 2
import re


def dart(dartResult):
    p=re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores=p.findall(dartResult)
# scores=[('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]

    print(scores)
    result = []

    for idx,score in enumerate(scores):   #0   1    2
        point=scores[0]
        bonus=scores[1]
        option=scores[2]
        if bonus =="S":
            bonus = 1
        elif bonus =="D":
            bonus =2
        elif bonus =="T":
            bonus = 3
        if option =="*":
            if idx==0:     #*가 처음에 나오면
                result.append(int(point)**bonus*2)

            else:
                result[-1]*=2
                result.append(int(point)**bonus*2)
        elif option=="#":
            result.append(int(point)**bonus*-1)
        else:
            result.append(int(point)**bonus)

    return sum(result)






#다른분이 푼거
def dart(text):
    lis=[]
    n=''
    for i in text:
        if i.isnumeric():  #숫자점수면 저장
            n +=i
        elif i=='D':
            lis.append(int(n)**2)
            n=''
        elif i=='T':
            lis.append(int(n)**3)
            n=''
        elif i =='S':
            lis.append(int(n)**1)
            n=''
        elif i=='*':
            if len(lis) >1: #두번째 게임 이상

                lis[-2] *=2

            lis[-1]*=2 #2번째 점수 --> *이 두개일때 고려

        elif i=='#':
            lis[-1]*=-1

    return sum(lis)


dartResult =input('dart:')
print(dart(dartResult))





#다른 분
def cashSize(a,b):
    lower_li=[]
    for i in b:
        i=i.lower() #소문자화
        lower_li.append(i)
    print(lower_li)
    cash=[]

    time=0


    for d in b:
        if a==0:
            time+=5

        elif d not in cash and len(cash)!=a:
            cash.append(d)
            time+=5

        elif d not in cash and len(cash)==a:
            cash.remove(cash[0])
            cash.append(d)
            time+=5

        elif d in cash:
            time+=1

    return time









#
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer






#
# 2. 카카오 입사 기출문제 (어려움)
#
# 지도 개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
# 이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
# 어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.
#
# 어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
#
# 입력 형식
# 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
# cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
# cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
#
# 출력 형식
# 입력된 도시이름 배열을 순서대로 처리할 때, “총 실행시간”을 출력한다.
#
# 조건
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# - LRU는 가장 오래전에 참조된 데이터를 교체하는 알고리즘
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.
#
# 입출력 예제
# 캐시크기(cacheSize)	도시이름(cities)							  	       		실행시간
# 3	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]				50
# 3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]					21
# 2	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]		60
# 5	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”, “SanFrancisco”, “Seoul”, “Rome”, “Paris”, “Jeju”, “NewYork”, “Rome”]		52
# 2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]									16
# 0	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]								25
#
#
# 3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]      21
# 캐쉬크기 : 3
# 캐쉬 =[  “Pangyo”,“Seoul”,“NewYork”,  ]
# 소요시간 : 5+5+5+1+1+1+1+1+1=21
#
# 2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]
#
# , “Pangyo”,“NewYork”
#



#다른사람 풀이
# LRU 알고리즘
# def cacheProcess(data, cache_size):
#     if cache_size == 0:  # 캐시가 없으면 바로 return
#         return len(data) * 5
#     count = 5  # 어차피 처음 들어가는 놈은 무조건 +5 니까 애초에 5로 선언
#     cache = []
#     cache.append(data.pop().lower())  # 대소문자 구분 안하기 때문에 대소문자 일괄 통일하여 넣기
#     for i in range(len(data) + 1):  # data 크기만큼 돌기
#         if not data:  # 비어있다면 return
#             return count
#         a = data[-1].lower()  # 나는 걍 뒤부터 하나씩 뽑아냄
#         if a in cache:  # 뽑은 도시가 cache에 있다면 +1
#             count += 1
#             cache.remove(a)  # LRU의 특징인 최근 검색 자료를 제일 앞으로 보내주기 위해 과거의 cache 지우고
#             cache.append(data.pop().lower())  # 새로운 것을 넣어 MRU 위치에 넣어줌
#         else:
#             if len(cache) == cache_size:  # cache 사이즈가 꽉 차면 LRU를 지움
#                 del cache[0]
#             cache.append(data.pop().lower())
#             count += 5

def solution(cacheSize, cities):
    runtime, cache = 0, []  # 실행시간, 캐시
    if not cacheSize: # 캐시 사이즈가 0이라면
        return 5 * len(cities)
    for city in cities:
        city = city.upper()  # 대문자로 통일
        if city in cache:  # cache안에 city가 있다면
            cache.remove(city) # cache에서 city를 삭제
            runtime += 1
        else:
            if len(cache) >= cacheSize:  # cach가 꽉 찼다면
                cache.pop(0)  # 가장 안쓰인 요소를 삭제
            runtime += 5
        cache.append(city)  # 새로운 요소를 캐시에 추가
    print(runtime)
    return runtime





#
def solution(cacheSize,cities):
    cache=[]
    answer=0

    if cacheSize ==0:
        return len(cities)*5

    for i in cities:
        j=i.lower()

        if not j in cache:
            if len(cache)<cacheSize:
                cache.append(j)

            else:
                cache.pop(0)
                cache.append(j)

        else:
            cache.pop(cache.index(j))
            cache.append(j)
            answer+=1

    return answer

