class Prime:
    def __init__(self):
        self.number = 0

    def main(self):

        while True:

            flag = False

            for n in range(2, self.number - 1):

                if self.number % n == 0:
                    flag = True

            if flag == False:

                print(self.number)

            # print(self.number)
            # return

            self.number += 1


prime = Prime()
prime.main()
