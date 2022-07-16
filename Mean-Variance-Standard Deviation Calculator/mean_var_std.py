import numpy as np

def calculate(arr):

    # This function calculates the mean, variance, standard d., max, min and sum.

    if len(arr) != 9:
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.array(arr).reshape(3, 3)
    flattened_matrix = np.array(arr)

    list_mean = [list(np.mean(matrix, 0)), list(np.mean(matrix, 1)),
                 np.mean(flattened_matrix)]

    list_variance = [list(np.var(matrix, 0)), list(np.var(matrix, 1)),
                 np.var(flattened_matrix)]

    list_stand_d = [list(np.std(matrix, 0)), list(np.std(matrix, 1)),
                     np.std(flattened_matrix)]

    list_max = [list(np.max(matrix, 0)), list(np.max(matrix, 1)),
                     np.max(flattened_matrix)]

    list_min = [list(np.min(matrix, 0)), list(np.min(matrix, 1)),
                np.min(flattened_matrix)]

    list_sum = [list(np.sum(matrix, 0)), list(np.sum(matrix, 1)),
                np.sum(flattened_matrix)]

    calculations = {
        'mean': list_mean,
        'variance': list_variance,
        'standard deviation': list_stand_d,
        'max': list_max,
        'min': list_min,
        'sum': list_sum
    }

    return calculations
