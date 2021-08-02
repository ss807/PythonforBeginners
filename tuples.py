# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be openend:", fname)
    quit()
count = 0
hr = None
hrno = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    count = count+1
    word = line.rstrip().split()
    hr = word[5].split(":")
    hrno[hr[0]] = hrno.get(hr[0], 0) + 1
sortedlist = list()
for key, value in hrno.items():
    sortedlist.append(key, value)
sortedlist = sorted(sortedlist)
print(sortedlist)
