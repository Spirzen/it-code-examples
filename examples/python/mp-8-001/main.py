# max, дискретные состояния 0..S
T = 4
S = 10
dp = [[0] * (S + 1) for _ in range(T + 2)]

for t in range(T, 0, -1):
    for s in range(S + 1):
        best = float("-inf")
        for u in range(s + 1):
            val = g(t, u) + dp[t + 1][s - u]
            if val > best:
                best = val
        dp[t][s] = best

answer = dp[1][S]
