__author__ = 'Jonathan'

while True:
    try:
        biggestnum = int(input("How many numbers should we count to? "))
        if biggestnum <= 0:
            raise ValueError
        break
    except ValueError:
        print("That's not a positive integer.")
    except NameError:
        print("That's not a positive integer.")



counter = 1
while counter <= biggestnum:
    if (counter % 3 == 0) and (counter % 5 == 0):
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter += 1
