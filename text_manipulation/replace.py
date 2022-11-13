import sys

file = open(sys.argv[1], 'r')
data = file.read()
file = open(sys.argv[2], 'w')
file.write(data.replace(sys.argv[3], sys.argv[4]))
file.close()
