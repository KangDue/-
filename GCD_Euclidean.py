# 유클리드 호제법을 이용한 최대공약수 구하기 알고리즘

def gcd(*x):
    xs = range(len(x) - 1)
    ans = x[0]
    for i in xs:
        a, b = (ans, x[i + 1]) if ans > x[i + 1] else (x[i + 1], ans)
        if a == b:
            ans = a
        else:
            while 1:
                r = a % b
                if r == 1:
                    return 1
                elif r == 0:
                    ans = b;
                    break
                a = b;
                b = r
    return ans


print(gcd(7, 24, 32))
