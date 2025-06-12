"""Problem 06: Fibonacci DP"""

def fibonacci(n):
    """Return nth Fibonacci number using DP."""
    if n <= 1:
        return n
    dp = [0, 1]
    for _ in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]
