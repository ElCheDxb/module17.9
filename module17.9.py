numbers = input('Введите последовательность челых чисел через пробел: ')

if ',' in numbers:
    print('Вводить можно только целые числа через пробел. Попробуйте еще раз.'), exit()

elif '.' in numbers:
    print('Вводить можно только целые числа. Попробуйте еще раз.'), exit()

element = int(input('Введите любое целое число: '))

# Преобразование введённой последовательности в список
array = list(map(int, numbers.split()))

#число не соответсвуюет заданному условию
if element < array[0] or element > array[-1]:
    print('Введенный элемент не подходит, начните заново.'), exit()

# сортировка вставками
def sort():
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x

# двоичный поиск элемента
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
#вызываем функцию сортировки
sort()

x = binary_search(array, element, 0, len(array))
# Устанавливаем номер позиции элемента, который меньше введенного пользователем числа
if element in array:
    print('номер позиции элемента, который меньше введенного пользователем числа: ', x - 1)

else:
    while element not in array:
        element = element-1
        x = binary_search(array, element, 0, len(array))
    if element in array:
        print('Hомер позиции элемента, который меньше введенного пользователем числа: ', x)