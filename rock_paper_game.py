import random
def chose():
    a = ["r","p","s"]
    random_a = random.choice(a)
    return random_a

score = 0
count = 0
while True:
    computer_choice = chose()
    count = count+1
    # print(chose())
    user_choice = input(f"{count}.chose rock(r) paper(p) or seaser(s) or quit(q) :")
    
    # if (user_choice != "r"):
    #     raise ValueError("invalid input") 
    # isme != worl nahi kar ra ha hai
    
    if user_choice == "q":
        break
    elif count == 12:
        break
    

    elif user_choice==chose():
        print("Draw") 
        print(f"your current score = {score}")
        
        
    elif (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p"):
         print("You won  ✔️")
         score += 1
         print(f"your current score = {score}")
        
    else:
        print("you loose ❌") 
        print(f"your current score = {score}")
        
if score >= 2:
    print("hurray you won the match") 
else:
    print("ooh you loose the game ")
print(f"your total score is {score}")