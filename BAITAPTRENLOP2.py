from math import *
from collections import Counter
#L1
def Findchanle(a):
    checkChan=0
    checkLe=0
    for i in a:
        if(i%2==0 and checkChan==0):
            checkChan=i
        if(i%2==1 and checkLe==0):
            checkLe=i
        if(checkChan!=0 and checkLe!=0):
            break

    print((checkChan,checkLe))

#L2
def sum1(numbers, start_index, end_index):
    total = 0
    for i in range(start_index, end_index + 1):
        total += numbers[i]
    return total
#L3
def reverse(string_list):
    s = [s[::-1] for s in string_list]
    return s

#L4
def tim_phan_tu_giao(a):
    giao = set(a[0])
    for i in a[1:]:
        giao = giao.intersection(i)
    return list(giao)

#L5
def day_duy_nhat(input_list):
    unique_set = set(input_list)
    return len(input_list) == len(unique_set)
#L6
def is_sorted(input_list):
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))
#L7
def xuat_hien_nhieu_nhat(input_list):
    item_counts = Counter(input_list)
    max_count = max(item_counts.values())
    max1 = [item for item, count in item_counts.items() if count == max_count]
    return max1
#L8
def in_cot(matrix, col_index):
    column = [row[col_index] for row in matrix]
    return column

#L9
def remove_column(matrix, col_index):
    for row in matrix:
        del row[col_index]
#L10
def sort_matrix_by_row_sum(matrix):
    sorted_matrix = sorted(matrix, key=lambda row: sum(row))
    return sorted_matrix


#input L1
a1 = [1, 3, 5, 7, 4, 1, 6, 8]
print(Findchanle(a1))

#input L2
a2 = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
begin = 8
end = 10
print(sum1(a2,begin,end))

#input L3
a3 = ['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse(a3))

#input L4
a4 = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print( tim_phan_tu_giao(a4))

#input L5
a5  = [2, 4, 6, 8, 10, 12, 14]
print(day_duy_nhat(a5))

#input L6
a6  = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print(is_sorted(a6))

#input L7
a7 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print(xuat_hien_nhieu_nhat(a7))
#input L8
a8 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
cot = 2
print(in_cot(a8,cot))

#input L9
a9 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
cot9 = 0
remove_column(a9, cot9)

for hang in a9:
    print(hang)

#input L10
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sorted_matrix = sort_matrix_by_row_sum(matrix)

for row in sorted_matrix:
    print(row)