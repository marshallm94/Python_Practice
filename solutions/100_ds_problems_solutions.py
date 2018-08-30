import numpy as np

# General Programming
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

def simplify_polynomial(list_of_tups):
    string = ""
    for term in list_of_tups:
        coef = term[0]
        degree = term[1]
        if len(str(np.sign(coef))) == 1:
            sign = "+"
        elif len(str(np.sign(coef))) == 2:
            sign = "-"

        if coef == 0:
            continue
        elif abs(coef) == 1:
            if degree == 0:
                current_string = f" {sign} 1"
            elif degree > 0:
                if degree != 1:
                    current_string = f" {sign} x^{degree}"
                elif degree == 1:
                    current_string = f" {sign} x"
            elif degree < 0:
                if degree != -1:
                    current_string = f" {sign} (1/x^{degree})"
                elif degree == -1:
                    current_string = f" {sign} (1/x)"
        elif abs(coef) != 1:
            if degree == 0:
                current_string = f" {sign} {abs(coef)}"
            elif degree > 0:
                if degree != 1:
                    current_string = f" {sign} {abs(coef)}x^{degree}"
                elif degree == 1:
                    current_string = f" {sign} {abs(coef)}x"
            elif degree < 0:
                if degree != -1:
                    current_string = f" {sign} (1/{abs(coef)}^{degree})"
                elif degree == -1:
                    current_string = f" {sign} (1/{abs(coef)})"
        else:
            continue

        string += current_string

    if string[1] == "-":
        return string[1:]
    elif string[1] == "+":
        return string[3:]

print(simplify_polynomial(group_1))
print(simplify_polynomial(group_2))
print(simplify_polynomial(group_3))

print("\nNumber 9 (version 2) Output:")

def combine_terms(list_of_tups):
    list_of_tups.sort(key=lambda x: x[1])
    out = []
    cache = []
    for x, tup in enumerate(list_of_tups):
        coef = tup[0]
        degree = tup[1]
        if tup in cache or coef == 0:
            cache.pop()
            continue
        else:
            for other_tup in list_of_tups[x+1:]:
                other_coef = other_tup[0]
                other_degree = other_tup[1]
                if other_degree == degree:
                    cache.append(other_tup)
                    coef += other_coef

        out.append((coef, degree))
    for coef, degree in out:
        if coef == 0:
            out.remove((coef, degree))

    # out.reverse()
    # return simplify_polynomial(out)
    return out


print(combine_terms(group_1))
print(combine_terms(group_2))
print(combine_terms(group_3))

print("\nNumber 10 Output:")

def differentiate_polynomial(list_of_tups):
    terms = combine_terms(list_of_tups)
    derivative = []

    for coef, deg in terms:
        if deg == 0:
            continue
        else:
            new_deg = deg - 1

        new_coef = coef*deg

        derivative.append((new_coef, new_deg))

    return derivative

print(differentiate_polynomial(group_1))
print(differentiate_polynomial(group_2))
print(differentiate_polynomial(group_3))

print("\nNumber 11 Output:")

language = {"number", "numbers", "ship", "ships",
            "hip", "hips", "swear", "wear"}

def split_into_words(word, language):
    out = []
    for i in language:
        word_set = set(word.partition(i))
        inter = word_set.intersection(language)
        if len(inter) > 0:
            string = " ".join(inter)
        else:
            continue

        if string in out:
            continue
        else:
            out.append(string)

    length = max([len(i.split()) for i in out])

    return [i for i in out if len(i.split()) == length]

print(split_into_words('number', language))
print(split_into_words('numbership', language))
print(split_into_words('numbershipswear', language))

# Data Manipulation
# 1
arr = np.array((0,0,1,0,1))

def binary_to_RB(arr):
    return np.where(arr == 0, 'red', 'blue')

print(binary_to_RB(arr))

# 2
x = np.arange(1,6)
b = np.array((1,1,0,0,1))

def binary_mean(x, b):
    out_dict = {}
    out_dict[1] = x[b == 1].mean()
    out_dict[0] = x[b == 0].mean()
    return out_dict

print(binary_mean(x, b))

# 3
x = np.array([[0,1],[2,1]])

def get_mean(arr, label):
    if label == 'row':
        return arr.mean(axis=1)
    elif label == 'column':
        return arr.mean(axis=0)

print(get_mean(x, 'row'))
print(get_mean(x, 'column'))
