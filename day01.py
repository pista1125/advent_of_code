
with open("day_01.txt", mode="r", encoding='cp1250') as data:
    df = data.readlines()

df = [x.replace(f"\n", "") for x in df]

#1. day 1 first part

# final_number = 0
# for x in df:
#     number = []
#     for y in x:
#         is_digit = y.isdigit()
#         if is_digit:
#             number.append(y)
#     final_number += int(number[0] + number[-1])
#
# print(final_number)

#1. day 1 second part

old_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
old_str_1 = ["on", "tw", "thre", "fou", "fiv", "si", "seve", "eigh", "nin"]
new_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

dt = []

for item in df:
    find_num = []
    for x in range(9):
        find_num.append(item.find(old_str[x]))

    dt_item = []
    find_num_2 = find_num
    for x in range(9):
        try:
            find_num_2.remove(-1)
        except:
            continue
    find_num = []
    for e in range(9):
        find_num.append(item.find(old_str[e]))
    z = -1
    for h in range(len(find_num_2)):
        min_value = min(i for i in find_num if i > z)
        y = find_num.index(min_value)
        item = item.replace(old_str_1[y], new_str[y])
        z = min_value
    dt.append(item)
print(dt)


final_number = 0
for x in dt:
    number = []
    for q in x:
        is_digit = q.isdigit()
        if is_digit:
            number.append(q)
    final_number_add = int(number[0] + number[-1])
    final_number += final_number_add
    print(final_number_add)
print(final_number)



# import re
#
# d = "one two three four five six seven eight nine".split()
# r = 0
#
# def convert(n):
#     if n in d:
#         return str(d.index(n) + 1)
#
#     else :
#         return n
#
# with open("day_01.txt") as f:
#     lines = f.readlines()
#
#     for line in lines:
#         digits = list(map(convert, re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)))
#         new_number = int(digits[0] + digits[-1])
#         r = r + new_number
#         print(new_number)
#     print(r)