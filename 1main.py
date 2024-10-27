money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
k = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for i in range(1,10):

    if(i > 1):
        spend = spend + spend * increase
    money_capital = money_capital + salary - spend
    if (money_capital > 0):
        k+=1


print("Количество месяцев, которое можно протянуть без долгов:", k)
