summa = int(input("Введите сумму ипотеки: "))

srok = int(input("На сколько месяцев ипотека: "))

print("Базовая ставка ипотечного кредита составляет 16%")

usl1 = input("Вы из Дальнего Востока? ")
if usl1 == "да":
    proc_summar = 0.02
else:
    usl2 = input("У вас количество детей больше 3? ")
    usl3 = input("Есть ли у вас зарплатный проект в этом банке? ")
    usl4 = input("Вам нужно страхование? ")
    if usl2 == "да":
        proc1 = 0.01
    if usl2 == "нет":
        proc1 = 0
    if usl3 == "да":
        proc2 = 0.005
    if usl3 == "нет":
        proc2 = 0
    if usl4 == "да":
        proc3 = 0.015
    if usl4 == "нет":
        proc3 = 0
    proc_summar = 0.16 - proc1 - proc2 - proc3
proc = proc_summar * 100 # процентная ставка

raschet = ((summa * proc_summar) + summa) / srok

print(f"Ваша процентная ставка: {proc} %")
print(f"Итого ежемесячный платеж составляет: {raschet} руб.")
#  для Main 2025 15.10
# изменение что ниб сделал