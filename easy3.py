strs = ["flower","flow","flight"]
i=0
a=''
b=''
while i<=1:
    j=0
    while j<len(strs):
        if i==0:
            if strs[j][i]=='f':
               a='f'
        elif i==1:
            if strs[j][i]=='l':
               b='l'
        j=j+1
    i=i+1
c=a+b
print(c)