list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = 0
a = len(list_numbers) - 1
for i in range(len(list_numbers)):
    if list_numbers[i] >= list_numbers[max_]:
        max_ = i
list_numbers[max_], list_numbers[a]= list_numbers[a], list_numbers[max_]



print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
