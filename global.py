''''a=10
def display():
    # global ad
    a=5
    # a=a+1
    print(a)
display()
print(a)'''''

a='deekshitha'
def display():
    global a
    a=a+'reddy'
print(a,'local')
display()
print(a,'global')

