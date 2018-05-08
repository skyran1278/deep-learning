import time


import matplotlib.pyplot as plt
from openpyxl import load_workbook


from get_data_by_excel import get_data_by_excel
from hw5_1_a import hw5_1_a
from hw5_1_b import hw5_1_b


# ================= initialize =============================
t = time.time()
WB = load_workbook(
    filename='pc/VE damper properties test.xlsx', read_only=True)

WS_25 = WB['0.303Hz_2.5mm']

WS_75 = WB['0.303Hz_7.5mm']


TDF_25 = get_data_by_excel(
    ws=WS_25, min_row=3, min_col=1, max_row=3747, max_col=3)

TDF_75 = get_data_by_excel(
    ws=WS_75, min_row=3, min_col=1, max_row=4817, max_col=3)


hw5_1_a(TDF_25, '2.5mm')
hw5_1_a(TDF_75, '7.5mm')

hw5_1_b(TDF_25, '2.5mm')
hw5_1_b(TDF_75, '7.5mm')

elapsed = time.time() - t
print(elapsed)

plt.show()
