def to_binary(n):
    return format(n & 0xFF, '08b')


def binary_subtraction(a, b):
    # Subtraction: A - B = A + (-B)
    neg_b = (~b + 1) & 0xFF
    result = (a + neg_b) & 0xFF

    # Convert unsigned result to signed decimal
    decimal_result = result if result < 128 else result - 256

    # Overflow occurs when operands added have the same sign
    # but the result has a different sign
    sign_a = (a >> 7) & 1
    sign_neg_b = (neg_b >> 7) & 1
    sign_result = (result >> 7) & 1

    overflow = (sign_a == sign_neg_b) and (sign_result != sign_a)

    print("A =", to_binary(a))
    print("B =", to_binary(b))
    print("-B =", format(neg_b, '08b'))
    print("Result (Binary) =", format(result, '08b'))
    print("Result (Decimal) =", decimal_result)
    print("Overflow =", overflow)
    print()


print("Expression 1: 45 - (+19)")
binary_subtraction(45, 19)

print("Expression 2: (-35) - (-12)")
binary_subtraction(-35, -12)