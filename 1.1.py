'''1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n через рекурсію'''
import timeit
def fact(x):
    if x==0:
        return 1
    else:
        return fact(x-1)*x #Визначення функції самої через себе
kawai=int(input('Enter your factorial: '))
print(f'Your factorial: {fact(kawai)}')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')

'''Написання програми зайняло 5-7 хвилин,читабельність коду:нормальна'''