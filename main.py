import random

#Variables for the Player scores
userScore = 0
botScore = 0

#Introduction message / game rules
print("[THESE ARE THE RULES]:"
+ "\n\tROCK > SCISSORS. \n\tPAPER > ROCK. \n\tSCISSORS > PAPER."
+ "\n\nWelcome to rock paper scissors. When prompted you will type (rock, paper, or scissors). Then shortly after, your opponent (a bot) will randomly choose as well. The winning rules are shown above.  "
+ "\n\n")

#Client / bot input
user = input("To begin, type your selection:")
bot = random.randint(1, 3)

    #bot selections:
    #1 = rock
    #2 = paper
    #3 = scissors

if bot == 1:
    bot = "rock"
elif bot == 2:
    bot = "paper"
elif bot == 3:
    bot = "scissors"

print("Bot selection: "+bot+"\n")

#---------------------------------------------------------------------------------------------------

#Main game

#make sure input IS rock,paper, or scissors. (input validation)
#check for ties.. if user == bot:
    #increment scores
    #give feedback : output tie (print)

if user == bot:
    userScore+=1
    botScore+=1
    print("Tie!")

#user paper
    #bot rock
        #user wins
    #otherwise
        #bot wins

elif user == "paper":
    if bot == "rock":
        userScore+=1
    else:
        botScore+=1


#user rock
    #bot paper
        #bot wins
    #otherwise
        #user wins

elif user == "rock":
    if bot == "paper":
        botScore+=1
    else:
        userScore+=1

#user scissors
    #bot rock
        #bot wins
    #otherwise
        #user wins

elif user == "scissors":
    if bot == "rock":
        botScore+=1
    else:
        userScore+=1

#display score (print)
print("\n[BotScore]: "+str(botScore)
      +"\n[UserScore]: "+str(userScore))

#TODO:
#actually print who won
#play again ? (input)