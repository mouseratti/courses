list1 = [1,2,3,4,4,1,2,3]
empty_list1 = []
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

index = 0
while index < 16:
    print(list_from_sequence[index])
    index += 1

# for index, element in enumerate(list_from_sequence):
#     if index in (2,3,4): list_from_sequence.append(element)

