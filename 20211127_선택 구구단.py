#선택 구구단 
a,b = input("a,b를 입력해주세요").split(",")
a = int(a)
b = int(b)
for x in range(a,b+1):
    for y in range(1,10):
        print(a,"*",y,"=",a*y)
    a+=1
    
