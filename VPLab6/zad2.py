import math

try:
    num = int(input())
    if num < 0:
        raise Exception()
    print(math.sqrt(num))
except Exception:
    print('Invalid Number')
finally:
    print("Goodbye")
