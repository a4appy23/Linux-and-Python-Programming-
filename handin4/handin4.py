#1. Create a function called read_data, that takes a filename as argument. The function should open the file, and read its contents into a list of list of floats, where the outer list corresponds to the lines of the file, and the inner lists correspond to the columns (that is, convert the strings of each line to a list of two numeric values, and append them to an outer list). The function should return this list. Test the function by calling it on the experimental_results.txt file like this:
def read_data(filename):
    """function called read_data"""
    result_list = []
    mid_list = []
    with open(filename) as input:
        for line in input:
            for number in line.split():
                mid_list.append(float(number))
                if len(mid_list) == 2:
                    result_list.append(mid_list)
                    mid_list=[]

    return(result_list)


list_of_rows = read_data('experimental_results.txt')
print(list_of_rows)

#2. Write a function called calc_averages that takes a list of list of floats as input, and calculates the average value for each column by iterating over the rows. The function should return these two values. Test the function by calling it like this:
def calc_averages(floatfile):
    """calc_averages that takes a list of list of floats"""
    n_lines = len(floatfile)
    col1 = 0
    col2 = 0
    for line in list_of_rows:
        col1 = col1 + line[0]
        col2 = col2 + line[1]
    return(col1/n_lines, col2/n_lines)

col1_avg, col2_avg = calc_averages(list_of_rows)
print(col1_avg, col2_avg)
    
#3. Write a function called transpose_data that turns the list of lists around so that it becomes a list of columns, rather than a list of rows. This means that the outer list now has two elements each containing a list of all the values in the corresponding column. In other words, if I want to access the 26th value in the 2nd column, I would now index with [1][25] instead of [25][1].
def transpose_data(floatfile):
    """transpose_data"""
    col = [[], []]
    for line in floatfile:
        col[0].append(line[0])
        col[1].append(line[1])
    return(col)

list_of_columns = transpose_data(list_of_rows)
print(list_of_columns)

