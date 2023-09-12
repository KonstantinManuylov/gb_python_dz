from random import randint


def get_random_array(array_len):
    """
    Получение случайного массива

    :param array_len: Размерность массива
    :return: Список чифр
    """
    return [randint(0, 9) for _ in range(array_len)]


def get_doubles(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] == array[i]:
                count += 1
    return count


if __name__ == "__main__":
    n = int(input("Введите размер массива: "))
    array = get_random_array(array_len=n)
    print("Массив:", array)
    print("Количество повторений:", get_doubles(array=array))