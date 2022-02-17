import  pandas as pd
from datetime import datetime

# Обработка csv файла при помощи pandas #
def my_pandas_csv():
   
    # Текущий месяц и день
    
    current_datetime = datetime.now()
    month = current_datetime.month
    day= current_datetime.day
        
    # Extract #
    df = pd.read_csv('3MonthPeriod.csv',sep=';')
        
    # Transform #
    cnt = df[df.columns[0]].count()
    for i in range(cnt):
        if df.iat[i,0] == month:
            if df.iat[i,1] == day:
                df.iat[i,2] = 1
    
    # Load Сохранить файл #
    df.to_csv('3MonthPeriod.csv',sep=';',encoding='utf-8',index=False) 

