fname = input("Enter file name: ")        
fh = open(fname)
lst = list()
        
for line in fh:
    cle_line =line.strip()
    wordlist = cle_line.split()

    for words in wordlist:
        lst.append(words)

lst = list(dict.fromkeys(lst)) 
lst.sort()
print(lst)
