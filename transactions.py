import helper as h
MAX_AMOUNT = 3


def deposit(balance):
    """
    Takes in amount of deposit from user input

    returns balance
    
    """
    while True:
        deposit_amount = input("How much would you like to deposit? $")
        
        try:
            deposit_amount = int(deposit_amount)
            if deposit_amount <= 0:
                print("Deposit amount should be greater than 0.")
            else:
                print(f"Your deposit of {deposit_amount} is successful.\n")
                balance = h.increaseBalance(balance, deposit_amount)
                
                return balance
        
        except ValueError:
            print("Invalid amount. Please try again.")


def bet(balance, lines):
    """
    takes in user input bet_amount, lines, and balance
    bet_amount is multiplied by lines
    bet_amount should be greater than balance

    returns bet_amount and balance

    """
    while True:
        bet_amount = input("How much would you like to bet? $")
        print(f"Remaining balance: ${balance}")
        
        try:
            bet_amount = int(bet_amount)
            bet_amount *= lines
            if bet_amount > balance:
                print("You don't have enough balance to make this bet.")
            else:
                print(f"Your bet of ${bet_amount} has been placed.\n")
                balance = h.decreaseBalance(balance, bet_amount)
                return bet_amount, balance
            
        except ValueError:
            print("Invalid amount. Please try again.")

def getLines():
    """
    takes in how many lines the user wants to bet on

    returns a number - the amount of bet from the user
    """

    while True:
        lines = input("How many lines would you like to bet on? [1 - " + str(MAX_AMOUNT) + "] ")

        try:
            lines = int(lines)
            if (lines < 1) or (lines > MAX_AMOUNT):
                print("Choose [1 - " + str(MAX_AMOUNT) + "]")
            
            else:
                print(f"Number of lines selected: {lines} \n")
                return lines
                
        except ValueError:
            print("Invalid input. Please try again.")

def calculateWinnings(multiplier, bet_amount):
    """
    calculates total winnnings
    if no winnings, returns 0

    takes in multiplier and bet_amount

    returns the product of multiplier and bet_amount
    """
    if (multiplier == 0):
        print("Better luck next time!")

    winnings = multiplier*bet_amount
    return winnings




    


        













