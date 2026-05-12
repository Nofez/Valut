def currency_converter():
    # Актуальные курсы (условно)
    rates = {
        "USD": 92.50,
        "EUR": 101.20,
        "CNY": 12.80   # Добавили Юань для разнообразия
    }

    print("=== Приложение 'Супер-Обменник' ===")
    print("Доступные валюты: USD, EUR, CNY")
    print("Введите 'выход', чтобы завершить работу.")

    while True:
        print("\n" + "-"*30)
        user_input = input("Какую валюту покупаем? (или 'выход'): ").upper()

        if user_input == "ВЫХОД":
            print("До свидания! Хорошего дня.")
            break

        if user_input not in rates:
            print(f"Ошибка: Валюта '{user_input}' не поддерживается.")
            continue

        try:
            rub_amount = float(input(f"Сколько грн меняем на {user_input}? "))
            
            if rub_amount < 0:
                print("Ошибка: Сумма не может быть отрицательной!")
                continue

            # Расчет
            rate = rates[user_input]
            result = rub_amount / rate
            
            print(f"✅ Готово! Вы получаете: {result:.2f} {user_input}")
            print(f"Курс: 1 {user_input} = {rate} грн.")

        except ValueError:
            print("Ошибка: Введите корректное число (например, 500 или 150.50).")

if __name__ == "__main__":
    currency_converter()