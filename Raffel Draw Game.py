# ---------------------------------Python Coding Style-----------------------------------------------------------
print("This program use indent formatting to create a function")
def open():
    print("Welcome to Lustre Technologies")
    print("Let's know how we can help you\n")
    return ()


open()
#----------------------------------------------------Raffel Draw Game----------------------------------------------------------------------------------------------------------
print("This is a raffel draw game that allows gamer to input fruit names thrice using the concept of \'string slicing\' , \'if function\', \'defined function\',  \'iteration\', and \'while loop\'.")
y = ['Orange', 'Pineapple', 'Mango', 'Apple', 'Watermelon']
def lose():
    return "You have lost 5 points which cost $20 each"
class Game:

    def mainb(self):
        x = input("Enter any name of fruit that you know: ")
        if x == y[3]:
            print("You have won $100")
        elif x == y[2]:
            print("You have won $1000")
        else:
            print(lose())

    def start_game(self):
        i = 0
        while i < 3:
            self.mainb()
            i += 1
# Create an instance of the game and start it
game_instance = Game()
game_instance.start_game()
print("Visit the nearest bank to claim your total money")