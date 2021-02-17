import random
print("九九計算して")


def loop():
    i1 = random.randint(0, 9)
    i2 = random.randint(0, 9)
    correct = i1 * i2

    print("{0} x {1}".format(i1, i2))

    ans = int(input().rstrip())

    if correct != ans:
        return

    loop()


loop()

print("おわり")
