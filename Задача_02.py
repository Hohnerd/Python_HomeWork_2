# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import math
a = [2,7,4,9,1,3,6] # задаю список
middleList = math.ceil(len(a)/2) # определяю середину списка (или сколько значений будет содержать конечный результат)
result = [a[i] * a[len(a) - i - 1] for i in range(middleList)] # перемножаю элементы согласно условию задачи (middleList) раз
print(result)
