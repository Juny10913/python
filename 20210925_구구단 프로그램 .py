#구구단 프로그램 
a = int(input("첫번째 숫자를 입력해주세요"))
b = 1
for x in range( 1,9*a,a):
    print(a,"X",b,"=",a*b)
    b = b+1
