list1 = [1,2,3,4,]

empty_list = list()

list_from_sequence = list("non-empty string")

for element in list_from_sequence:
    print(element)

empty_list.append(1)
empty_list.pop()

list_from_sequence.sort()


# slices
list_from_sequence_slice = list_from_sequence[1:4]
list_from_sequence.reverse()
list_from_sequence_reversed = list_from_sequence[::-1]



