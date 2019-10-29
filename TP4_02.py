# Author : M Mirza Fathan Al Arsyad - IF ITB
def BacaMatriks(matriks, n, m):
	for i in range(n):
		for j in range(m):
			print("Masukkan nilai A" + "[" + str(i+1) + "]" + "[" + str(j+1) + "]: ", end ="")
			matriks[i][j] = int(input())
def HitungElPositif(matriks, n, m):
	count = 0
	for i in range(n):
		for j in range(m):
			if matriks[i][j] > 0:
				count += 1
	return count
def TulisMatriks(matriks, n, m):
	for i in range(n):
		for j in range(m):
			print(matriks[i][j], end=" ")
		print("")

N = int(input("Masukkan N:"))
M = int(input("Masukkan M:"))
A = [[0 for j in range(M)] for i in range(N)]
BacaMatriks(A, N, M)
print("Ada " + str(HitungElPositif(A, N, M)) + " bilangan positif di matriks.")
TulisMatriks(A, N, M)