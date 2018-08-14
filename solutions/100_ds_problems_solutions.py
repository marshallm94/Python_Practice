import numpy as np

# 1
print("Number 1 Output:")
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
print("\nNumber 2 Output:")
test_list = dict_to_list(test_dict)
def list_to_dict(input_list):
    out = {k: [] for k in input_list[0].keys()}
    for i in input_list:
        for k, v in i.items():
            out[k].append(v)
    return out

print(list_to_dict(test_list))

# 3
print("\nNumber 3 Output:")
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
print("\nNumber 4 Output:")
def str_to_dict(string):
    words = string.split()
    return {word[0]: [word_2 for word_2 in words if word_2[0] == word[0]] for word in words}

test_string = "a special string bearing an important salutation"
print(str_to_dict(test_string))

# 5
print("\nNumber 5 Output:")
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
print('newfile.txt contents:')
with open('newfile.txt', 'r') as f1:
    print(f1.read())

# 6
print("\nNumber 6 Output:")
def transpose(liz, method='numpy'):
    if method == 'numpy':
        X = np.array(liz)
        transpose = X.T
        return [list(arr) for arr in transpose]
    elif method == 'python':
        rows = len(liz)
        cols = len(liz[0])
        return [[liz[j][i] for j in range(cols)] for i in range(rows)]

test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(test_list, 'python'))

# 7
print("\nNumber 7 Output:")
def get_valid_passwords(possible_passwords):
    digits = set([str(i) for i in range(10)])
    special = set("^ ! # $ ? -".split())
    out = []
    dig_bool_cache = False
    spec_bool_cache = False
    for poss in possible_passwords:
        for char in poss:
            if char in digits:
                dig_bool_cache = True
            if char in special:
                spec_bool_cache = True
        if dig_bool_cache and spec_bool_cache:
            out.append(poss)
        dig_bool_cache = False
        spec_bool_cache = False
    return out

possible_passwords = ['moshi', 'm0shi', 'mosh!', 'm0sh!', '^^oshi',
                      '^^0shi', '^^0sh!']
print(get_valid_passwords(possible_passwords))

# 8
print("\nNumber 8 Output:")
def pretty_math(coef_list):
    degree = len(coef_list) - 1
    string = ""
    for x, i in enumerate(coef_list):
        if i < 0:
            string += f"- {abs(i)}x^{degree} "
        elif i > 0:
            string += f"+ {abs(i)}x^{degree} "
        else:
            degree -= 1
            continue
        degree -= 1
    string = string.replace("x^1", "x")
    string = string.replace("x^0", "")
    string = string.replace("+ 1x", "+ x")
    string = string.replace("- 1x", "- x")
    return string[2:]


list_1 = [1, 1, 1]
list_2 = [2, -1, -2]
list_3 = [0, 9, -10]
list_4 = [10, 11, 110, 1, 10]
print(pretty_math(list_1))
print(pretty_math(list_2))
print(pretty_math(list_3))
print(pretty_math(list_4))

# 9
print("\nNumber 9 Output:")
group_1 = [(1, 0), (1, 1), (1, 2)]
group_2 = [(2, 0), (-2, 1), (2, 2), (-2, 2)]
group_3 = [(1, 0), (1, 1), (1, 0), (1, 1)]

def pretty_math_2(list_of_tups):
    string = ""
    for term in list_of_tups:
        degree = term[1]
        coef = term[0]
        if len(str(np.sign(coef))) == 1:
            sign = "+"
        elif len(str(np.sign(coef))) == 2:
            sign = "-"

        if degree == 0 and coef == 0:
            continue
        elif degree == 0 and coef != 0:
            current_string = f"{sign} {abs(coef)} "
        elif degree != 0 and coef == 0:
            continue
        elif degree != 0 and coef != 0:
            current_string = f"{sign} {abs(coef)}x^{degree} "
        string += current_string
    return string[2:]

print(pretty_math_2(group_1))
print(pretty_math_2(group_2))
print(pretty_math_2(group_3))
