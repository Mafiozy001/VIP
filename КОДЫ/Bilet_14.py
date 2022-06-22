str=input('Введите предложение:\n')
znaki = ['.', '-', ',', ';', ':', '!', '*', '?']
out_lst=[]
 
for i in str:
        if i in znaki:
            out_lst.append(i)
 
print('В этой строке содержаться', len(out_lst), 'знака припинания')
