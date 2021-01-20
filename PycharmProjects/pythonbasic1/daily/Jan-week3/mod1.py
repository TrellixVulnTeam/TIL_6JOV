def madd(a,b):
    return a+b

def msub(a,b):
    return a-b

if __name__=="__main__":
    print("__name__ 값 : ", __name__)
    print(madd(3,2)) #5
    print(msub(10,3)) #7
else :
    print("__name__ 값 : ", __name__)

#mod1.py를 실행시키면  __name__이라는 특별한 변수의 값으로 __main__이 저장됨.
#따라서 if __name__=="__main__": 조건식이 참이 됨
