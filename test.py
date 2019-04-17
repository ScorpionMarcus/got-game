temp = file.read().splitlines()

fh = open('characters.txt')
for line in fh:
    print(line)
fh.close()