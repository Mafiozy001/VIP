import time
start_time = time.time()
n = int(input("Введите конечное число: "))
for i in range(1,n+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
end_time = time.time()
print("Выполнено за: " + str(end_time-start_time ) + " секунд" )