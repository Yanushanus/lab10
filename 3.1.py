''' 3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.Метод рекурсії'''
from random import randint
import numpy as np
import timeit
def maxind(arr, i=0, j=0, i_max=0, j_max=0,maxnum=0):#Створення функції для перевірки елементів
    if j == len(arr[i]):
        i += 1  #Рядок
        j = 0  #Стовбчик
    if i == len(arr):
        return i_max, j_max
    if arr[i][j] > arr[i_max][j_max]:
        maxnum=arr[i][j]
        i_max = i
        j_max = j
    j += 1
    return maxind(arr, i, j, i_max, j_max)
n=int (input('Enter your length:'))
if 1<=n<=5:#Створення масиву
    m=n
    akk=np.zeros((n,m),dtype=int)
    for i in range(n):
        for j in range (m):
            akk[i][j]=randint(1,20)
    print(f'Your array:\n{akk}')
    print(f'Your position of max el:{maxind(akk)}')
else:
    print('You are out of length')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')
'''Написання програми зайняло близько години,через труднощі у розумінні як правильно написати алгоритм '''

