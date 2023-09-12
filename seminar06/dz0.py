def prompt(msg: str) -> int:
    return int(input(msg))

def create_list(base: int, step: int, amount: int) -> list[int]:
    result_list = []
    for _ in range(amount):
        result_list.append(base)
        base += step
    return result_list

def print_result(result_list: list[int]):
    for num in result_list:
        print(num)

base_num = prompt("Введите базовое число > ")
step_num = prompt("Введите шаг > ")
nums_amount = prompt("Введите количество чисел > ")

res_list = create_list(base_num, step_num, nums_amount)
print_result(res_list)