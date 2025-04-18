# Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
# scissors. For this game the user plays against the computer for a certain number of rounds.
# Your class should have fields for the how many rounds there will be, the current round number,
# and the number of wins each player has. There should be methods for getting the computer’s
# choice, finding the winner of a round, and checking to see if someone has one the (entire)
# game. You may want more methods.

import random
class Rock_paper_scissors:
    def __init__(self,rounds):
        self.rounds = rounds
    @staticmethod
    def welcome():
        print("Welcomt to Rock_Paper_Scissors ")
    def game(self):
        win =0
        lose =0

        for i in range(1,self.rounds+1):
            print("Round",i,"\n")
            userInput = input("Enter your choice: ")
            userInput.lower()
            rand = random.randint(1,3)
            if(rand == 1):
                computerChoice = "rock"
            elif(rand == 2):
                computerChoice = "scissor"
            else:
                computerChoice = "paper"
            if(userInput == "rock" and computerChoice == "rock"):
                print("Tie\n")
            elif(userInput == "rock" and computerChoice == "scissor"):
                win +=1
            elif(userInput == "rock" and computerChoice == "paper"):
                lose +=1
            elif(userInput == "paper" and computerChoice == "paper"):
                print("Tie")
            elif(userInput == "paper" and computerChoice == "rock"):
                win +=1
            elif(userInput == "paper" and computerChoice == "scissor"):
                lose +=1
            elif(userInput == "scissor" and computerChoice == "scissor"):
                print("tie")
            elif(userInput == "scissor" and computerChoice == "paper"):
                win +=1
            elif(userInput == "scissor" and computerChoice == "rock"):
                lose +=1
            print("Computer choice is ",computerChoice,"and Your choice is",userInput)
            print("\nwin:",win,"and"," lose:",lose)

                    
            
p1 = Rock_paper_scissors(3)
p1.game()    


        
        