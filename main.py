import random
# guessing Game 
# RPS 
# Dice Roll 
# Fortune teller

def guessingGame(): 
	print("This is the guessing game")

def RPS(): 
	#print("This is rock paper scissors")
	
	# cpu and player 
	# cpu chooses a random number between 1-3 
	# get player choice 
	print("1. Rock")
	print("2. Paper")
	print("3. Scissors")
	cpu = random.randint(1,3)
	user = int(input("Please choose your weapon: "))
	# use nested conditionals 
	if(cpu == user): 
		print("Tie game")
	elif(cpu == 1): 
		if(user == 2): 
			print("You won! I chose Rock")
		elif(user == 3): 
			print("You lose! I chose Rock")
	elif(cpu == 2): 
		if(user == 1): 
			print("You lose! I chose Paper")
		elif(user == 3): 
			print("You won! I chose Paper")
	elif(cpu == 3): 
		if(user == 1): 
			print("You won! I chose Scissors")
		elif(user == 2): 
			print("You lose! I chose Scissors")


def diceRoll(): 
	#print("This is the dice roll")
	print(random.randint(1,6))

def fortuneTeller(): 
	#print("this is the fortune teller")
	#using a list, add 5 fortunes and randomly choose one to output to the user
	fortuneList = ["You're having a great hair day!", "Yikes, my forecast says to stay inside for the next month", "Today's the day to try something new!", "Treat yourself today!", "You're looking quite ugly today. It's best to stay inside as to not scare others"]

	print(fortuneList[random.randint(0,len(fortuneList)-1)]) 

# 'main' function 
# this is where we define how we want our program to run

def main(): 
	#print("This is the main function")

	# Tell the user their game options 
	# Ask the user to choose one
	# Call the correct function based on user input
	print("1. Guessing Game")
	print("2. Rock Paper Scissors")
	print("3. Dice Roll")
	print("4. Fortune Teller")
	userInput = input("Which game would you like to play? Please specify with a number: ")
	# 1 != "1"

	if(userInput == "1"): 
		guessingGame()
	elif(userInput == "2"): 
		RPS() 
	elif(userInput == "3"): 
		diceRoll() 
	elif(userInput == "4"): 
		fortuneTeller() 
	else: # catch exceptions 
		print("Sorry that was an invalid input")
		main()

# This controls the execution of our code
if __name__ == "__main__": 
	main()