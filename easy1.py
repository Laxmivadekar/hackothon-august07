num= [2,7,11,15] #target = 9
i=0
a=[]
sum=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]+num[j]==9:
            if i not in a:
                a.append(i)
                a.append(j)
                sum=num[i]+num[j]
        j=j+1
    i=i+1
print(sum)
print(a)

# print(a)
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

