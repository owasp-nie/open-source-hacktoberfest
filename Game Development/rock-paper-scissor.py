import random
def winner(user_ch,pc_ch):
    global user
    global pc
    if user_ch == pc_ch:
        print("it's a tie")
    elif user_ch == "rock" and pc_ch == "scissor":
        print("You win!!")
        user += 1
    elif user_ch == "paper" and pc_ch == "rock":
        print("You win!!")
        user += 1
    elif user_ch == "scissor" and pc_ch == "paper":
        print("You win!!")
        user += 1
    else:
        print("Computer wins!!")
        pc += 1

print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦ WELCOME TO ROCK, PAPER AND SCISSORS ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")        
options = ["rock","paper","scissor"]
pc = 0
user = 0
best_of = int(input("BEST OF?(Odd numbers only): "))
while(True):
    user_ch = input("Enter your choice: ").lower()
    pc_ch = random.choice(options)
    print("Computer chose",pc_ch)
    winner(user_ch,pc_ch)
    print(f"User: {user} Computer: {pc}")
    if pc > best_of//2 or user > best_of//2:
        if pc > user:
            print("Computer won the match!!!")
        else:
            print("You won the match!!!")
        break


