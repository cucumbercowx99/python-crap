selection = int(input("What operation would you like to carry out? 1: Add  2: Subtract  3: Multiply  4: Divide "))
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

answer1 = first_number+second_number
answer2 = first_number-second_number
answer3 = first_number*second_number
answer4 = first_number/second_number

if selection == 1:
    print(answer1)

if selection == 2:
    print(answer2)

if selection == 3:
    print(answer3)

if selection == 4:
    print(answer4)