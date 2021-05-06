import random
print("九九計算して")


def loop():
    i1 = random.randint(0, 9)
    i2 = random.randint(0, 9)

    m = random.randint(0, 2)

    correct = 0

    if m == 0:
        correct = i1 * i2
        print("{0} x {1}".format(i1, i2))

    if m == 1:
        correct = i1 + i2
        print("{0} + {1}".format(i1, i2))

    if m == 2:
        correct = i1 - i2
        print("{0} - {1}".format(i1, i2))

    correct_str = str(correct)
    ans_str = input().rstrip()

    correct_f = correct_str[-1]
    ans_f = ans_str[-1]

    if correct_f != ans_f:
        return

    loop()


loop()

print("おわり")
