# 17425번 약수의 합
# 첫째줄에는 테스트 케이스의 갯수
# 둘째줄 부터는 각 테스트 케이스가 한줄씩 주어짐.
# 각각의 테스트 케이스마다, 한 줄에 하나씩 g(N)를 출력한다.
# g(n)은 1~n까지 각각의 약수의 합의 합

""" try 1
from math import sqrt as msqrt
from math import prod as mprod
from operator import add,mul,sub
def sum_divisor(n):
    sum = n
    sr = int( msqrt(n) )
    end = n
    for k in range(2, sr+1):
        start = n//k
        sum += add( mprod( ( sub(k,1) , sub(end,start) , add(mul(2,start+1),sub(end,start+1) )/2) ) , ( mul(k,(n//k)) ) )
        end = start
    #print('%d'%(sum))
    return sum
# 수열의 합 공식 n * ( 2a + (n-1) * d )/2
"""

# 자꾸 시간초과가 된다 ..... why ?????
# 숫자를 여러번 구하는데 각각 다 구해서 그런건가 ???
# 이전의 계산했던 정보를 활용하는 코드를 추가하자. ㄴㄴㄴ
# 사실 계산 그 자체 말고는 크게 속도에 문제가 없는것으로 보임.
# 계산 자체에서 비효율적으로 많이 반복되는 부분을 삭제하자.
# 1. 범위를 2~n+1 에서 n//2+1로 줄이고, 줄인부분은 수열의 합 공식.
# 1을 응용해서 적절한 범위까지만 수열의 합 공식 사용.
# 아무리 operator,math 등 사용해도 느리다 ......
# 리스트를 미리 만들까...?
# 웹서핑중 Dynamic Programming 이라는 것을 발견
# But, 이 문제를 풀며 알게된건
# 시간을 측정하는 방식이 input을 받기 시작하는 시점부터
# 출력을 마칠때 까지 ...
# 미리 뭔가를 만들어 놓으면 시간 아끼기 가능
# 출력하는 시간 조차도 한개 입력 한개 출력 하는식으로 하면 시간낭비됨.
# 한번에 받아서 한번에 출력할 것!
MAX = 1000000
dp = [0] * (MAX + 1)  # dp[i] = i의 약수의 합
s = [0] * (MAX + 1)  # 누적 합 계산

for i in range(1, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    s[i] = s[i - 1] + dp[i]  # 누적 합 list 완성

N = int(input())

for i in range(N):
    n = int(input())
    print('%d' % (s[n]))
