#an = a1 + (n-1) * d
#ебучая арифмет. прогрессия! Время 4:00-4:42

def rec_sum(a_1, d, n):
    if n == 0:
        return 0
    return a_1 + rec_sum(a_1 + d, d, n-1)# рекурсия

r = int(input("a: "))
t = int(input("d: "))
u = int(input("n: "))
print(rec_sum(r, t, u))# в конце вызываем функцию
