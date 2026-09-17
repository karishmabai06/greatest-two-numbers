import sys

def greatest_of_three(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    # Expecting three arguments from the command line
    if len(sys.argv) != 4:
        print("Usage: python greatest_of_three.py num1 num2 num3")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        num3 = float(sys.argv[3])

        result = greatest_of_three(num1, num2, num3)
        print(f"The greatest of {num1}, {num2}, and {num3} is {result}")
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
