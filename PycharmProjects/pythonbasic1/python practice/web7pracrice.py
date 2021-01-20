# 1. 아마존 면접문제
#
# A사무실에는 특정일자의 출퇴근 시간이 기록된 거대한 로그파일이 있다고 한다.
#
# 파일의 형식은 다음과 같다. (한 라인에서 앞부분은 출근시간(HH:MM:SS), 뒷부분은 퇴근시간이다)
#
# 09:12:23 11:14:35
# 10:34:01 13:23:40
# 10:34:31 11:20:10
# 특정시간을 입력(예:11:05:20)으로 주었을 때 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.
#

def office(n):
    cnt = 0
    n = n.replace(':', '')
    with open('time.txt', 'r') as f:
        time = f.readlines()

    for t in [j.split() for j in (i.strip() for i in time)]:  #\n제가한 후 공백단위로 구분해 각각 list에 넣어 for문으로..
        if int(n) - int(t[0].replace(':', '')) >= 0 and int(t[1].replace(':', '')) - int(n) >= 0:
            cnt += 1
    return cnt


n = input()
print('{0}]시에는 {1}명이 사무실에 있었습니다.'.format(n,office(n)))




#다른분이 한 것

def readtext(worklist):
    with open(worklist,"r") as f:
        a = f.read()
    a = a.split("\n")                                 #개행문자를 기준으로 스플릿 [,,]
    people = len(a)
    inout = [a[i].split() for i in range(people)]     #띄어쓰기 기준으로 스플릿[[],[],[]]
    return inout

def workman(worklist,nowtime):
    a=readtext(worklist)
    b=len(a)
    num=0
    for i in range(b):
        a[i].append(nowtime)
        a[i].sort()
        if a[i][1]==str(nowtime):
            num+=1
    print(num)

workman("inandout.txt","11:11:11")
# 2. 웹페이지 작성






dlfkjskljfklds

