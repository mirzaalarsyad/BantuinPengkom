# Author : M Mirza Fathan IF ITB 2018
A = [0 for i in range(10)]
B = [0 for i in range(10)]
tabFrekuensi = [0 for i in range(11)]
nA = int(input("Masukkan banyaknya elemen A: "))
for i in range(nA):
	print("Masukkan elemen A ke-" + str(i+1) + ": ", end="")
	A[i] = int(input())
nB = int(input("Masukkan banyaknya elemen B: "))
for i in range(nB):
	print("Masukkan elemen B ke-" + str(i+1) + ": ", end="")
	B[i] = int(input())
for i in range(11):
	for j in range(nA):
		if i == A[j] :
			tabFrekuensi[i]+=1
Anagram = True
i = 0
while(Anagram and i<11):
	countElmt = 0
	for j in range(nB):
		if i == B[j]:
			countElmt+=1
	if tabFrekuensi[i] != countElmt:
		Anagram = False
	i+=1

if Anagram:
	print("A adalah anagram dari B")
else:
	print("A bukan anagram dari B")