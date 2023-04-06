answer1 = 3
answer2 = 8
guess1 = None
guess2 = None

while answer1 != guess1 or answer2 != guess2:
    guess1 = int(input("1. please type in a number from 1 to 9："))
    guess2 = int(input("2. please type in a number from 1 to 9："))
    if answer1 == guess1 and not (answer2 == guess2):
         print("only one number correct!")
    if answer2 == guess2 and not (answer1 == guess1):
         print("only one number correct!")
    if answer1 != guess1 and answer2 != guess2:
        print("Wrong！！")   
        if answer1 > guess1:
            print("First one Bigger!")
        if answer1 < guess1:
            print("First one smaller!")
        if answer2 > guess2:
            print("Second one Bigger!")
        if answer2 < guess2:
            print("Second one smaller!")
else:
    if answer1 == guess1 and answer2 == guess2:
        print("Congratulations！！ You Got the right answer!")
