digits = [1,2,3]  #one plus
a=digits[-1]+1
digits.remove(3)
digits.insert(2,a)
print(digits)
# Output: [1,2,4]