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
            line.append(str(numbers))
        # Add the line in the sudoku
        sorted_sudoku.append(line)
    # Return the sorted sudoku
    return sorted_sudoku

# Check if the submitted sudoku respect the rules
def solved(sudoku):
    # Create a variable for the test
    test_sudoku = []
    # Create the variable containing the sorted sudoku
    sorted_sudoku = sort_sudoku(len(sudoku))
    # Check each line of the sudoku
    for line in sudoku:
        # Sort the current line and add it to the sudoku's test variable
        test_sudoku.append(sorted(line))
    # If the new sudoku isn't the same as the sorted one
    if test_sudoku != sorted_sudoku:
        # Return false
        return False
    # If the new sudoku is the same as the sorted one
    else:
        # Return true
        return True
    
# Summarizing all the numbers missing
def missings(sudoku):
    # Create a variable containing the amount of missing numbers in each line
    lines = []
    # Check each line
    for line in sudoku :
        # Create a variable to count the missing numbers
        missing = 0 
        # Check each number :
        for number in range(len(line)):
            # Check if the number isn't in the list
            if str(number) not in line:
                # Add one to the missing numbers
                missing = missing + 1
        # Add the amount of missing numbers in the list for its respectively line
        lines.append(missing)
    # Create a variable containing the amount of missing numbers in each columns
    columns = []
    # Check each column in the sudoku
    for column in range(len(sudoku)):
        # Create an variable to stock the current column
        current_column = []
        # Check each line of the sudoku
        for line in sudoku:
            # Add the number which is the intersection of current line and current column to the column
            current_column.append(line[column])
        # Create a variable containing the amount of missing numbers
        missing = 0 
        # Check each number :
        for number in range(len(sudoku)):
            # Check if the number isn't in the list
            if str(number) not in current_column:
                # Add one to the missing numbers
                missing = missing + 1
        # Add the amount of missing numbers in the list for its respectively line
        columns.append(missing)
    # Return amount of missing numbers in lines and columns
    return lines, columns

# Try to replace the missing ones
def add_missing(list):
    # Check each number
    for i in range(len(list)):
        # If the nummber is not in the list
        if str(i) not in list:
            # Find the place of the missing number
            place = list.index('x')
            # Replace it with the right number
            list[place] = str(i)
    # Return the new list
    return list

# Get the value of the column
def get_column(column, sudoku):
    # Create a variable for the column value
    column_list = []
    # Check each line in the sudoku
    for line in sudoku:
        # Add the intersection of the line and column to the value of the column
        column_list.append(line[column])
    # Return the value of the column
    return column_list

# Replace the column with its right value
def replace_column(column, missing_column, sudoku):
    # Get the previous column
    bad_one = get_column(column, sudoku)
    # For each line in the column
    for line in range(len(bad_one)):
        # Replace the bad value with the good value in the sudoku
        sudoku[line][column] = missing_column[line]
    # Return the new value of the sudoku
    return sudoku

# Finding the good values for missing numbers
def find(lines, columns, sudoku):
    # Check if on line misses one number
    if 1 in lines:
        # Find the index of the missing one
        line = lines.index(1)
        # Replace the line with the good answer
        sudoku[line] = add_missing(sudoku[line])
    # Check if on column misses one number
    elif 1 in columns:
        # Find the index of the missing one
        column = columns.index(1)
        # Get the column's value
        column_value = get_column(column, sudoku)
        # Replace the column with the good answer
        sudoku = replace_column(column, add_missing(column_value), sudoku)
    # Return the sudoku
    return sudoku

# Open the text file and get the sudoku from it
with open("sudoku.txt", "r") as f:
    # Create a list with the sudoku in it
    sudoku = sudoku_table(f.readlines())

# Check if the suko is in the good format
if valid_content(sudoku):
    # Analysing the sudoku submitted
    print("Analysing...")
    # Create a variable containing the boolean value of sudoku if he is solved
    valid = False
    # While the sudoku isn't solve
    while valid == False:
        # Summarizing all the numbers missing
        missing_lines, missing_columns = missings(sudoku)
        # Finding the good values for missing numbers
        find(missing_lines, missing_columns, sudoku)
        # Retest the sudoku to know if he's solved
        valid = solved(sudoku)
    # Print the answer of this sudoku
    print("The answer for this sudoku is :", *sudoku, sep='\n')
else: 
    # Say that the sudoku isn't in a good format
    print("Le sudoku isn't in a good format")