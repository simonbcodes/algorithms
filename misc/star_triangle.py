"""
Printing a Star Triangle.
This implementation uses the ^ operator for format strings, which
centers the input. Only problem with this implementation is that the
width of the centering is set at a static value, so TODO
"""


def star_triangle(n):
    """Prints a centered triangle using format strings."""
    for i in range(1, n + 1):
        print('{:^100}'.format((2 * i - 1) * '*'))


star_triangle(30)

# level of triangle | num stars
# 1                   1
# 2                   3
# 3                   5
# 4                   7
# 5                   9
# 6                   11

# num stars = 2 * level of triangle - 1
