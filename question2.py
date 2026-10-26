def rotate_left_without_carry(binary, positions):
    print("\nRotate Left Without Carry (ROL)")
    print("Original number:", binary)

    for i in range(positions):
        first_bit = binary[0]
        binary = binary[1:] + first_bit
        print("After rotation", i + 1, ":", binary)

    print("Final result:", binary)


def rotate_left_with_carry(binary, carry, positions):
    print("\nRotate Left With Carry (RCL)")
    print("Original number:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        first_bit = binary[0]
        binary = binary[1:] + carry
        carry = first_bit

        print("After rotation", i + 1, ":", binary)
        print("Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)


number = "10110110"

rotate_left_without_carry(number, 2)

initial_carry = "0"
rotate_left_with_carry(number, initial_carry, 2)