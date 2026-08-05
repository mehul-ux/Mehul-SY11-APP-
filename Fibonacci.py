def fibonacci(n):
    if n < 0:
        print("Please enter a non-negative integer.")
        return

    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev2, prev1 = 0, 1

    for i in range(2, n + 1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current

    return prev1


# Take input from the user
n = int(input("Enter the value of n: "))

# Display the nth Fibonacci number
result = fibonacci(n)
if result is not None:
    print(f"The {n}th Fibonacci number is: {result}")