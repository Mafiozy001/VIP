import random
q = random.randint(1,45)
w = random.randint(1,45)
e = random.randint(1,45)
r = random.randint(1,45)
t = random.randint(1,45)
y = random.randint(1,45)
u = random.randint(1,45)
i = random.randint(1,45)
a = [q,w,e,r,t,y,u,i,]
#a = list(map(int, input().split()))#одиночный ввод
class abs:
    print(a)
class abc:
    for i in range(0, len(a) - 1, 2) :
        a[i], a[i+1] = a[i+1], a[i]
    print(a)
    #Я не уверен, что сделал то что надо.