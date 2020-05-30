
def change(value):
    global test
    test = value

def change2(value):
    global test
    print(test)
    test = value

#print(test)
change(1)
print(test)
change2(5)
print(test)
