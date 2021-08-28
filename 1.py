a = [1,'null',3,2,4,'null',5,6]
# i=0
# b=[]
# # c=0
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#     else:
#         c=a.index(a[i])
#         print(c)
#     i=i+1
# print(b)

# Output: [[1],[3,2,4],[5,6]]
i=0
b=[]
while i<len(a):
    if a[i]=='null':
        c=a.index(a[i])
        b.append(c)
    i=i+1
print(b)