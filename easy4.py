nums = [0,1,2,2,3,0,4,2]
i=0
a=[]
b=[]
c=0
while i<len(nums):
    if nums[i]==2:
        a.append('_')
    else:
        b.append(nums[i])
        c=c+1
    i=i+1
d=b+a
print(c)
print(d)
# val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]