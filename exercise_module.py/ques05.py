
from client import mymod
#from client.mymod import countChars_file
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
lines=mymod.countlines_file(file)
print("the number of lines are=",lines)
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
counts=mymod.countChars_file(file)
print("the number of charter are=",counts)
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
testname_lines,testchar=mymod.testname_file(file)
print(f"the number of lines are={testname_lines} and the character are{testchar}")


