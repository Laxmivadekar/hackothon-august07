s = "PAYPALISHIRING"   #numRows = 3
r=0
while r<=2:
    c=0
    a=r
    while c<=6:
        if r==0:
            print(s[a],'',end='')
            a=a+3
        elif r==1:
            print(s[a],end='')
            a=a+2
        elif r==2:
            print(s[a],end=' ')
            a=a+3
        c=c+1
    r=r+1
    print()
        
        
        
        
















# Output: "PAHNAPLSIIGYIR
# P   A   H   N
# A P L S I I G
# Y   I   R