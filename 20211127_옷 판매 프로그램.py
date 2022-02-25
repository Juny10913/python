#옷 판매 프로그램 
dis = 0
price = 0


print("패딩:100000원, 롱패딩:150000원, 내복:50000원")
b = input("픔목을 입력해주세요")
a = input("등급을 입력해주세요")

if b == '패딩':
    c = 100000
elif b == '롱패딩':
    c = 150000
elif b == '내복':
    c = 50000
else:
    print("잘못 입력하셨습니다")

if a == 'G':
    dis = int(c * 0.7)
    price = int(c * 0.3)
elif a == 'S':
    dis = int(c * 0.5)
    price = int(c * 0.5)
elif a == 'B':
    dis = int(c * 0.3)
    price = int(c*0.7)
else:
    print("없는 등급입니다")
print(c,"원에서",dis,"원이 할인되서",price,"원 입니다")


    

    
    

      

