def generate_fibonacci(n):
    if n <= 0:
        return "Number of terms must be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

fibonacci_sequence = generate_fibonacci(n)

print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")
