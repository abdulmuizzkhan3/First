fhand=open(r'C:\Users\Abdul Moiz\Desktop\mbox-short.txt')
for line in fhand:
    line= line.rstrip()
    if line.startswith('From'):
        #continue
        words=line.split()
        print(words)
