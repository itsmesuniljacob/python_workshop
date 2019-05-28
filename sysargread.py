import sys
fileobj = sys.argv[1]
file = open(fileobj)
print(file.readlines())
file.close()