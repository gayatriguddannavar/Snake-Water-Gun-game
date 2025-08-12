import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you ):
    print("It's a draw!")

else:
    '''
    # if(computer == -1 and you == 1): (computer-you) = -2
#        print("You Win!")

#     elif (computer == -1 and you == 0): (computer-you) = -1
#         print("You Lose!")

#     elif (computer == 1 and you == -1): (computer-you) = 2
#         print("You Lose!")

#     elif (computer == 1 and you == 0): (computer-you) = 1
#         print("You Win!")

#     elif (computer == 0 and you == -1): (computer-you) = 1
#         print("You Win!")

#     elif (computer == 0 and you == 1): (computer-you) = -1
#         print("You Lose!")

  the below logic is written in the basis of the value computer - you

'''
    if((computer - you ) == -1 or (computer - you) == 2):
       print("You Lose!")
    else:
       print("You Win!")
