"""
Print the Fibonacci series.
Using generators because they're cool and memory efficient
"""


def fib(n):
    """Generate the Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for f in fib(10):
    print(f)
