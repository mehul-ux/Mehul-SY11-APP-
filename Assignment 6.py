def top_down(weights, values, capacity):
    n = len(weights)
    dp = {}

    def solve(n, capacity):
        if n == 0 or capacity == 0:
            return 0

        if (n, capacity) in dp:
            return dp[(n, capacity)]

        if weights[n - 1] > capacity:
            dp[(n, capacity)] = solve(n - 1, capacity)
        else:
            take = values[n - 1] + solve(
                n - 1, capacity - weights[n - 1]
            )
            not_take = solve(n - 1, capacity)

            dp[(n, capacity)] = max(take, not_take)

        return dp[(n, capacity)]

    return solve(n, capacity)


def bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [1, 3, 4, 5]
values = [2, 6, 7, 10]
capacity = 7

# Results
print("Top-Down Result:", top_down(weights, values, capacity))
print("Bottom-Up Result:", bottom_up(weights, values, capacity))
