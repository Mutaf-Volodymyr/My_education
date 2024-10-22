def count_numbers(s):
    dp = [[0 for _ in range(s + 1)] for _ in range(13)]
    dp[0][0] = 1
    for i in range(1, 13):
        for j in range(s + 1):
            for k in range(10):
                if j >= k:
                    dp[i][j] += dp[i - 1][j - k]
    return dp

res = count_numbers(int(input()))
for row in res:
    print(row)