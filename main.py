from sudoku_table import sudoku_table, check_true

with open("sudoku.txt", "r") as f:
    text = sudoku_table(f.readlines())

if check_true(text):
    print("Analyse...")
else: 
    print("Le sudoku ne respecte pas les règles")