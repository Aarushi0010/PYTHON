list = [0]*26
str = "abbccc"
for s in str:
    if('a'<= s < 'z'):
        list[ord(s) - ord('a')] += 1
flag = True
for j in range(26):
    if list[j]!= 0 and list[j]!= j+1:
        flag = False
        break
if flag == True:
    print("Super ASCII")
else:
    print("Not super ASCII")