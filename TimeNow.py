print ("Изменение поля Количество выполнений для текущей даты")
print("")
import  pandas as pd

from datetime import datetime

# Текущий месяц и день
current_datetime = datetime.now()
month = current_datetime.month
day = current_datetime.day
# Столбец 2 - энергетическое ; Столбец 3 - энергетика стихии огня 
column = 3


# Обработка csv файла при помощи pandas #
def my_pandas_csv(month,day,column):
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
                df.iat[i,column] = 1
                row_now = i
    
    
    # Печать строки текущего дня          
    print(df.loc[row_now])
       
    # Load Сохранить файл #
    df.to_csv('3MonthPeriod.csv',sep=';',encoding='utf-8',index=False)

# Точка входа в программу
def main():
    #my_text()
      
    my_pandas_csv(month,day,column)
    return 0
if __name__ == '__main__':
    main()
