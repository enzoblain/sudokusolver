# Return the value without line breakers
def clear_linebreaks(text):
    # Check if the line finished with a line breaker
    if text.endswith('\n'):
            # Delete the line breaker
        text = text[:-1]
    # Return the value without line breakers
    return text

# Return a list with sudoku's value
def sudoku_table(sudoku):
    # Create a table for the sudoku
    new_sudoku = []
    # Check all the lines of the sudoku
    for i in range(len(sudoku)):
        # Create a list for the lines
        line = []
        # Delete the line breakers
        sudoku[i] = clear_linebreaks(sudoku[i])
        # Check all the caracters of each lines
        for character in sudoku[i]:
            # Check if it's a real character
            if character != " ":
                # Add the character to the list for the line
                line.append(character)
        # Add the line to the sudoku's list
        new_sudoku.append(line)
    # Return the list with sudoku's value
    return new_sudoku

# Check if the sudoku is in a valid form
def valid_content(sudoku):
    # Create a variable with the number of columns of the sudoku
    column = len(sudoku)
    # Check if line of the suoku
    for line in sudoku:
        # Check if the line has the same amount of characters than the column
        if len(line) != column:
            # Return false to stop the loop
            return False
        # Check each character of the line
        for character in line:
            # Check if the caracter is in a valid format
            if not character.isdigit() and character != "x":
                # Return false to stop the loop
                return False
    # Return true
    return True

# Create the correct sudoku respectively to his size
def sort_sudoku(number):
    # Create the variable containing the sorted sudoku 
    sorted_sudoku = []
    # Create each line of the sorted sudoku
    for i in range(number):
        # Create the variable containing the line of the sudoku
        line = []
        # Check each number 
        for numbers in range(number):
            # Add the number in the list
            line.append(numbers)
        # Add the line in the sudoku
        sorted_sudoku.append(line)
    # Return the sorted sudoku
    return sorted_sudoku

sort_sudoku(9)

# Check if the submitted sudoku respect the rules
def solved(sudoku):
    # Create the variable containing the sorted sudoku
    sorted_sudoku = sort_sudoku(len(sudoku))
    # Check each line of the sudoku
    for line in sudoku:
        # Sort the current line
        line = line.sort()
    # If the new sudoku isn't the same as the sorted one
    if sudoku != sorted_sudoku:
        # Return false
        return False
    # If the new sudoku is the same as the sorted one
    else:
        # Return true
        return True

# Open the text file and get the sudoku from it
with open("sudoku.txt", "r") as f:
    # Create a list with the sudoku in it
    sudoku = sudoku_table(f.readlines())

# Check if the suko is in the good format
if valid_content(sudoku):
    # Analysing the sudoku submitted
    print("Analysing...")
    print(solved(sudoku))
else: 
    # Say that the sudoku isn't in a good format
    print("Le sudoku isn't in a good format")