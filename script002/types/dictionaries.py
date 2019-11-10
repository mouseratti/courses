empty_dict = {}
empty_dict2 = dict([(1,2), (3,4)])
non_empty_dict = {'key1': 'value1', 2: 'value2', 3.0: 'value3'}

for key in non_empty_dict:
    print(key, non_empty_dict[key], non_empty_dict.get(key, "No such key!"))

new_dict = {'item1':1.0, 'item2': 2.0}
non_empty_dict.update(new_dict)

non_empty_dict['item3'] = 3.5
