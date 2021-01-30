# def wakeupearly(h,m):  #10,10
#
#     if h==0:
#         if m>45:
#             m=m-45
#         else:
#             h=23
#             m=60-(45-m)
#     else:
#         if m>45:
#             m=m-45
#         else:
#             h=h-1
#             m=60-(45-m)
#     return h,m
#
# print(wakeupearly(0,46))




def yoonyear(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return 1
    else:
        return 0


print(yoonyear(2000))





n=list(map(int,input("고정비용,가변비용,노트북가격을 순서대로 입력하세요").split()))


if n[1]>=n[2]:
    print(-1)

else:
    print((n[0] / (n[2] - n[1])) + 1)



# a + b * i < c * i

# a+b*i<c*i
# a<c*i-b*i
# a<(c-b)*i




