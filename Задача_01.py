# Найти сумму чисел списка стоящих на нечетной позиции. Пример:[1,2,3,4] -> 4

a = [1, 2, 3, 4,5,6,7,8] # исходный список
l = a[::2] # формирую список из элементов стоящих на нечётных позициях
print(l) # вывожу новый список, просто для наглядности
print('Сумма чисел на нечётных позициях = ',sum(l)) # вывожу сумму чисел согласно условию задачи