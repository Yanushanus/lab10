''' 3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.Метод ітерації'''
from random import randint
import numpy as np
import timeit
def maxpos(arr):#Створення функції для перевірки елементів
    imax = 0
    jmax = 0
    maxel=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > arr[imax][jmax]:
                maxel=arr[i][j]                            #
                imax = i
                jmax=j
    return (f'Your maxel:{maxel} on position{imax+1},{jmax+1}')
n=int(input('Enter your num'))
if 1<=n<=5:#Створення масиву
    m=n
    a=np.zeros((n,m),dtype=int)
    for t in range(n):
        for q in range(m):
            a[t][q]=randint(1,20)
    print(f'Your array:\n{a}')
    print(maxpos(a))
else:
    print('You are out of length')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')
'''Алгоритм через ітерацію значно легше сформувати ніж через рекурсію.Написання програми зайняло близько 20 хвилин'''
