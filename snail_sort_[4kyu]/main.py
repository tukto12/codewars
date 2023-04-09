'''
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]


array_one = [[1, 2, 3, 4],
             [12, 13, 14, 5],
             [11, 16, 15, 6],
             [10, 9, 8, 7]]


def array_solution(array):
    array_sort = []

    while array:
        # REMOVE TOP
        array_sort += array.pop(0)

        #REMOVE RIGHT SIDE
        for i in range(len(array)):
            array_sort.append(array[i].pop(-1))

        # REMOVE BOTTOM
        if array:
            array_sort += reversed(array.pop(-1))

        # REMOVE LEFT SIDE
        for j in range(len(array)-1, -1, -1):
            array_sort.append(array[j].pop(0))

    return array_sort


print(array_solution(array))
print(array_solution(array_one))
