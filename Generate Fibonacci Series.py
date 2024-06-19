def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Program to take input from the user
n = int(input("Enter the number of terms: "))
fib_sequence = generate_fibonacci(n)
print("Fibonacci sequence up to", n, "terms:", fib_sequence)
