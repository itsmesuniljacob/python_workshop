dayofweek = input('Enter day of week\n')
dayofweek = dayofweek.lower()
if ((dayofweek == 'monday') or (dayofweek == 'tuesday') or (dayofweek == 'wednesday') or (dayofweek == 'thursday') or (dayofweek == 'friday')):
   print('Time is 9 to 6')
elif (dayofweek == 'saturday'):
   print('9 to 1')
elif (dayofweek == 'sunday'):
   print('Holiday')
else:
   print('Invalid input')   