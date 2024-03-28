def sudoku_table(file):
    new_file = []
    for i in range(len(file)):
        line = []
        if file[i].endswith('\n'):
            file[i] = file[i][:-1]
        for j in file[i]:
            if j != " ":
                line.append(j)
        new_file.append(line)
    return new_file

def check_true(sudoku):
    column =  len(sudoku)
    for i in sudoku:
        if len(i) != column:
            return False
        for j in i:
            if not j.isdigit() and j != "x":
                return False
    return True