#Open a file to read 
fin=open("work31.py","r")
#store all the lines of the code on the variable lines
lines=fin.readlines()
#close the file
fin.close()


#Open a file to read with write permissions
fin = open("work31.py","w")
final_list = list()
for line in lines:
    if "#" in line:
        y=list(line)
        x=y.index("#")
        for i in range(0,x):
            final_list.append(y[i])
        if line[0] != "#":
            final_list.append("\n")
    else:
        final_list.append(line)
        
final="".join(final_list)
fin.write(final)
    
fin.close()
