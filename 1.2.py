'''1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n через ітерацію'''
import timeit
def fact(x):
    fac=1
    while x>1:#Створення циклу для перемноження значень на кожному проході циклу для визначення факторіалу
        fac*=x
        x-=1
    return fac
kav=int(input('Enter your num'))
print(f'Your fact:{fact(kav)}')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')

'''Написання зайняло біля 10 хвилин.Місткість коду трохи більше ніж в рекурсивному методі'''