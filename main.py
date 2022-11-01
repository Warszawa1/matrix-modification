import numpy


def index_neighbors_fila(i, fila):
    neighbours_f = []
    neighbours_f.append(i + 1)
    neighbours_f.append(i - 1)
    neighbours_f.append(i)
    neighbours_f = list(filter((lambda x: x >= 0 and x < len(fila)), neighbours_f))
    return neighbours_f


def get_values_neighbors_fila(i, fila):
    neighbours = index_neighbors_fila(i, fila)
    result_filas = list(map((lambda x: fila[x]), neighbours))
    return result_filas


def index_neighbors_columna(columna, i, j):
    neighbours_c = []
    neighbours_c.append(i + 1)
    neighbours_c.append(i - 1)
    # neighbours_c.append(i)
    return list(filter((lambda x: x >= 0 and x < len(columna)), neighbours_c))


def get_values_neighbors_columna(columna, i, j):
    neighbours = index_neighbors_columna(columna, i, j)
    return list(map((lambda x: columna[x][j]), neighbours))


def get_all_neighbors_values(matrix, i, j):
    if len(matrix) == 1: 
        return get_values_neighbors_fila(j, matrix[i])
    elif len(matrix[0]) == 1: 
        return get_values_neighbors_columna(matrix, i, j)
    else: 
        return get_values_neighbors_fila(j, matrix[i]) + get_values_neighbors_columna(matrix, i, j)


def numpy_average(matrix, i, j):
    neighbours = get_all_neighbors_values(matrix, i, j)
    return numpy.average(neighbours)


def process_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(numpy_average(matrix, i, j))
            result[i][j] = round(result[i][j], 2)
    return result   









