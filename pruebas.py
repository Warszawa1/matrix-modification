import numpy
import pandas

from main import process_matrix

matrix = []

rows_num = int(input('\nCuantas filas quieres que tenga la matriz? '))
columns_num = int(input('\nCuantas columnas quieres que tenga la matriz? '))

# print matrix with the rows and columns numbers, having the positions inside
# the matrix as a reference
def print_matrix(rows_num, columns_num):
    print(f'\nESTAS SON LAS POSICIONES DE LA MATRIZ:\n')
    for row in range(rows_num):
        for column in range(columns_num):
            print(f'[{row}][{column}]', end=' ')
        print('\n')

print_matrix(rows_num, columns_num)

# ask if the user wants to generate a random matrix with the rows_num and columns-num
# or if he wants to input the numbers himself
def generate_matrix():
    generate = input('\nQuieres generar una matriz aleatoria? (s/n) ')
    if generate == 's':
        for row in range(rows_num):
            matrix.append([])
            for column in range(columns_num):
                matrix[row].append(numpy.random.randint(1, 10))
    elif generate == 'n':
        for row in range(rows_num):
            matrix.append([])
            for column in range(columns_num):
                matrix[row].append(int(input(f'\nIntroduce el numero de la posicion [{row}][{column}]: ')))
    else:
        print('\nLa opcion introducida no es valida')
        generate_matrix()
    return matrix

print(generate_matrix())


print('')

original_matrix = pandas.DataFrame(matrix,
        index=[f'| row{row} |' for row in range(rows_num)], columns=[f'|_col{row}_|' for row in range(columns_num)])

processed_matrix = (process_matrix(matrix))
processed_matrix = pandas.DataFrame(processed_matrix, index=[f'| row{row} |' for row in range(rows_num)], columns=[f'|_col{row}_|' for row in range(columns_num)])

print(f'\nORIGINAL MATRIX:\n{original_matrix}')
print(f'\nPROCESSED MATRIX:\n{processed_matrix}\n')






# matrix2 = [[1],
#           [4], 
#           [7]]
# print(f'\nOrigin Matrix:{matrix2}')
# print(f'Expected:     [[2.5], [4.0], [5.5]')
# print(f'solo columnas:{process_matrix(matrix2)}\n')


# matrix3 = [[1, 2, 3]]
# print(f'\nOrigin Matrix:{matrix3}')
# print(f'Expected:  [[1.5, 2.0, 2.5]')
# print(f'solo filas:{process_matrix(matrix3)}\n')

# m11 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f'\nOrigin Matrix:{m11}')
# print(f'Expected:[[2.33, 2.75, 3.66], [4.25, 5, 6],[6.33, 7.25, 7.66]')
# print(f'matriz 3: {process_matrix(m11)}\n')

# m1 = [[3, 0], [0, 3]]
# print(f'\nOrigin Matrix:{m1}')
# print(f'matriz2 : {process_matrix(m1)}\n')

# m2 = [[1, 4],
#      [-3, -9], 
#      [0, -13]]
# print(f'\nOrigin Matrix:{m2}')
# print(f'Expected: [[1, 2], [2, 1], [,]]')
# print(f'negativos{process_matrix(m2)}')

# zeroes = [[0, 0, 0], 
#          [0, 0, 0]]
# print(f'\nOrigin Matrix:{zeroes}')
# print(f'zeroes{process_matrix(zeroes)}')

# one_row_matrix = [[1, 3, 6, 9, 12]]
# print(f'\nOrigin Matrix:{one_row_matrix}')
# print(f'Expected: [[2, 3.33, 6.0, 9.0, 10.5]]')
# print(f'one_row{process_matrix(one_row_matrix)}')

# one_column_matrix = [[1], 
#                     [-1], 
#                     [10]]
# print(f'\none column{process_matrix(one_column_matrix)}')

# one_number = [[4]]
# print(f'\none number{process_matrix(one_number)}')

# empty = [[]]
# print(f'\nempty{process_matrix(empty)}\n')









# import numpy

# lista = [ 5, 9, 3, 4]

# def process_list(lista):
#     new_list = []
#     for row in range(len(lista)):
#         new_list.append(neighbors_index(lista, row))
#     return new_list

# # find the neighbors value with a filter function
# def neighbors_index(lista, row):
#     if row == 0:
#         neighbours = filter(lambda x: x != row, [row+1])
#     elif row == len(lista) - 1:
#         neighbours = filter(lambda x: x != row, [row-1])
#     else:
#         neighbours = filter(lambda x: x != row, [row+1, row-1])
#     neighbours = list(neighbours)
#     neighbours.append(lista[row])
#     return neighbours

# print(process_list(lista))
# lista = [ 5, 9, 3, 4]



# import numpy

# def get_neighbours_indexes(index, elements):
#     indices = []
#     indices.append(index + 1)
#     indices.append(index - 1)
#     indices.append(index)
#     return list(filter(lambda x: x >= 0 and x < len(elements), indices))


# def average(index, elements):
#     return list(map(lambda x: elements[x], get_neighbours_indexes(index, elements)))



# def get_neighbours_values(index, elements):
#     return list(map(lambda x: elements[x], get_neighbours_indexes(index, elements)))

# print(get_neighbours_values(0, lista))

# def get_average(elements):
#     return round(numpy.mean(elements), 2)

# print(get_average(get_neighbours_values(0, lista)))

