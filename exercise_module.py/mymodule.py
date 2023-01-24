
def countlines_file(s):
    lines= len(s.readlines())
    
    return lines

def countChars_file(a):
    data=a.read()
    #print(data)
    return len(data) 


def testname_file(b):
    lines=countlines_file(b)
    b.seek(0)
    char1 =countChars_file(b)
    return lines,char1


if __name__ == "__main__":
    file = open(r"C:\Users\Saroj Dhiman\OneDrive\Documents\08_class.py\exercise_module.py\mymod.txt",mode='r')
    
    testname_lines,testchar=testname_file(file)
    print("hello!")














