#OPEN -- open()
"""
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

"""
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
path = 'E:\\Sreeshanth\\Django-test\\CodeCrack\\sample\\sample.txt'
f = open(path,'rt')
# print(f.read())
# print(f.readline())

# print(f.encoding)
# print(dir(f))

# print("kja")

"""
Close the file when you are finish with it:
f.close()
"""

#append/edit.create

f = open(path, "a")
f.write("\nNow the file has more content!")
f.close()

f = open(path, "r")
# print(f.read())

#"x" - Create - will create a file, returns an error if the file exist

# f = open("myfile.txt", "x")

import os
os.remove("myfile.txt")