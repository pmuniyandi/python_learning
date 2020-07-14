import pandas as pd
from pandas import ExcelWriter

xmlname="/Users/munperum/PycharmProjects/training/data/friendlist.xls"

df = pd.DataFrame({'Name': ["Muni", "Kaali", "Rajesh", "Arul", "Raja"],
                   'Age': [35, 36, 36, 28, 41]})

writer = ExcelWriter(xmlname)

df.to_excel(writer, 'friends', index=False)

writer.save()
