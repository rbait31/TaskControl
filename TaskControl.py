# 5.2 Построение графиков в Python

import tkinter as tk
from datetime import datetime
import  pandas as pd

# Импорт внешних файлов
import TaskDone
#import chart2

# Функция закрытия окна
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("500x500")
window.title("Ежедневные задания")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Ежедневные задания", font = ('Helvetica', 16, 'bold'), fg = '#3333FF')
lblTitle.place(x=120, y=32)

# Добавление метки подзаголовка
lblTitle = tk.Label(text = "Отметка о выполнении", font = ('Helvetica', 12, 'bold'), fg = '#3333FF')
lblTitle.place(x=140, y=67)

# Добавление кнопки и метки для задания 1
btnChart1 = tk.Button(window, text="Выполнил", font = ('Helvetica', 10, 'bold'), command=TaskDone.my_pandas_csv(2))

btnChart1.place(x=35, y=122, width=90, height=30)

lblChart1 = tk.Label(text="Наполнение цветными энергиями", font = ('Helvetica', 10))
lblChart1.place(x=153, y=127)

# Добавление кнопки и метки для задания 2
btnChart2 = tk.Button(window, text="Выполнил", font = ('Helvetica', 10, 'bold'), command=TaskDone.my_pandas_csv(3))

btnChart2.place(x=35, y=186, width=90, height=30)

lblChart1 = tk.Label(text="Соединение с энергией стихии огня ", font = ('Helvetica', 10))
lblChart1.place(x=153, y=191)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=380, y=440, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
 
