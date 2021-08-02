# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for
# your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1317324.txt (There are 76 values and the sum ends with 608)

import re
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be openend:", fname)
    quit()
Singlefile = fh.read()
y = re.findall('[0-9]+', Singlefile)
count = 0
sum = 0
for x in y:
    count = count + 1
    sum = sum + int(x)
print(sum)
print(count)
