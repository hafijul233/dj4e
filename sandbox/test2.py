# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
spamTotal = 0
count = 0;
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        ind = line.find(":")
        substr = line[ind+1:len(line)]
        clean = substr.strip()
        num = float(clean)
        spamTotal+=num
        count+=1
    
print("Average spam confidence:", (spamTotal/count))
