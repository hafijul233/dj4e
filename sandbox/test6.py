fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
senders = dict()

for line in fh:
    if not line.startswith("From ") :
        continue
    else :
        ind = line.split()
        hours = ind[5].split(":")[0]
        senders[hours] = senders.get(hours, 0) +1;

send_list = []

for (h, i) in senders.items():
	send_list.append((h,i))

send_list.sort()

for h,i in send_list:
	print(h,i)