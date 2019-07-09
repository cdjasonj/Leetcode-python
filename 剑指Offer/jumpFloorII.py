#一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#递归 f(1) = 1 f(2) = 2 f(3) = f(1)+f(2)+1  f(n) = f(n-1)+...f(1) +1


def jumpFloorII(num):
    if num ==1 or num == 0:
        return 1
    if num ==2 :
        return 2
    sum = 0
    for i in range(0,num): #0 就返回1
        sum += jumpFloorII(i)
    return sum

print(jumpFloorII(10))