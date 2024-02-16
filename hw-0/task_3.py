import math
import re

eq_matcher = re.compile('(-?\d*\*?x\*\*2)?([+-]?\d*\*?x)?([+-]?\d*)?=0')


def parse(eq_str):
    a, b, c = 0, 0, 0

    sanitized = eq_str.replace(' ', '')
    matches = eq_matcher.match(sanitized)

    a_group = matches.group(1)
    b_group = matches.group(2)
    c_group = matches.group(3)

    if a_group is not None:
        a_group = a_group.replace('*', '').replace('x2', '')
        if a_group in ['+', '-', '']:
            a_group += '1'

        a = float(a_group)

    if b_group is not None:
        b_group = b_group.replace('*', '').replace('x', '')
        if b_group in ['+', '-']:
            b_group += '1'

        b = float(b_group)

    if c_group is not None and c_group != '':
        c = float(c_group)

    return [a, b, c]


def calc(arr):
    # no solutions if only 'c' param provided
    if arr[0] == 0 and arr[1] == 0:
        return []
    # if no 'a' param
    elif arr[0] == 0:
        return [-arr[2] / arr[1]]
    elif arr[2] == 0:
        # 0 is always solution if no 'c' param
        r = [0.0, -arr[1] / arr[0]]
        return r if r[0] < r[1] else [r[1], r[0]]

    d = arr[1] * arr[1] - 4 * arr[0] * arr[2]

    # no solutions
    if d < 0:
        return []
    elif d == 0:
        # only one solution
        return [-arr[1] / (2 * arr[0])]

    # happy path
    x1 = (-arr[1] - math.sqrt(d)) / (2 * arr[0])
    x2 = (-arr[1] + math.sqrt(d)) / (2 * arr[0])

    return [x1, x2] if x1 < x2 else [x2, x1]


def to_human_repr(arr):
    # solutions must be readable
    if len(arr) == 2:
        return 'x_1 = {x1}, x_2 = {x2}'.format(x1=arr[0], x2=arr[1])
    elif len(arr) == 1:
        return 'x = {x}'.format(x=arr[0])

    return 'no solutions'

# tests
assert parse('x**2 - 11*x + 28 = 0') == [1, -11, 28]
assert parse('3*x**2 - 11*x + 28 = 0') == [3, -11, 28]
assert parse('3*x**2 - 11*x = 0') == [3, -11, 0]
assert parse('3*x**2 + 28 = 0') == [3, 0, 28]
assert parse('-11*x + 28 = 0') == [0, -11, 28]
assert parse('28 = 0') == [0, 0, 28]

assert calc([1, -11, 28]) == [4.0, 7.0]
assert calc([1, -6, 9]) == [3.0]
assert calc([1, 1, 1]) == []
assert calc([0, 2, 4]) == [-2.0]
assert calc([2, 4, 0]) == [-2.0, 0]
assert calc([0, 0, 1]) == []
# 0 = 0 will not be considered

# exec
print(
    to_human_repr(
        calc(
            parse(
                input('Enter the equation: ')))))
