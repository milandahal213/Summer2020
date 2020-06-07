# Read from a text file

#Open the file, read the value and close the file 
f = open("output.txt","r")
text=f.read()
f.close()
print(text)