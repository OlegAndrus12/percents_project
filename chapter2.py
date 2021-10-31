from datetime import datetime

# нарощення та дисконтування за складними відсотковими ставками
# 2.1 нарощення за складними відсотковими ставками
# приклад 10
def f13(P, n, i):
    S = P * pow(1 + i, n)
    I = S - P
    output = f"S = {round(S,2)} грн |I = S - P = {round(S,2)} - {round(P,2)} = {round(I,2)} грн"
    return output

#приклад 11
def f14(P, i, i1, i2, n1, n2):
    S = P * pow(1 + i + i1, n1) * pow(1 + i + i2, n2)
    return f"S = {round(S,2)}"

# приклад 12
def f15(P, i, years, days):
    K = 365
    n = ((years * K) + days) / K    
    S1 = P * pow((1 + i), int(n)) * (1 + (n - int(n)) * i)
    S2 = P * pow(1 + 0.25, n)
    output = f"Припустимо, що K = {365} днів. Отже, n = {round(n,4)} р.|За таких умов матимемо:|"
    output += f"Змішаний метод нарахування відсотків : S1 =  {round(S1,2)} грн|"
    output += f"Простий метод нарахування відсотків : S2 =  {round(S2,2)} грн"
    return output

# номінальна ставка відсотка
# приклад 13
def f16(P, j, n):
    years = n / 3
    S1 = P * pow((1 + j / 4), years)
    S2 = P * pow(1 + j / 4, int(years)) * (1 + (years - int(years)) * j / 4)
    output = f"Розв'яжемо дану задачу двома методами: загальним та змішаним| Згідно умови задачі кількість періодів нарахування складає {round(years,2)}|"
    output += f"Загальний метод : S1 = {round(S1,2)}|"
    output += f"Змішаний метод : S2 = {round(S2,2)}"
    return output


# ефективна відсоткова ставка
# приклад 14
def f17(j, n):
    res = pow(1 + j/4, n * 4)
    output = f"Множник нарощення становить : {round(res,2)}"
    return output

# приклад 15
def f18(j):
    i1 = pow(1 + j/12, 12) - 1
    i2 = pow(1 + j/365, 365) - 1
    output = f"Ефективна річна ставка за умов щомісячної капіталізації : {round(i1*100,2)}%|"
    output += f"Ефективна річна ставка за умов щоденної капіталізації : {round(i2*100,2)}%"
    return output

# приклад 16
def f19(j, m, n):
    res = m * (pow(1 + j / n, n/m) - 1)
    return f'Номінальна ставка j^{int(m)} = {round(res,4)} = {round(res * 100, 2)}%'


# математичне дисконтування та облік за складними ставками відсотка
# 2.2.1 математичне дисконтування за складною відсотковою ставкою
# приклад 17

def f20(S, n, i):
    P = S /pow(1 + i, n)
    return f"P = {round(P,2)}"

# приклад 18
def f21(S, n, i):
    P = S / pow(1 + i/4, 4 * n)
    return f"P = {round(P,2)} грн"

# облік за складною обліковою ставкою
# приклад 19
def f22(S, n, i):
    P = S * pow(1 - i, n)
    D = S - P
    output = f"P = {round(P,2)} грн|"
    output += f"D = {round(D,2)} грн"
    return output


# приклад 20, 21
def f23(S, n, i):
    P = S * pow(1 - i/2, 2 * n)
    D = S - P
    d = 1 - pow(1 - i/2, 2)
    output = f"P = {round(P,2)}|"
    output += f"D = {round(D,2)}|"
    output += f"Ефективна облікова ставка : {round(d,4)} = {round(d * 100, 2)}%"
    return output

# приклад 22
def f24(P, i, n):
    S = P / pow(1-i, n)
    return f"Нарощена сума боргу : S = {round(S,2)} грн"

execution_queue = {
                    f13: [100000, 0.2, 3],
                    f14: [50000, 0.15, 0.03, 0.04, 2, 4],
                    f15: [300000, 0.25, 2, 155],
                    f16: [100000, 0.22, 31],
                    f17: [0.15, 3],
                    f18: [0.2],
                    f19: [0.25, 4, 12],
                    f20: [10000, 3, 0.3],
                    f21: [10000, 3, 0.3],
                    f22: [100000, 3.5, 0.2],
                    f23: [100000, 3.5, 0.2],
                    f24: [50000, 0.17, 5],
}
'''
for i in execution_queue:
    i(*execution_queue[i])
    print("#" * 20)
'''