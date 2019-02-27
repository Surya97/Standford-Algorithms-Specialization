# Karatsuba Multiplication Algorithm

# x = 10**(n/2) * a + b
# y =  10**(n/2) * c + d, where n is the number of digits in the given number
# and a, b, c, d are (n/2)-digit numbers
#
# Step-1: Compute recursively a*c
# Step-2: Compute recursively b*d
# Step-3: Compute recursively (a+b)*(c+d) = a*c + a*d + b*c + b*d
# (a+b)*(c+d) - a*c - b*d = (a*d + b*c)
#
# result is 10**n * (a*c) + 10**(n/2) * (a*d + b*c) + (b*d)


from itertools import zip_longest


def add(x, y):
    res, carry = [], 0
    for a, b in zip_longest(x, y, fillvalue=0):
        temp = a + b + carry
        carry = temp // 10
        res.append(temp % 10)
    if carry:
        res.append(carry)

    return res


def subtract(x, y):
    res, carry = [], 0
    for a, b in zip_longest(x, y, fillvalue=0):
        temp = a - b + carry
        carry = temp // 10
        res.append(temp % 10)

    return res


def karatsuba(x, y):
    while len(x) < len(y):
        x.append(0)
    while len(y) < len(x):
        y.append(0)

    l1 = len(x)
    l1_2 = (l1+1) >> 1

    if l1 == 1:
        return add([x[0] * y[0]], [])

    a = x[:l1_2]
    b = x[l1_2:]
    c = y[:l1_2]
    d = y[l1_2:]

    a_c = karatsuba(a, c)
    b_d = karatsuba(b, d)
    a_d_b_c = karatsuba(add(a, b), add(c, d))
    a_d_b_c = subtract(subtract(a_d_b_c, a_c), b_d)

    res = add(a_c,  [0]*(l1_2 << 1) + b_d)
    res = add(res, [0]*l1_2 + a_d_b_c)

    return res


t1 = list(map(int, reversed("3141592653589793238462643383279502884197169399375105820974944592")))
t2 = list(map(int, reversed("2718281828459045235360287471352662497757247093699959574966967627")))

print(''.join(map(str, reversed(karatsuba(t1, t2)))))
