import os

m=os.listdir("io")
'''for i in m:
    if "out" in i:
        print("\"",i,"\"",end=",")'''
outputs=[
    [["set1a output1.txt","set1a output2.txt"],["set2a output1.txt","set2a output2.txt"],["set3out a-1.txt","set3out a-2.txt"]],
    [["set1b output1.txt","set1b output2.txt"],["set2b output1.txt","set2b output2.txt"],["set3 out b-1.txt","set3 out b-2.txt"]],
    [["set1c output1.txt","set1c output2.txt"],["set2c output1.txt","set2c output2.txt"],["set3 out b-1.txt","set3 out b-2.txt"]],
    [["set1d output1.txt","set1d output2.txt"],["set2d output1.txt","set2d output2.txt"],["set3 out -d1.txt","set3 out -d2.txt"]],
    [["set1e output1.txt","set1e output2.txt"],["set2e output1.txt","set2e output2.txt"],["set3 out -e1.txt","set3 out -e2.txt"]],   
    ]
for i in outputs:
    for j in i:
        for k in j:
            #if 'o' in k:
            #print(k)
            a=open("io/"+k,"r")
            print(a.read(),end="")
'''

inputs=[
    [["set1a input1.txt","set1a input2.txt"],["set2a input1.txt", "set2a input2.txt"],["set3-a1.txt ","set3-a2.txt "]],
    [["set1b input1.txt","set1b input2.txt"],["set2b input1.txt", "set2b input2.txt"],["set3-b1.txt ","set3 -b2.txt "]],
    [["set1c input1.txt","set1c input2.txt"],["set2c input1.txt", "set2c input2.txt"],["set3 -c1.txt ","set3 -c2.txt "]],
    [["set1d input1.txt","set1d input2.txt"],["set2d input1.txt", "set2d input2.txt"],["set3 d1.txt ","set3 d2.txt "]],
    [["set1e input1.txt","set1e input2.txt"],["set2e input1.txt", "set2e input2.txt"],["set3 e1.txt ","set3 e2.txt "]]
]        
7829628899
for i in inputs:
    for j in i:
        for k in j:
            #if 'o' in k:
            #print(k)
            a=open("io/"+k,"r")
            print(a.read(),end="")'''
