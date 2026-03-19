salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0  # начальное значение подушки
current_spend = spend  # траты текущего месяца

for month in range(1, months + 1):
    deficit = current_spend - salary  # нехватка (траты минус зарплата)
    if deficit > 0:
        money_capital += deficit  # добавляем нехватку к подушке
    current_spend *= (1 + increase)  # увеличиваем траты на следующий месяц

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
