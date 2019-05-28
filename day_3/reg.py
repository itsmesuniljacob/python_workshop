import re
x = re.findall(r'\Bf[a-z]*','which bigfoot or hand fell fastest')
print(x)
# start with s, followed by any character and check for the vowels
s = re.findall('s.[aeiou]','she sells seashells on the seashore')
print(s)
print( re.findall(r'\bs.[aeiou]','she sells seashells on the seashore'))
line = 'she sells sea shells on the seashore'
print(re.sub('l','LL',line))
print(re.sub('sea','ocean',line))
print(re.findall('(sh[aeiou]|sea)',line))
matchObj = re.match(r'(.*) shells (.*?) (.*)',line, re.M | re.I)
print('---------------------------------------------------------')
if matchObj:
    print('matchObj.group(): ',matchObj.group())
    print('matchObj.group(1): ',matchObj.group(1))
    print('matchObj.group(2): ',matchObj.group(2))
    print('matchObj.group(3): ',matchObj.group(3))