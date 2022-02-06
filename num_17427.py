# 17427번 약수의 합 2
# 1~n 까지의 모든 수의 약수의 합을 구하시오
n = int(input())
ns = range(2, n + 1)
""" try 1 아무리 뜯어봐도 시간초과 .... 원인이 뭘까?
#1~n 까지 소수판별 에라토스테네스의 채
a = [False,False] + [True] * (n-1)
for i in ns:
    if a[i]: # True 상태이면
        for k in range(2*i, n+1, i): #자기자신은 놔두고 다음부터
            a[k] = False #그 배수를 전부 False로 변환
# a = 1~n까지 소수를 걸러낸 채가 된다.
sum = (n-1) + int((n+1)*n/2) # 1~n까지 (1+자기자신) 의 합
for i in ns:
    if not a[i]:
        for k in range(2,int(i**(1/2))+1):
            if i % k == 0:
                if i != k**2:
                    sum += (i//k + k)
                else:
                    sum += k
"""

"""try 2 배수를 잘 살펴봤다. 가만 보니 1~n까지의 표에서
모든 약수들의 합은 각 수(x)의 x * (n//x)와 같다.
x의 배수에는 모두 약수로 x를 가지고 있기 때문에 그 갯수만큼 더해주면 된다.
이를 이용헤 코드를 구현해보자.
"""
sum = n
for i in ns:
    sum += i * (n // i)

print(sum)

# 결론: 문제를 잘 파악하고 해결하기 위한 합리적인 구조를 추론하는것이 중요
