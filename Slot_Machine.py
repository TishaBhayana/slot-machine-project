import random  # Importing the random module to generate random numbers

# Global constants to make the program dynamic
MAX_LINES = 3  # Maximum number of lines the player can bet on
MAX_BET = 100  # Maximum amount of money the player can bet on each line
MIN_BET = 1    # Minimum amount of money the player can bet on each line

# Slot machine dimensions
ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary to define how many of each symbol are available in the slot machine
symbol_count = {
    "👑": 2,  # Crown symbol appears 2 times
    "💃": 4,  # Dancing woman symbol appears 4 times
    "🍀": 6,  # Lucky clover symbol appears 6 times
    "🕺": 8   # Dancing man symbol appears 8 times
}

# Dictionary to define the value of each symbol
symbol_value = {
    "👑": 5,  # Crown symbol is worth 5 points
    "💃": 4,  # Dancing woman symbol is worth 4 points
    "🍀": 3,  # Lucky clover symbol is worth 3 points
    "🕺": 2   # Dancing man symbol is worth 2 points
}

# Function to check if the player won any money
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize the total winnings to 0
    winning_lines = []  # List to keep track of winning lines
    for line in range(lines):  # Check each line
        symbol = columns[0][line]  # Get the symbol in the current line from the first column
        for column in columns:  # Check each column
            symbol_to_check = column[line]  # Get the symbol in the current line from the column
            if symbol != symbol_to_check:  # If the symbols don't match
                break  # Stop checking this line
        else:  # If all symbols match
            winnings += values[symbol] * bet  # Calculate the winnings
            winning_lines.append(line + 1)  # Add the line number to the winning lines list

    return winnings, winning_lines  # Return the total winnings and the winning lines

# Function to generate a random outcome for the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List to hold all symbols according to their counts
    for symbol, count in symbols.items():  # Go through each symbol and its count
        for _ in range(count):  # Add the symbol to the list 'count' times
            all_symbols.append(symbol)

    columns = []  # List to hold each column of the slot machine
    for _ in range(cols):  # Create each column
        column = []  # Initialize a new column
        current_symbols = all_symbols[:]  # Copy the list of symbols for this column
        for _ in range(rows):  # Fill the column with symbols
            value = random.choice(current_symbols)  # Pick a random symbol
            current_symbols.remove(value)  # Remove the chosen symbol to avoid duplication
            column.append(value)  # Add the symbol to the column

        columns.append(column)  # Add the column to the list of columns

    return columns  # Return the list of columns representing the slot machine spin

# Function to print the slot machine outcome in a readable format
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Print each row
        for i, column in enumerate(columns):  # Go through each column
            if i != len(columns) - 1:  # If it's not the last column
                print(column[row], end=" | ")  # Print the symbol followed by a separator
            else:
                print(column[row], end="")  # Print the last symbol without a separator

        print()  # Move to the next line after printing the row

# Function to get the deposit amount from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")  # Ask the user to enter a deposit amount
        if amount.isdigit():  # Check if the input is a number
            amount = int(amount)  # Convert the input to an integer
            if amount > 0:  # Check if the amount is positive
                break  # Exit the loop if the amount is valid
            else:
                print("Amount must be greater than 0.")  # Prompt the user to enter a positive amount
        else:
            print("Please enter a number.")  # Prompt the user to enter a valid number

    return amount  # Return the deposit amount

# Function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # Ask the user for the number of lines
        if lines.isdigit():  # Check if the input is a number
            lines = int(lines)  # Convert the input to an integer
            if 1 <= lines <= MAX_LINES:  # Check if the number of lines is within the allowed range
                break  # Exit the loop if the number of lines is valid
            else:
                print("Enter a valid number of lines.")  # Prompt the user to enter a valid number of lines
        else:
            print("Please enter a number.")  # Prompt the user to enter a valid number

    return lines  # Return the number of lines

# Function to get the bet amount for each line from the user
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")  # Ask the user for the bet amount per line
        if amount.isdigit():  # Check if the input is a number
            amount = int(amount)  # Convert the input to an integer
            if MIN_BET <= amount <= MAX_BET:  # Check if the bet amount is within the allowed range
                break  # Exit the loop if the bet amount is valid
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")  # Prompt the user to enter a valid bet amount
        else:
            print("Please enter a number.")  # Prompt the user to enter a valid number

    return amount  # Return the bet amount

# Function to handle a single spin of the slot machine
def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines to bet on
    while True:
        bet = get_bet()  # Get the bet amount per line
        total_bet = bet * lines  # Calculate the total bet

        if total_bet > balance:  # Check if the user has enough money
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")  # Prompt the user about insufficient balance
        else:
            break  # Exit the loop if the balance is sufficient

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")  # Display the betting details

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Generate the outcome of the slot machine
    print_slot_machine(slots)  # Print the slot machine outcome
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check if the user won
    print(f"You won ${winnings}.")  # Display the winnings
    if winning_lines:  # If there are winning lines
        print(f"You won on lines:", *winning_lines)  # Display the winning lines
    else:
        print("You won on the lines: 0")  # If no lines won

    return winnings - total_bet  # Return the net result (winnings - total bet)

# Main function to run the slot machine game
def main():
    balance = deposit()  # Get the initial deposit
    while True:
        print(f"Current balance is ${balance}")  # Display the current balance
        answer = input("Press enter to play (q to quit).")  # Ask the user if they want to play or quit
        if answer == "q":  # If the user wants to quit
            break  # Exit the loop
        balance += spin(balance)  # Run a spin and update the balance

    print(f"You left with ${balance}")  # Display the final balance when the user quits

# Run the main function to start the game
main()
