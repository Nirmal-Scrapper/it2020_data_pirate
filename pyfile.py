import PyPDF2 as p,os
import random
import time

files=[["pdf/set1 a.pdf","pdf/set2 a.pdf","pdf/set3 a.pdf"],
       ["pdf/set1 b.pdf","pdf/set2 b.pdf","pdf/set3 b.pdf"],
       ["pdf/set1 c.pdf","pdf/set2 c.pdf","pdf/set3 c.pdf"],
       ["pdf/set1 d.pdf","pdf/set2 d.pdf","pdf/set3 d.pdf"],
       ["pdf/set1 e.pdf","pdf/set2 e.pdf","pdf/set3 e.pdf"]]
password = "back up/password.txt" 

inputs=[
    [["set1a input1.txt","set1a input2.txt"],["set2a input1.txt", "set2a input2.txt"],["set3-a1.txt ","set3-a2.txt "]],
    [["set1b input1.txt","set1b input2.txt"],["set2b input1.txt", "set2b input2.txt"],["set3-b1.txt ","set3 -b2.txt "]],
    [["set1c input1.txt","set1c input2.txt"],["set2c input1.txt", "set2c input2.txt"],["set3 -c1.txt ","set3 -c2.txt "]],
    [["set1d input1.txt","set1d input2.txt"],["set2d input1.txt", "set2d input2.txt"],["set3 d1.txt ","set3 d2.txt "]],
    [["set1e input1.txt","set1e input2.txt"],["set2e input1.txt", "set2e input2.txt"],["set3 e1.txt ","set3 e2.txt "]]
]

outputs=[
    [["set1a output1.txt","set1a output2.txt"],["set2a output1.txt","set2a output2.txt"],["set3out a-1.txt","set3out a-2.txt"]],
    [["set1b output1.txt","set1b output2.txt"],["set2b output1.txt","set2b output2.txt"],["set3 out b-1.txt","set3 out b-2.txt"]],
    [["set1c output1.txt","set1c output2.txt"],["set2c output1.txt","set2c output2.txt"],["set3 out b-1.txt","set3 out b-2.txt"]],
    [["set1d output1.txt","set1d output2.txt"],["set2d output1.txt","set2d output2.txt"],["set3 out -d1.txt","set3 out -d2.txt"]],
    [["set1e output1.txt","set1e output2.txt"],["set2e output1.txt","set2e output2.txt"],["set3 out -e1.txt","set3 out -e2.txt"]],   
    ]
checker='''import os
fil="output1.txt"
files="checkoutput1.txt"
file1="output2.txt"
files1="checkoutput2.txt"
num={}
path=os.path.abspath("back up\password.txt")
path=path.replace("challenge\\\\task "+str(num)+"\\\\","",1)
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
        print("key for next quest is",a[0].strip())
    else:
        print("not that perfect")
else:
    print("not even close")'''
random.seed(time.time())
selected = list()
passw=[]
for i in range(len(files)):
    curfile="challenge/task "+str(i+1)+"/checker"+str(i+1)+".py"
    mainwriter=checker.format(i+1)
    program=open(curfile,"w")
    program.write(mainwriter)
    index=random.randint(0,len(files[i])-1)
    selected.append(files[i][index])
    output = p.PdfFileWriter()
    input_stream = p.PdfFileReader(open(selected[i], "rb"))
    for j in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(j))
    curfile="challenge/task "+str(i+1)+"/challenge"+str(i+1)+".pdf"
    if(os.path.exists(curfile)):
        os.remove(curfile)
    outputstream = open(curfile, "wb")
    passw.append(str(time.time()).replace(".",""))
    output.encrypt(str(passw[i]), use_128bit=True)
    output.write(outputstream)
    outputstream.close()
    no=1
    for taskio in inputs[i][index]:
        curfile="challenge/task "+str(i+1)+"/input"+str(no)+".txt"
        readfile=open("io/"+taskio,"r")
        writefile=open(curfile,"w")
        writefile.write(readfile.read())
        readfile.close()
        writefile.close()
        no+=1
    no=1
    for taskio in outputs[i][index]:
        curfile="challenge/task "+str(i+1)+"/checkoutput"+str(no)+".txt"
        readfile=open("io/"+taskio,"r")
        writefile=open(curfile,"w")
        writefile.write(readfile.read())
        readfile.close()
        writefile.close()
        no+=1

passfile=open(password,"w")
for i in passw:
    passfile.write(i)
    passfile.write("\n")
passfile.close()
print(selected)
print(passw)

'''




'''

'''import PyPDF2
import os
import argparse
def set_password(input_file, user_pass, owner_pass):
    """
    Function creates new temporary pdf file with same content,
    assigns given password to pdf and rename it with original file.
    """
    # temporary output file with name same as input file but prepended
    # by "temp_", inside same direcory as input file.
    path, filename = os.path.split(input_file)
    output_file = os.path.join(path, "temp_" + filename)
    output = PyPDF2.PdfFileWriter()
    input_stream = PyPDF2.PdfFileReader(open(input_file, "rb"))
    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))
    outputStream = open(output_file, "wb")
    # Set user and owner password to pdf file
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()
    # Rename temporary output file with original filename, this
    # will automatically delete temporary file
    os.rename(output_file, input_file)
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--C:/Users/Nirmal/Desktop/CNS_Ch01_AJ.pdf', required=True,help='Input pdf file')
parser.add_argument('-p', '--unityb', required=True,help='output CSV file')
parser.add_argument('-o', "--unityb", default=None,help='Owner Password')
args = parser.parse_args()
set_password(args.input_pdf, args.user_password, args.owner_password)'''
