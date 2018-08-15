#File objects
from os import path

strPath = r"D:\code_sandbox\sandbox_python\intro to python\digits.txt"
print("the current directory is: " , strPath)
print("the final current directory is:", path.abspath(strPath))
print("the directory name:", path.dirname(strPath))
print("base name is:", path.basename(strPath))

#try to get current file directory
print("My current file directory: ", )

f = open(strPath)

print(f.name)

f.close()