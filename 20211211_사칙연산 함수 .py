#사칙연산 함수 

def plus(one,two,three):
    print(one+two+three)

def minus(one,two,three):
    if one>two and two>three or one>three and three>two: 
        print(one-two-three)
    elif two>one and one>three or two>three and three>one:
        print(two-one-three)
    elif three>one and one>two or three>two and two>one:
        print(three-two-one)

def mul(one,two,three):
    print(one*two*three)

def div(one,two):
    print(one/two)

plus(1,2,3)
minus(1,2,3)
mul(1,2,3)
div(6,2)

