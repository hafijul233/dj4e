# You can write any code you like in the window below.
# There are three files loaded and ready for you to open
# if you want to do file processing: "mbox-short.txt",
# "romeo.txt", and "words.txt".

fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count, "Lines")
