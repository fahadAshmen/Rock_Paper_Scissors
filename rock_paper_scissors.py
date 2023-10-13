import random
from enum import IntEnum

print("Welcome to Rock Paper Scissors")
print("-------------------------------")
class user_action(IntEnum):
        ROCK = 1
        PAPER = 2
        SCISSORS =3

#action= int(input("Enter a choice(rock[1], paper[2], scissors[3]):"))

def user_option():
        options = [f"{i.name} [{i.value}]" for i in user_action]
        choices = ', '.join(options)
        selection = int(input(f"\nMake a choice :{choices} "'\n'))
        selected_choice = user_action(selection)
        return selected_choice
        #print("user==>",selected_choice)


def cpu_option():
        selection = random.randint(1, len(user_action))
        selected_choice = user_action(selection)
        return selected_choice
        #print("cpu==>",selected_choice)

victories = {
        user_action.PAPER : [user_action.ROCK, 22],
        user_action.SCISSORS : [user_action.PAPER],
        user_action.ROCK : [user_action.SCISSORS]
}


def determine_winner(user, cpu):
        # print('usr=',user)
        # print('cpu=',cpu)
        defeats = victories[user]
        if user == cpu:
                print(f"Both players selected {user.name}. Its a tie")
                return "tie"

        elif cpu in defeats:
                print(f"{user.name} beats {cpu.name}. YOU WON")
                return "player"
        else:
                print(f"{cpu.name} beats {user.name}. YOU LOSE")
                return "computer"

        # elif user == user_action.ROCK:
        #         if cpu == user_action.PAPER:
        #                 print('YOU LOSE \n PAPER COVERS ROCK')
        #         else:
        #                 print("YOU WON \n ROCK SMASHES SCISSORS")
        # elif user == user_action.PAPER:
        #         if cpu == user_action.SCISSORS:
        #                 print('YOU LOSE \n SCISSORS CUTS PAPER')
        #         else:
        #                 print('YOU WON \n PAPER COVERS ROCK')
        # elif user == user_action.SCISSORS:
        #         if cpu == user_action.PAPER:
        #                 print("YOU WON \n SCISSORS CUTS PAPER")
        #         else:
        #                 print("YOU LOSE \n ROCK SMASHES SCISSORS")


# user_option()
# cpu_option()
# determine_winner(user_action.PAPER, user_action.PAPER)
player_score =0
cpu_score=0
tie_score =0

#while (player_score != 3) or (cpu_score != 3):
                
while True:
        try:                
                user = user_option()
                
        except ValueError as e:
                range = (1, len(user_action))
                
                print(f"\n Invalid entry. select from range {range} \n")
                continue
                
        cpu = cpu_option ()
        result=determine_winner(user, cpu)
        if (result == 'player'):
                player_score +=1
        elif (result == 'computer'):
                cpu_score += 1
        else:
                tie_score += 1
        print('\n'"Your score: ", player_score, "CPU: ", cpu_score, "Ties: ", tie_score)

        if (player_score == 3) or (cpu_score == 3):
                player_score =0
                cpu_score=0
                tie_score =0
                play_again = input("Game Over....Play again? [y/n]: ").lower()
                if play_again != "y":                        
                        break




        
        
     

# print(user_action.ROCK.name)
# print(user_action.ROCK.value)
# print(user_action.ROCK == user_action(1))
# print(list(user_action))


# while True:   
#     possible_choices=["rock","paper","scissors"]
#     user_action= int(input("Enter a choice(rock[1], paper[2], scissors[3]):"))
#     cpu_action=random.choice(possible_choices)
#     print(f"\n User action is {user_action} and cpu is {cpu_action}.\n")
   

#     if user_action == cpu_action:
#         print(f"Both players selected same")
#     elif user_action == "rock":
#         if cpu_action == 'paper':
#             print('YOU LOSE \n PAPER COVERS ROCK')
#         else:
#             print("YOU WON \n ROCK SMASHES SCISSORS")
#     elif user_action == 'paper':
#         if cpu_action == 'scissors':
#             print('YOU LOSE \n SCISSORS CUTS PAPER')
#         else:
#             print('YOU WON \n PAPER COVERS ROCK')
#     elif user_action == 'scissors':
#         if cpu_action == "paper":
#             print("YOU WON \n SCISSORS CUTS PAPER")
#         else:
#             print("YOU LOSE \n ROCK SMASHES SCISSORS")
#     play_again = input("Play again? [y/n] ")
#     if play_again.lower() != 'y':
#         break
