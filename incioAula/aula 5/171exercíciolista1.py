listnumber = ['0', '1', '2', '3', '4']
listcolors = ['red', 'green', 'black', 'blue', 'white']
listnumber100 = ['100', '200', '300', '400', '500']

concatenate = []

for i in range(len(listnumber)):
    concatenate.append(listnumber[i] + listcolors[i] + listnumber100[i])

print(concatenate)

