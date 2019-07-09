#斐波那契数列 F(1)=1 F(2)=2 F(N)=F(N-1)+F(N-2)


#递归
def Fibonacci_1(n):

    if n == 1:
        return 1
    if n == 2:
        return 2


    sum = Fibonacci_1(n-1) + Fibonacci_1(n-2)

    return sum

def Fibonacci_2(n):
    result , next_item = 0,1
    for i in range(n):
        result,next_item = next_item,next_item+result

    return result

print(Fibonacci_2(10))