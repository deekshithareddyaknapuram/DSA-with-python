list1=['hi','hello','welcome']
names=['deeksh','sathwik','ram']
for items in list1:
    for name in names:
        print(items,name)
        if items=='hi' and name=='deeksh':
            break
print('out everyone')        
