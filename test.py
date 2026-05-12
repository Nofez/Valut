def currency_converter():
    print("--- Добро пожаловать в Simple Converter! ---")
    
    # Задаем фиксированный курс (в реальном мире его можно брать из API)
    usd_rate = 92.50
    eur_rate = 101.20

    try:
        rub_amount = float(input("Введите сумму в рублях: "))
        
        print(f"\nРезультат для {rub_amount} грн:")
        print(f"Доллары (USD): {round(rub_amount / usd_rate, 2)}$")
        print(f"Евро (EUR): {round(rub_amount / eur_rate, 2)}€")
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите число, используя точку для дробей.")

if __name__ == "__main__":
    currency_converter()