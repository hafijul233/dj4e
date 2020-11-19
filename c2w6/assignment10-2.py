# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

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
        hours = ind[5].split(":")[0]
        senders[hours] = senders.get(hours, 0) + 1;

send_list = []

for (h, i) in senders.items():
    send_list.append((h, i))

send_list.sort()

for h, i in send_list:
    print(h, i)
