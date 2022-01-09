
# Assignment: W02 Prove: Developer - Solo Code Submission
# Name: Finley Jarvis

# Program for playing tic tac toe 

# I decided to make a class so that is was easier to access variables within the functions
class Game:

    x = 1
    grid = [1,2,3,4,5,6,7,8,9]
    x_or_o = ''
    choice = 0
    win = 0
    winner = 0
    turn = 1

# Function for displaying the game board with an enhanced display that displays x's and o's 
# in different colors and highlights the winning row 
    def display():
        print()
        x = 0
        while x < 9:
            if (x+1)%3:
                if Game.win == 1:
                    if Game.grid[x] == Game.x_or_o and x in Game.winner:
                        print("\033[1;31;40m"+f"{Game.grid[x]}"+"\u001b[0m"+" | ",end="")
                    else:
                        print(Game.grid[x],"| ",end="")
                elif Game.grid[x] == 'x':
                    print("\u001b[33m"+Game.grid[x]+"\u001b[0m","| ",end="")
                elif Game.grid[x] == 'o':
                    print("\u001b[36m"+Game.grid[x]+"\u001b[0m","| ",end="")
                else: 
                    print(Game.grid[x],"| ",end="")
            else:
                if Game.win == 1:
                    if Game.grid[x] == Game.x_or_o and x in Game.winner:
                        print("\033[1;31;40m"+f"{Game.grid[x]}"+"\u001b[0m")
                    else: 
                        print(Game.grid[x])
                elif Game.grid[x] == 'x':
                    print("\u001b[33m"+Game.grid[x]+"\u001b[0m")
                elif Game.grid[x] == 'o':
                    print("\u001b[36m"+Game.grid[x]+"\u001b[0m")
                else:
                    print(Game.grid[x])
                if x < 7:
                    print("--+---+--")
            x=x+1


# Function for making sure there are no duplicate squares and the value chosen is between 1 and 9
    def check_for_error(choice):
        if choice < 1 or choice > 9:
            print("\nYou have to choose between 1 - 9, try again")
            Game.display()
            return 0
        elif Game.grid[choice - 1] == 'x' or Game.grid[choice - 1] == 'o':
            print(f"\nSquare {choice} has already been chosen \n"
                   "Please try again and choose a square that does not have an 'x' or 'o'")
            Game.display()
            return 0
        else:
            return 1

# Function for choosing which tile to play in
    def play():  
        choice = ""
        while True:
            if Game.x:
                # These two try statements are included in the small chance someone typed in 
                # a non int character. That would cause it to break if the try 
                # statemtents weren't here
                try:
                    choice = int(input("\nx's turn to choose a square (1-9): "))
                    
                except ValueError:
                    print("\nYou cannot choose a non-numerical character")
            else:
                try:
                    choice = int(input("\no's turn to choose a square (1-9): "))
                    
                except ValueError:
                    print("\nYou cannot choose a non-numerical character")

            if choice != "":
                result = Game.check_for_error(choice)
                if result == 1:
                    break

        Game.turn = Game.turn + 1
        return choice

# Function for checking if someone won
    def check_for_win():
        if Game.grid[0] == Game.grid[1] == Game.grid[2]:
            return 1, [0,1,2]
        elif Game.grid[3] == Game.grid[4] == Game.grid[5]:
            return 1, [3,4,5]
        elif Game.grid[6] == Game.grid[7] == Game.grid[8]:
            return 1, [6,7,8]
        elif Game.grid[0] == Game.grid[3] == Game.grid[6]:
            return 1, [0,3,6]
        elif Game.grid[1] == Game.grid[4] == Game.grid[7]:
            return 1, [1,4,7]
        elif Game.grid[2] == Game.grid[5] == Game.grid[8]:
            return 1, [2,5,8]
        elif Game.grid[0] == Game.grid[4] == Game.grid[8]:
            return 1, [0,4,8]
        elif Game.grid[2] == Game.grid[4] == Game.grid[6]:
            return 1, [2,4,6]
        else:
            return 0, 0



# Main function
    def main():
        
        while True:
            if Game.x:
                Game.x_or_o = "x"
            else: 
                Game.x_or_o = "o"
            Game.display()
            Game.choice = Game.play()
            Game.grid[Game.choice-1] = Game.x_or_o
            Game.x = not Game.x
            Game.win, Game.winner = Game.check_for_win()
            if Game.win:
                Game.display()
                print(f"\n{Game.x_or_o} is the winner! Thank you for playing!\n")
                break
            elif Game.turn > 9:
                Game.display()
                print("\nIt's a draw! I guess that means you both win! Congrats!"
                      "\nThanks for Playing!\n")
                break

Game.main()