# Write to a text file

#Open the file, write the value and close the file 
f = open("output.txt","w")
message="Hi all! Welcome from CEEO Innovations!"
text=f.write(message)
f.close()
