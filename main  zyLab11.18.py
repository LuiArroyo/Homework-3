# Luis Arroyo
# PSID: 2037081
# CIS 2348

numberlist = []
numberlist = [int(item) for item in input("").split()]
numberlist.sort()
for f in range(0,len(numberlist)):
    if(numberlist[f]>=0):
        print(numberlist[f],end=" ")