import re
fh = open("regex_sum_42.txt", 'r')
total = 0
numbers = []

for line in fh:
    y = re.findall('[\d]+', line)
    numbers += y;

for num in numbers:
    total+=int(num)

print(total)
