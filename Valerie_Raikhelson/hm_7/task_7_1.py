import numpy as np

# first decision
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(6, 2)
print(new_arr)

# second decision
multi_array = []


def change_elements_in_multi_array(rows, elements, array):
    def create_multi_array(number_of_rows, number_of_elements):
        for _ in range(number_of_rows):
            multi_array.append([0] * number_of_elements)

    create_multi_array(rows, elements)

    index = 0
    for row in range(rows):
        for element in range(elements):
            multi_array[row][element] = array[index]
            index += 1


array = [1, 2, 3, 4, 5, 6, 7, 8]
r = 4
e = 2

change_elements_in_multi_array(r, e, array)
print(multi_array)
