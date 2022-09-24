from random import randint


listOfPeople = []
endGame = 'Y'

#Generate the list of people who will be playing credit card roulette.
while endGame != 'N':
    listOfPeople.append(input('Who would you like to add to credit card roulette?\nEnter their name please.'))
    endGame = input('Would you like to add another person? (Y or N)').upper()
    
#Selects a random person from the list
print(f'Wow, it seems like {listOfPeople[randint(0, len(listOfPeople)-1)]}, will be paying the bill.')