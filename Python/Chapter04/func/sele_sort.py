__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

def sele_sort(number):
    def min_index(left, right):
        if right == len(number):
            return left
        elif number[right] < number[left]:
            return min_index(right, right + 1)
        else:
            return min_index(left, right + 1)

    for i in range(len(number)):
        selected = min_index(i, i + 1)
        if i != selected:
            number[i], number[selected] = number[selected], number[i]

number = [int(arg) for arg in sys.argv[1:]]
sele_sort(number)
print(number)
