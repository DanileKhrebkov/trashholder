list = [1,2,3,4,5]
keylist = []
counter = 0
print(len(list))
for i in range(1,6):
    counter +=1
    print(i)
    keylist.append([counter, list[i]])


print(f'Кол-во итераций: {counter}')
print(f'кол-во элементов в списке: {len(list)}')
print(keylist)