# Finding Numbers in a Haystack
# In this assignment you will read through and parse
# a file with text and numbers. You will extract all
# the numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample
# file where we give you the sum for your testing and the other
# is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
# (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1018626.txt
# (There are 93 values and the sum ends with 218)
# These links open in a new window. Make sure to save the file into
# the same folder as you will be writing your Python program.
# Note: Each student will have a distinct data file for the
# assignment - so only use your own data file for analysis.
# Data Format
# The file contains much of the text from the introduction of the textbook
# except that random numbers are inserted throughout the text.
# Here is a sample of the output you might see:

# Why should you learn to write programs? 7746
#   12 1929 8827
#   Writing programs (or programming) is a very creative
#   7 and rewarding activity.  You can write programs for
#   many reasons, ranging from making your living to solving
#   8837 a difficult data analysis problem to having fun to helping 128
#   someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...

import re

fh = open("regex_sum_42.txt", 'r')
total = 0
numbers = []

for line in fh:
    y = re.findall('[0-9]+', line)
    numbers += y;

for num in numbers:
    total += int(num)

print(total)
