import pandas as pd

xlsname="/Users/munperum/PycharmProjects/training/data/friendlist.xls"

xls = pd.ExcelFile(xlsname)

trig_values = xls.parse('friends', index_col=None,na_values=['NA'])
print(trig_values)