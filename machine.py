import random as rand

COLS = 3
symbol_count = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}

def spinMachine(rows, cols, symbols):
    """
    returns a nested list of unprocessed results
    """
    all_symbols = []
    
    #takes in key, value pair (symbol = "A", symbol_count = 8)
    for symbol, symbol_count in symbols.items():  #symbols.items() references both key and value
        for _ in range(symbol_count): #range() makes symbol_count iterable
            all_symbols.append(symbol) 

    
    columns = [] #this becomes columns [[column1],[column2],[column3]]
    
    for _ in range(cols):
        copy_symbols = all_symbols[:]
        column = [] #empty column list
        for _ in range(rows):
            item = rand.choice(copy_symbols) #choose a random item from copysymbols
            column.append(item) #append that item to the column list
            copy_symbols.remove(item) #remove the item from copysymbols so it wont be selected again
        
        columns.append(column) #appends the column list to columns[] 
    
    return columns

def processSpinResult(unproccesedResult): 
    """
    Since result is a nested list where each sublist is a column, it needs to be transposed

    returns a list of tuples [(A, B, C), (A, B, C), (A, B, C)] where each tuple is a row of the final result
    
    """
    transformedResult = list(zip(*unproccesedResult)) # * is the unpack operator, it separates the nested list into separate lists, then zips it eg. first element of each list becomes the part of one list, second element of each list becomes another and so on
    for row in transformedResult:
        print (*row) #prints unpacked rows so commas and parenthesis is removed

    print(list(transformedResult))
    
    return list(transformedResult)

def checkResult(transformedResult):
    """
    takes in a list of tuples, transformedResult [(a, b, c), (a,b,c), (a,b,c)]

    returns a list of string of winning symbols eg. if A and B matches thrice, it returns [A, B]
    
    """
    result = transformedResult

    winningSymbols = []

    for row in result:
        if (all(x == row[0] for x in row )):
            print(f"MATCHING {row[0]}. Congratulations!")
            winningSymbols.append(row[0])
        
    print(winningSymbols)


    return winningSymbols


def checkWinnings(winningSymbols):
    """
    accepts a list of strings that contains the symbols that matched

    returns a number 'multiplier' that will be multiplied to the bet_amount
    
    """

    valueMultiplier = {

        "A": 1.5,
        "B": 2,
        "C": 4,
        "D": 10
    }

    multiplier = 0
    if len(winningSymbols) != 0:
        for symbol in winningSymbols:
            if symbol in valueMultiplier:
                multiplier += valueMultiplier[symbol]  # Correctly access the value using the key
    print(multiplier)
    return multiplier

def play(rows, cols = COLS, symbols=symbol_count):
    """
    function in which the main.py will interact with

    accepts rows, cols, and symbols 
    rows parameter is required, cols and symbols have default values

    returns the multiplier of earnings
    """
    multiplier = checkWinnings(checkResult(processSpinResult(spinMachine(rows, cols, symbols))))

    return multiplier


                
    









            
    















     
    