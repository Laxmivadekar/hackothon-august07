root = [1,'null',2,3]  #pre order traversal
i=0
a=[]
b=[]
while i<len(root):
    if root[i]=='null':
        b.append(root[i])
    else:
        a.append(root[i])
    i=i+1
print(a)


# Output: [1,2,3]
