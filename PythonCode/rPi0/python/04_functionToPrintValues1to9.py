# Import necessary library
import time

# Create a global variable named val
val=0

# Create a function to change the value of a variable
def changeValue():
    global val
    val+=1
    if val>9:
        val=0 
    return val

# Run the loop 20 times
for i in range(20):
    # Call the function 
    value=changeValue()
    print(value)
    # wait for 2 second
    time.sleep(1)