def greatest(a, b):
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    a = 10
    b = 20

    print("First number:", a)
    print("Second number:", b)
    print("Greatest number:", greatest(a, b))