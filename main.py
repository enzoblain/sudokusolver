from sudoku_table import sudoku_table, valid_content, solved

with open("sudoku.txt", "r") as f:
    sudoku = sudoku_table(f.readlines())

if valid_content(sudoku):
    print("Analyse...")
    print(solved(sudoku))
else: 
    print("Le sudoku ne respecte pas les règles")