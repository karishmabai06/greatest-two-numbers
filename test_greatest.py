from greatest import greatest

def test_greatest():
    assert greatest(10, 20) == 20
    assert greatest(50, 30) == 50
    assert greatest(7, 7) == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_greatest()