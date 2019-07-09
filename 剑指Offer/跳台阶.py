#跳台阶 F(1) = 1 F(2) = 2 F(3) = F(2) + F(1) F(4) = F(3) + F(2) F(N) = F(N-1) + F(N-2)


def jumpFloor(n):

    if n == 1:
        return 1

    if n == 2:
        return 2

    sum = jumpFloor(n-1) + jumpFloor(n-2)

    return sum

print(jumpFloor(10))