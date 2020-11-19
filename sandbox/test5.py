fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
senders = dict()

for line in fh:
    if not line.startswith("From ") :
        continue
    else :
        ind = line.split()
        senders[ind[1]] = senders.get(ind[1], 0) +1;

bigsender = ''
maxnow = 0
for email, count in senders.items():
#    print(email, "->", count)
    if count > maxnow :
        maxnow = count
        bigsender = email

print(bigsender, senders[bigsender])
    
