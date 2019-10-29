# Author : M Mirza Fathan Al Arsyad - IF ITB

# PROGRAM SEGITIGA PASCAL

# Kamus
# N			: integer
# i, j 		: integer
# Pascal    : array[1..N] of array[1..N] of integer
def SegitigaPascal(x, matriks):
	# I.S. x ukuran matriks, seluruh elemen matriks bernilai 1
	# F.S. terbentuk matriks dengan elemen-elemen mengikuti aturan segitiga pascal
	# Kamus Lokal
	# i, j 		: integer
	# Algoritma
	for i in range(x):
		for j in range(x):
			if i!=0 and j!=0:
				matriks[i][j] = matriks[i-1][j] + matriks[i][j-1]

def TulisMatriks(x, matriks):
	# I.S. Matriks berukuran x*x	
	# F.S. Matriks x*x dituliskan ke layar
	# Kamus Lokal
	# i, j 		: integer
	# Algoritma
	for i in range(x):
		for j in range(x):
			print(matriks[i][j], end = " ")
		print("")

# Algoritma

N = int(input("Masukkan N: "))
Pascal = [[1 for i in range(N)] for j in range(N)]
SegitigaPascal(N, Pascal)
TulisMatriks(N, Pascal)