import  pandas as pd

from datetime import datetime

current_datetime = datetime.now()

month = current_datetime.month
day= current_datetime.day



# Обработка csv файла при помощи pandas #
def my_pandas_csv(month,day):
    print("Месяц", month)
    print("День",day)
    # Extract #
    df = pd.read_csv('3MonthPeriod.csv',sep=';')
    print(df)
    # Transform #
    cnt = df[df.columns[0]].count()
    #print(cnt)
    for i in range(cnt):
        if df.iat[i,0] == month:
            if df.iat[i,1] == day:
                df.iat[i,2] = 1
                row_now = i
    
    
    # Печать строки текущего дня          
    print(df.loc[row_now])
       
    # Load Сохранить файл #
    df.to_csv('3MonthPeriod.csv',sep=';',encoding='utf-8',index=False)
