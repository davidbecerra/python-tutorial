f = open('alphabet.csv', 'r')

for line in f:
    print('-> ' + line)

f.close()