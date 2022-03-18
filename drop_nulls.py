from random import randint

def drop_nulls(array):
    """ Удаление из списка целых чисел нулей  """
    index = 0
    for item in array:
        if item != 0:
            array[index] = item
            index += 1
    # Красиво использовать array[:index], но нет уверенности, что
    # эта операция по памяти будет O(1)
    # Поэтому отрезаем лишние элементы с конца массива
    for _ in range(index, len(array)):
        array.pop()
    return array

if __name__ == '__main__':
    # array = [randint(0, 10) for _ in range(20)]
    array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
    print(array)
    array = drop_nulls(array)
    print(array)
