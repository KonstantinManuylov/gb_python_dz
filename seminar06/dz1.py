from random import randint as rnd

def prompt(msg: str) -> int:
    return int(input(msg))

def create_indexes_list(min: int, max: int, num_lst: list[int]) -> list[int]:
    return [index for index in range(len(num_lst)) if min <= num_lst[index] <= max]

min_num = prompt("Введите нижнюю границу диапазона > ")
max_num = prompt("Введите верхнюю границу диапазона > ")
nums_list = [rnd(-10, 10) for _ in range(20)]
print(nums_list)
result_list = create_indexes_list(min_num, max_num, nums_list)
print(result_list)