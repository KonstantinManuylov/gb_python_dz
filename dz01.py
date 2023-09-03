# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8 # 8

list_1 = [1, 12, 6, 7, 8, 15]
k = 11 # 12

def find_closest_number(num_lst, num):
    sorted_list = num_lst.sort()
    num1 = num2 = num
    if num not in num_lst:
        while num1 not in num_lst or num2 not in num_lst:
            num1 -= 1
            num2 += 1
            if num1 in num_lst:
                return num1
            if num2 in num_lst:
                return num2

if k in list_1:
    print(k)
else:
    print(find_closest_number(list_1, k))