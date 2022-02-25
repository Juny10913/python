#자판기 프로그램 

print("1.아메리카노:2800")
print("2.카페라때:2700")
print("3.핫초코:2300")
a = int(input("커피의 종류를 입력하시오"))
if a==1:
    selected = 2800
elif a==2:
    selected = 2700
elif a==3:
    selected = 2300
else:
    print("잘못입력하시오")
b = int(input("몇잔을 드릴까요?"))
print("총 금액은",selected*b)
c = int(input("돈을 투입해주세요"))
left = c-selected*b
print("거스름돈은",left,"원입니다")
won1000 = left//1000
won500= left%1000
won100 = won500%500
won100 = won100//100
won500 = won500//500


print("1000원:",won1000,"개","500원:",won500,"개", "100원:",won100,"개")






