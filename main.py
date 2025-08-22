import transactions as tr
import helper as h
import machine as m 

balance = 0

while True:

    
    print("Welcome! Remember to gamble responsibly\n")
    print(f"Your remaining balance: {balance}\n")

    print("To start playing, deposit to your account.\n")

    balance = tr.deposit(balance) #initial deposit

    lines = tr.getLines() #select number of lines to bet on

    bet_amount, balance = tr.bet(balance,lines) #initialize bet amount

    play = m.play(lines) #play = multiplier from play
    winnings = tr.calculateWinnings(play, bet_amount)

    if winnings != 0:
        balance = h.increaseBalance(balance, winnings)



