import newpackage.fact
fileobj = open('test.txt')
file2 = open('test1.txt','w')
#print(fileobj.read())
# Write the contents to file2 after reading from file1
file2.write(fileobj.read())
fileobj.close()
file2.close()