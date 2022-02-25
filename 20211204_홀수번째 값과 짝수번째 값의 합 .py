#홀수번째 값과 짝수번째 값의 합 

a = []
i = 0
e = 0
for x in range(5):
    b = int(input("숫자를 입력해주세요"))
    a.append(b)

print(a)
for n in range(5):
    if n%2 == 1:
        i+=a[n]
    else:
        e+=a[n]
print("홀수번째 값:",i)
print("짝수번째 값:",e/2) 
