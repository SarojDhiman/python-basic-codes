
import mymodule
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
lines=mymodule.countlines_file(file)
print("the number of lines are=",lines)
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
counts=mymodule.countChars_file(file)
print("the number of charter are=",counts)
file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
testname_lines,testchar=mymodule.testname_file(file)
print(f"the number of lines are={testname_lines} and the character are{testchar}")



#-----------------------------------------------------------------------------------
