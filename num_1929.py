# 1929번 소수구하기
# 1<= m <= n <= 1,000,000 일때 m과 n사이의 모든 소수를
# 한줄에 하나씩 오름차순으로 출력
from math import sqrt

MAX = 1000000
point = int(sqrt(MAX))
prime = [False] * 2 + [True] * (MAX - 1)
# 이렇게 저장소를 미리 만드는 것도 좋지만
# ram 제한 등이 있는 문제는 다른 방법이 필요할수도 ?

for i in range(2, point + 1):
    for k in range(2 * i, MAX + 1, i):
        prime[k] = False

m, n = map(int, input().split())

for i in range(m, n + 1):
    if prime[i] == True:
        print(i)
