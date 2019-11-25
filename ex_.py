import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

z = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
bb = re.findall("\S+?@\S+",z)

print(bb)
