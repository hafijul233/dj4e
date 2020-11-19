# Use words.txt as the file name

fname = input('Enter file name: ')

fh = open(fname)
for line in fh:
    clean_line = line.strip()
    upper_line = clean_line.upper()
    print (upper_line)

