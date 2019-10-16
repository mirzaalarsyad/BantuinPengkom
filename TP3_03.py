# Author : M Mirza Fathan IF ITB 2018
inputString = input("Masukkan string: ")
i = 0
palindrom = True
length = len(inputString)
while (i<length and palindrom):
	if inputString[i] != inputString[length-i-1]:
		palindrom = False
	i+=1
if palindrom:
	print(inputString, "adalah palindrom")
else:
	print(inputString, "bukan palindrom")