# 💂 = '\U0001f482' angle  👹 = '\U0001f479' monter  🌊 = '\U0001f30a' water 🚢 = '\U0001f6A2' boat
# M = '\U0001f479'
# A= '\U0001f482'

import sys
import os
import time

global move
global left_side
global right_side
global water_right_boat
global water_left_boat
move = ()
left_side = []
right_side = ["\U0001f479", "\U0001f479", "\U0001f479", "\U0001f482", "\U0001f482", "\U0001f482"]
water_right_boat = ['\U0001f30a', '\U0001f30a', '\U0001f30a', '\U0001f6A2']
water_left_boat = ['\U0001f6A2', '\U0001f30a', '\U0001f30a', '\U0001f30a']

def winner(left_side, right_side):
    os.system("cls")
    print('      '.join(map(str, left_side + water_right_boat + right_side)))
    print("Congratulation you won the game....")
    main_menu()

def exit():
    os.system("cls")
    sys.exit()

def game_over():
    key = input("enter any key for continue...")
    os.system("cls")
    print("Game Over")
    time.sleep(2)
    print("1.Start Over\n2.exit")
    if input() == "1":
        start_game()
    else:
        exit()

# Function for move values form one side to another
def in_put():
    
    global move  # declare move as a global variable
    move = input("\nEnter values by comma separated to travel other side  : ").upper().split()
    for i in range(len(move)):

        #converting value form  M to 👹 = '\U0001f479' 
        if move[i] == "M":
           move[i] = '\U0001f479'

        # converting value fron A to 💂 = '\U0001f482' 
        elif move[i] == "A":
             move[i] = '\U0001f482'
    return move

def main_menu():
    print("1.Start Game \n2.exit")
    choice = input()
    if choice == "1":
        start_game()
    elif choice == "2":
        exit()

def start_game():
    left_side = []
    right_side = ["\U0001f479", "\U0001f479", "\U0001f479", "\U0001f482", "\U0001f482", "\U0001f482"]
    os.system("cls")
    print("\n", '      '.join(map(str, left_side + water_right_boat + right_side)))
    while check_condition(left_side,right_side):

        # Right to left
        move = in_put()
        if len(move) <= 2 and check_condition(left_side,right_side):
            
            # Using for loop for removing given object from right side
            for j in range(len(move)):
                right_side.remove(move[j])
                
            # Using for loop for adding given object to the left side
            for k in range(len(move)):
                left_side.append(move[k])

            os.system("cls")
            print("\n", '      '.join(map(str, left_side + water_left_boat + right_side)))

            if check_condition(left_side,right_side):
                pass

            else:
                print("\nMonsters number are greater than humans on right side....")
                game_over()

        else:
            print("Enter only two characters..")
        del move

        if left_side.count('\U0001f479') == 3 and left_side.count('\U0001f482') == 3:
            winner(left_side, right_side)

        # Left to right
        if  check_condition(left_side,right_side):
            move = in_put()
            if len(move) <= 2:

                for i in range(len(move)):  # remove from left side
                    left_side.remove(move[i])

                for l in range(len(move)):  # add to right side
                    right_side.append(move[l])
                os.system("cls")
                print("\n", '      '.join(map(str, left_side + water_right_boat + right_side)))

                if check_condition(left_side,right_side):
                    pass
                
                else:
                    print("Monsters number are greater than humans on right side....")
                    game_over()

            else:
                print("Enter only two characters..")
            del move
            if left_side.count('\U0001f479') == 3 and left_side.count('\U0001f482') == 3:
                winner(left_side, right_side)

    game_over()

# function for cheking condition are after every move
def check_condition(left_side,right_side):
    
    # 💂 = '\U0001f482' angle  👹 = '\U0001f479' monter
    
            # Checking monsters lesser than angles
    if (   right_side.count('\U0001f479') <= right_side.count('\U0001f482')

            # Cheking monster lesser than angles
        and left_side.count('\U0001f479') <= left_side.count('\U0001f482')
         
            # Handling Zero angle Error for Right Side
        or right_side.count('\U0001f482') == 0 
        
            # Handling Zero angle Error for Left Side
        or left_side.count('\U0001f482')  == 0 
        ):  
        return True
    else:
        return False



if __name__ == '__main__':
    main_menu()
