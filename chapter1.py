import ast
from datetime import datetime

# нарощення за простими відсотковими ставками
def f1 (P, n, i):
    I = n * P * i
    S = P + I
    return f'I = n * P * i =  {I} grn \nS = P + I = {S} grn'

# методи нарахування простих відсотків
# перший метод
def f2 (P, start_date, end_date, i): 
    K = 365
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date,"%d/%m/%Y")
    delta = end_date - start_date
    t = delta.days
    S = P * (1 + t/K * i)
    return f'K = {K}, t = {t}, S = {round(S,2)} grn'


# другий метод
def f3 (P, start_date, end_date, i):
    K = 360
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date,"%d/%m/%Y")
    delta = end_date - start_date
    t = delta.days
    S = P * (1 + t/K * i)
    return f'K = {K}, t = {t}, S = {round(S,2)} grn'


# третій метод
def f4(P, start_date, end_date, i):
    K = 360
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date,"%d/%m/%Y")
    t = (30 - start_date.day) + end_date.day + (end_date.month - start_date.month - 1) * 30
    S = P * (1 + t/K * i)
    return f'K = {K}, t = {t}, S = {round(S,2)} grn'

# заміна відсоткової ставки
def convert_simple_to_exect(simple, is_leap = False):
    if is_leap:
        print(f"This year is leap. Exect = 360/366 * {simple} = {360/366 * simple}")
    else:
        print(f"This year is not leap. Exect = 360/365 * {simple} = {360/365 * simple}")
        
def convert_exect_to_simple(exect, is_leap = False):
    if is_leap:
        print(f"This year is leap. Exect = 366/360 * {exect} = {366/360 * exect}")
    else:
        print(f"This year is not leap. Exect = 365/366 * {exect} = {365/360 * exect}")

# збільшення ставки з кожним кварталом приклад 3
def f5(P, i0, step):
    res = 1
    for i in range(4):
        res += 1/4 * i0
        i0 += step
    S = res * P
    return f"Множник нарощення становить : {res}, а накопичена на рахунку за рік сума складе S = {S} грн"

# формула для капіталізації приклад 4
def f6(P, i, quartal, is_leap):
    if quartal == 1:
        if is_leap:
            S = P * (1 + 31/366 * i) * (1 + 31/366 * i)*(1 + 29/366 * i)
        else: 
            S = P * (1 + 31/365 * i) * (1 + 31/365 * i)*(1 + 28/365 * i)
    elif quartal == 2:
        if is_leap:
            S = P * (1 + 30/366 * i) * (1 + 31/366 * i)*(1 + 30/366 * i)
        else: 
            S = P * (1 + 30/365 * i) * (1 + 31/365 * i)*(1 + 30/365 * i)
    elif quartal == 3:
        if is_leap:
            S = P * (1 + 31/366 * i) * (1 + 31/366 * i)*(1 + 30/366 * i)
        else:
            S = P * (1 + 31/365 * i) * (1 + 31/365 * i)*(1 + 30/365 * i)
    elif quartal == 4:
        if is_leap:
            S = P * (1 + 31/366 * i) * (1 + 30/366 * i)*(1 + 31/366 * i)
        else: 
            S = P * (1 + 31/365 * i) * (1 + 30/365 * i)*(1 + 31/365 * i)
    return f"S = {round(S,2)} grn"

# нарахування простих відсотків на змінні в часі суми депозиту
# приклад 7

def f7(changes, i):
    changes = ast.literal_eval(changes)
    K = 365 / (i * 100)
    remainder = 0
    res = 0
    output = "Дата         Рух коштів      Залишок  Термін  Процентне число|"
    for i in range(len(changes)):
        remainder += changes[i][1]
        if i != len(changes)-1:
            delta = datetime.strptime(changes[i+1][0], "%d/%m/%Y") - datetime.strptime(changes[i][0], "%d/%m/%Y")
            t = delta.days
        else:
            delta = datetime.strptime("31/12/2021", "%d/%m/%Y") - datetime.strptime(changes[i][0], "%d/%m/%Y")
            t = delta.days
        output += f'|{changes[i][0]}     {changes[i][1]}     {remainder}      {t}        {(remainder * t) / 100000}'
        res += (remainder * t) / 100000
    
    return output + f"||Проценти за весь період нарахувань становитимуть : {res} / {round(K,2)} = {round(res/K, 2)} grn"


# нарахування відсотків у користувацькому кредиті
# приклад 6

def f8(P, n, i):
    S = P * (1 + n * i)
    R = S/(n*12)
    print(f"Величина боргу разом з наразованими відсотками S = {S}")
    print(f"Щомісячна виплата за користування кредитом становить R = {R}")

# дисконтування та облік за простими відсотковими ставками
# математичне дисконтування
def f9(S, i, quartal, is_leap):
    quartals = {
        1: 91,
        2: 91,
        3: 92,
        4: 92
    }
    n = (quartals[quartal] + 1)/366 if is_leap else quartals[quartal]/365
    P = S / (1 + n*i)
    D = S - P
    print(f"P = {P}")
    print(f"D = {D}")

# банківський облік
# приклад 8
def f10(S, n, d):
    P = S * (1-n*d)
    D = S-P
    print(f"P = {P} grn")
    print(f"D = {D} grn")


# приклад 9
def f11(S, d, t):
    K = 360
    P = S * (1 - t/360 * d)
    D = S - P
    print(f'P = {P}')
    print(f'D = {D}')

# нарощення за простими обліковими ставками
def f12(P, n, d):
    S = P / (1 - n*d)
    print(f"S = {S}")

'''
f1(5, 100000, 0.25)
print("#" * 20)
f2(100000, "20/01/2021", "05/10/2021", 0.25)
print("#" * 20)
f3(100000, "20/01/2021", "05/10/2021", 0.25)
print("#" * 20)
f4(100000, "20/01/2021", "05/10/2021", 0.25)
print("#" * 20)
f5(10000, 0.15, 0.05)
print("#" * 20)
f6(1000, 0.1, 1, True)
print("#" * 20)
data = [("05/02/2021", 120000),("10/07/2021", -40000),("20/10/2021", 80000)]
f7(data, 0.15)
print("#" * 20)
f8(100000, 3, 0.15)
print("#" * 20)
f9(100, 0.2, 1, True)
print("#" * 20)
f10(100000, 1, 0.15)
print("#" * 20)
f11(2500, 0.2, 30)
print("#" * 20)
'''