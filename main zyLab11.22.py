# Luis Arroyo
# PSID: 2037081
# CIS 2348

data = input().split()
for frequency in data:
    count = 0
    for f in data:
        if frequency == f:
            count += 1
    print(frequency, count)