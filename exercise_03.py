# Iver John R Monroy
# ITELEC2
# Laboratory #05 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():

    a = 10
    b = 5
    c = 3
    result1 = a + b * c
    print("Result of a + b * c:", result1)
    result2 = (a + b) * c
    print("Result of (a + b) * c:", result2)
    result3 = a - b
    print("Result of a - b:", result3)
    result4 = a / b
    result5 = a // b
    print("Result of a / b:", result4)
    print("Result of a // b (floor division):", result5)
    result6 = a % b
    result7 = a ** c
    print("Result of a % b (modulus):", result6)
    print("Result of a ** c (exponentiation):", result7)
    result8 = (a + b - c) * (a / b)
    print("Result of (a + b - c) * (a / b):", result8)


if __name__ == "__main__":
    main()


