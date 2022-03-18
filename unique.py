
def find_unique_elements(list_one, list_two):
    """ Определение элементов,которые есть в 1-ом списке, но нет во 2-ом
    Сложность О(n*m), где n и m - длины списков """
    return [x for x in list_one if x not in list_two]

if __name__ == '__main__':
    list_one = [x for x in range(10)]
    print(f'Первый список: {list_one}')
    list_two = [x*x for x in range(10)]
    print(f'Второй список: {list_two}')

    result = find_unique_elements(list_one, list_two)
    print(f'Элементы, отсутствующие по втором списке: {result}')
