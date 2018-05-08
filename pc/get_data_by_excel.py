import numpy as np


def get_data_by_excel(ws, min_row, min_col, max_row, max_col):
    data = np.array([])
    for row in ws.iter_rows(min_row=min_row, min_col=min_col, max_row=max_row, max_col=max_col):
        for cell in row:
            data = np.append(data, [cell.value])
    return np.reshape(data, (max_row - min_row + 1, max_col - min_col + 1))
