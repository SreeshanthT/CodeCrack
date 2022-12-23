import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.search("\d", txt)
print(dir(x))