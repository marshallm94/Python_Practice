# 1
test_dict = {'a': [1, 2, 3], 'b': [3, 2, 1]}
def dict_to_list(input_dict):
    out = []
    idx = 0
    val_length = len(list(input_dict.values())[0])
    while idx < val_length:
        cache = {}
        for k, v in input_dict.items():
            cache[k] = v[idx]
        out.append(cache)
        idx += 1
        cache = {}
    return out

print(dict_to_list(test_dict))

# 2
test_list = dict_to_list(test_dict)
def list_to_dict(input_list):
    out = {k: [] for k in input_list[0].keys()}
    for i in input_list:
        for k, v in i.items():
            out[k].append(v)
    return out
print(list_to_dict(test_list))

# 3
def char_to_bool(list_1, list_2):
    vowels = set(['a','e','i','o','u'])
    out = []
    for i in range(len(list_1)):
        if list_1[i] in vowels or list_2[i] in vowels:
            out.append(True)
        else:
            out.append(False)
    return out

list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = ['v', 'w', 'x', 'y', 'z']

print(char_to_bool(list_1, list_2))

# 4
def str_to_dict(string):
    words = string.split()
    return {word[0]: [word_2 for word_2 in words if word_2[0] == word[0]] for word in words}

test_string = "a special string bearing an important salutation"
print(str_to_dict(test_string))

# 5
def files_to_file(filepath_1, filepath_2, newfilepath):
    with open(filepath_1, 'r') as f1:
        with open(filepath_2, 'r') as f2:
            f1_lines = [line.strip() for line in f1.readlines()]
            f2_lines = [line.strip() for line in f2.readlines()]
            diff = abs(len(f1_lines) - len(f2_lines))
            if len(f1_lines) < len(f2_lines):
                f1_lines.extend(["zz" for i in range(diff)])
            else:
                f2_lines.extend(["zz" for i in range(diff)])
    total = list(zip(f1_lines, f2_lines))
    total = [list(i) for i in total]
    with open(newfilepath, 'w') as f3:
        for i in total:
            i.sort()
            if i[1] == 'zz':
                f3.write(i[0])
                f3.write('\n')
            else:
                f3.write(", ".join(i))
                f3.write('\n')

files_to_file('test1.txt','test2.txt','newfile.txt')

# 6
test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
