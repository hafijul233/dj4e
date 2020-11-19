# Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that
# maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using
# a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
senders = dict()

for line in fh:
    if not line.startswith("From "):
        continue
    else:
        ind = line.split()
        senders[ind[1]] = senders.get(ind[1], 0) + 1;

bigsender = ''
maxnow = 0
for email, count in senders.items():
    #    print(email, "->", count)
    if count > maxnow:
        maxnow = count
        bigsender = email

print(bigsender, senders[bigsender])
