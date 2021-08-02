# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program creates a Python
# dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be openend:", fname)
    quit()
count = 0
mailno = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    count = count+1
    word = line.rstrip().split()
    mailno[word[1]] = mailno.get(word[1], 0) + 1
maxkey = None
maxvalue = None
for key, value in mailno.items():
    if maxvalue is None or maxvalue < value:
        maxvalue = value
        maxkey = key
print(maxkey, maxvalue)
