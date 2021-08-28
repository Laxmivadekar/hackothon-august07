s = "A man, a plan, a canal: Panama"  #valid polindron or not
a=''
i=1
while i<len(s):
    a+=s[-i]
    i=i+1
print(a)
if s==a:
    print('true')
else:
    print('false')
# Output: true
