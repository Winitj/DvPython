"""
aList = [1,2,3]
if len(aList)%2 == 0:
    even_flag = True
else:
    even_flag = False
result = []
for _ in aList:
    if even_flag == True:
        result.append(2)
    if even_flag == False:
        break
"""



aList = [1, 2, 3]

result = [2] * len(aList) if len(aList) % 2 == 0 else []

print(result)

"""

aList = [4, 2, 3]

if ( len(aList) % 2 == 0):
    print(aList)
else:
    print([])
"""