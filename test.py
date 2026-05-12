import tkinter as tk
from tkinter import messagebox

class UniversalConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Currency Pro")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")

        # База курсов относительно 1 USD
        self.rates = {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.79,
            "CNY": 7.23,
            "JPY": 151.50
        }

        self.setup_ui()

    def setup_ui(self):
        # Заголовок
        tk.Label(self.root, text="Global Currency Converter", fg="white", bg="#2c3e50", 
                 font=("Arial", 16, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(padx=20)

        # Левая часть: Ввод и выбор
        input_frame = tk.Frame(main_frame, bg="#2c3e50")
        input_frame.grid(row=0, column=0, padx=10)

        tk.Label(input_frame, text="Сумма:", fg="#ecf0f1", bg="#2c3e50").pack()
        self.entry_amount = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.entry_amount.pack(pady=5)

        tk.Label(input_frame, text="Из:", fg="#ecf0f1", bg="#2c3e50").pack()
        self.from_var = tk.StringVar(value="EUR")
        self.from_menu = tk.OptionMenu(input_frame, self.from_var, *self.rates.keys())
        self.from_menu.pack(pady=5)

        tk.Label(input_frame, text="В:", fg="#ecf0f1", bg="#2c3e50").pack()
        self.to_var = tk.StringVar(value="USD")
        self.to_menu = tk.OptionMenu(input_frame, self.to_var, *self.rates.keys())
        self.to_menu.pack(pady=5)

        # Правая часть: История
        tk.Label(main_frame, text="История:", fg="#ecf0f1", bg="#2c3e50").grid(row=0, column=1)
        self.history_list = tk.Text(main_frame, width=25, height=10, font=("Consolas", 9))
        self.history_list.grid(row=1, column=1, padx=10)

        # Кнопка
        self.btn_calc = tk.Button(input_frame, text="Посчитать", command=self.calculate,
                                  bg="#e67e22", fg="white", relief="flat", width=15)
        self.btn_calc.pack(pady=20)

    def calculate(self):
        try:
            amount = float(self.entry_amount.get())
            from_curr = self.from_var.get()
            to_curr = self.to_var.get()

            # Логика: переводим в USD, затем из USD в целевую валюту
            # Формула: (Сумма / Курс_исходной) * Курс_целевой
            result = (amount / self.rates[from_curr]) * self.rates[to_curr]

            res_str = f"{amount} {from_curr} = {result:.2f} {to_curr}"
            
            # Обновляем историю
            self.history_list.insert(tk.END, res_str + "\n")
            self.history_list.see(tk.END) # Прокрутка вниз
            
            self.entry_amount.delete(0, tk.END) # Очистка поля
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числовое значение")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalConverter(root)
    root.mainloop()