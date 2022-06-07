import random
moves = ['rock','paper','scissor']
def gen_rand():
    rand_no = random.randint(1,3)
    if rand_no == 1:
        cpu = "rock"
    elif rand_no == 2:
        cpu = "paper"
    else:
        cpu = "scissor"
    return cpu

def replay(reply):
    play_again = True
    again = True
    while again is True:
        if reply.lower() == "y":
            play_again = True
            again = False
        elif reply.lower() == "n":
            play_again =  False
            again = False
        else:
            print("Please enter a valid input")
            reply = input("Do you want to play [Y/N] : ")
            again = True
    return play_again

once_again = True
while once_again is True:
    play = True
    user = input("Enter rock paper scissor : ")
    cpu = gen_rand()
    i = 0
    count = 0
    for i in range(3) :
        if moves[i] != user.lower():
            count +=1
            once_again = True
    if count == 3:
        print("Enter a valid input")
    elif play == True:
        if user.lower() == cpu:
            print("Same result.")
            reply = input("Do you want to play [Y/N] : ")
            once_again = replay(reply)
        else:
            if user.lower() == "rock" and cpu == "paper":
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You lost.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)
                continue
            else:
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You won.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)

                continue
            if user.lower() == "paper" and cpu == "scissor":
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You lost.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)

                continue
            else:
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You won.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)

                continue
            if user.lower() == "scissor" and cpu == "rock":
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You lost.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)

                continue
            else:
                print(f"YOU : {user}")
                print(f"CPU : {cpu}")
                print("You won.")
                reply = input("Do you want to play [Y/N] : ")
                once_again = replay(reply)

                continue

print("Thank you for playing")


