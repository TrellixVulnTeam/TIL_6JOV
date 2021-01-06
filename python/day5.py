# def add(a,b):
#     sum=a+b
#     return sum
#
# res=add(1,2)
#
# print(res)
#
# def say():
#     return "안녕"
# s=say()
#
# print(s)
#
# def add(a,b):
#     print("두 수의 합은: ",a+b)
# add(3,4)
#
#
# def say():
#     print("안녕")
# say()
#
# #
# def add(a,b):
#     return a+b
# res=add(b=2,a=3)
# print(res)



# def add(a=1,b=3):
#     print(a)
#     print(b)
#     return a+b
# res=add(10,20)
# print(res)
#
#
#
#
# def add(*arg):
#     res=0
#     for i in arg:
#         res+=i
#     return res
# res=add(1,2,3,4)
# print(res)


def addmul(a,*arg):
    if a =="add":
        result = 0
        for i in arg:
            result+=i
    elif a =="mul":
        result = 1
        for i in arg:
            result*=i

    return result

print(addmul("add",1,2,3,4))









