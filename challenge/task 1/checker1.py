import os
fil="output1.txt"
files="checkoutput1.txt"
file1="output2.txt"
files1="checkoutput2.txt"
num=1
path=os.path.abspath("back up\password.txt")
path=path.replace("challenge\\task "+str(num)+"\\","",1)
print(path)
reader=open(fil,"r")
original=open(files,"r")
if(reader.read()==original.read()):
    reader1=open(file1,"r")
    original1=open(files1,"r")
    if(reader1.read()==original1.read()):
        passfile=open(path,"r")
        for j in range(num+1):
            a=passfile.readlines(1)
        print(a[0].strip())
    else:
        print("not that perfect")
else:
    print("not even close")