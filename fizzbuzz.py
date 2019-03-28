x = 1

while x < 100:
    if x % 3 == 0 and x % 5 == 0:
        print(f"fizzbuzz ({x})")
    elif x % 3 == 0:
        print(f"fizz ({x})")
    elif x % 5 == 0:
        print(f"buzz ({x})")
    x += 1
