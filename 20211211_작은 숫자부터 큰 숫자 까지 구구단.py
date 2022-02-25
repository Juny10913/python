#작은 숫자부터 큰 숫자 까지 구구단 
a= int(input("숫자를 입력해주세요"))
b= int(input("숫자를 입력해주세요"))
def mul(one,two):
    if one>two:
        for x in range(two,one+1):
            for y in range(1,10):
                 print(x,"*",y,"=",x*y)
    elif two<one:
        for n in range(one,two+1):
            for m in range(1,10):
                 print(n,"*",m,"=",n*m)
mul(a,b)

