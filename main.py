num1 = 3
tries = 0
num2 = int(input("Guess a Number:\t"))

if num2 == num1:
    print("You Won!\n")
else:
    while num2 != num1:
        # if num2 == num1:
        #     print("You Won!\n")
        # else:
        num2 = int(input("Guess Again:\t"))
        tries += 1
    print(f'You Won at last!\nAfter {tries+1} tries.')