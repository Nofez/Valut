import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        rub = float(entry_rub.get())
        currency = var.get()
        rates = {"USD": 92.50, "EUR": 101.20, "CNY": 12.80}
        
        result = rub / rates[currency]
        label_result.config(text=f"Результат: {result:.2f} {currency}", fg="#27ae60")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")

# Создаем главное окно
root = tk.Tk()
root.title("Super Converter")
root.geometry("300x400")
root.configure(bg="#f0f3f5")

# Заголовок
tk.Label(root, text="Сумма в рублях:", bg="#f0f3f5", font=("Arial", 10)).pack(pady=10)

# Поле ввода
entry_rub = tk.Entry(root, font=("Arial", 14), justify='center')
entry_rub.pack(pady=5)

# Выбор валюты (выпадающий список или радиокнопки)
var = tk.StringVar(value="USD")
tk.Label(root, text="Выберите валюту:", bg="#f0f3f5").pack(pady=10)

for curr in ["USD", "EUR", "CNY"]:
    tk.Radiobutton(root, text=curr, variable=var, value=curr, bg="#f0f3f5").pack()

# Кнопка конвертации
btn_convert = tk.Button(root, text="Конвертировать", command=convert, 
                       bg="#3498db", fg="white", font=("Arial", 12, "bold"), 
                       padx=20, pady=10, relief="flat")
btn_convert.pack(pady=20)

# Поле для результата
label_result = tk.Label(root, text="Результат: 0.00", bg="#f0f3f5", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()