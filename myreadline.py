fileobj = open('test.txt')
line = fileobj.readline()
i = 0
while line:
  i+=1
  print(i,"", line)
  line = fileobj.readline()
fileobj.close()

# readlines returns a list of lines