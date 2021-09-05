#str_in = input()
import copy
A = 0

while True:
    A += 1

    inp = copy.deepcopy(A)
    while inp != 1:
        if inp % 2 == 0:
            inp = inp // 2
        elif inp % 2 == 1:
            inp *= 3
            inp += 1
        else:
            break    

        print("現在 ",A," ",inp)
    print("end",A,inp)