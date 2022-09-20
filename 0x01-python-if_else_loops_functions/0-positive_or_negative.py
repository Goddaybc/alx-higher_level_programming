#!usr/bin/python3
import random
number = random.randint(-10, 10)
if random > 0:
    print("{} is positive".format(number))
elif random == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
