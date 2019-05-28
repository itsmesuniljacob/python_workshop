i = 1
while i <= 10:  
  print(i)
  #print(i,end=",")
  i += 1
  if i == 5:
    break
# the else block in while gets executed if there is no BREAK in while loop	
else:
  print('Outside while loop')  
  