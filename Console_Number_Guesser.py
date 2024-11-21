#Number guesser

import random
import sys
import time

numList = []
adder = 20

try:
    number = int(input(f"Enter a number between 1-{adder}: "))
except ValueError:
    print("Please choose a number")
    sys.exit()

for x in range(adder):
    numList.append(adder)
    adder = adder - 1

if number in numList:
    pass
else:
    print("Please choose number in that range")
    sys.exit()

x = ""

number_list = []
number_list2 = []

while True:

    if x == number:
        break
    a = random.randint(1, 20)
    print(number_list)
    if a in number_list:
        print("*****in list*****")
        pass
    else:
        number_list.append(a)
        print("I guess your number is {}".format(a))
        time.sleep(2)
        if a == number:
            print("I found it")
            break
        elif number - 4 < a < number + 4:
            print("Am I getting closer")
            number_list2.append(a)
            time.sleep(2)
            while True:
                if number >= 16:
                    x = random.randint(16, 20)
                    print(number_list2)
                    if x in number_list2:
                        print("*****in list*****")
                        time.sleep(2)
                        pass
                    else:
                        print("I guess your number is {}".format(x))
                        time.sleep(2)
                        number_list2.append(x)
                        if x == number:
                            print("I found it")
                            break
                        else:
                            print("Isn' it, I will find")
                            time.sleep(3)
                            pass
                elif number <= 4:
                    x = random.randint(1, number + 4)
                    print(number_list2)
                    if x in number_list2:
                        print("*****in list*****")
                        time.sleep(2)
                        pass
                    else:
                        print("I guess your number is {}".format(x))
                        time.sleep(2)
                        number_list2.append(x)
                        if x == number:
                            print("I found it")
                            break
                        else:
                            print("Isn' it, I will find")
                            time.sleep(3)
                            pass
                else:
                    x = random.randint(number - 4, number + 4)
                    print(number_list2)
                    if x in number_list2:
                        print("*****in list*****")
                        time.sleep(2)
                        pass
                    else:
                        print("I guess your number is {}".format(x))
                        time.sleep(2)
                        number_list2.append(x)
                        if x == number:
                            print("I found it")
                            break
                        else:
                            print("Isn' it, I will find")
                            time.sleep(3)
                            pass

        else:
            print("Isn' it, I will find")
            time.sleep(3)
            pass
