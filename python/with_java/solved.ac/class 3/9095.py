t = int(input())

ns = []
for _ in range(t):
    n = int(input())
    ns.append(n)

dp = [0, 1, 2, 4]
for i in range(4, max(ns)+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for n in ns:
    print(dp[n])
