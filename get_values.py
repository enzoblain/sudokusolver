def sudoku_table(file):
    new_file = []
    for i in range (len(file)):
        line = []
        if file[i].endswith('\n'):
            file[i] = file[i][:-1]
        for j in file[i]:
            print(j, j != " ")
            if j != " ":
                line.append(j)
        new_file.append(line)
    return new_file