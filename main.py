from get_values import sudoku_table

with open("sudoku.txt", "r") as f:
    text = sudoku_table(f.readlines())

print(type(text) == 'list')

print(text)