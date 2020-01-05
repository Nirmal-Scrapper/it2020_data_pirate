import PyPDF2 as p,os
import random
import time

files=[["pdf/set1 a.pdf","pdf/set2 a.pdf","pdf/set3 a.pdf"],
       ["pdf/set1 b.pdf","pdf/set2 b.pdf","pdf/set3 b.pdf"],
       ["pdf/set1 c.pdf","pdf/set2 c.pdf","pdf/set3 c.pdf"],
       ["pdf/set1 d.pdf","pdf/set2 d.pdf","pdf/set3 d.pdf"],
       ["pdf/set1 e.pdf","pdf/set2 e.pdf","pdf/set3 e.pdf"]]
password = "back up/password.txt" 
random.seed(time.time())
selected = list()
passw=[]
for i in range(len(files)):
    index=random.randint(0,len(files[i])-1)
    selected.append(files[i][index])
    output = p.PdfFileWriter()
    input_stream = p.PdfFileReader(open(selected[i], "rb"))
    for j in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(j))
    curfile="challenge/"+"challenge"+str(i+1)+".pdf"
    if(os.path.exists(curfile)):
        os.remove(curfile)
    outputstream = open(curfile, "wb")
    passw.append(str(time.time()).replace(".",""))
    output.encrypt(str(passw[i]), use_128bit=True)
    output.write(outputstream)
    outputstream.close()
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
