# Author: M Mirza Fathan - IF ITB 2018
N = int(input("Masukkan N: "))
TabInt = [0 for i in range(N)]
for i in range(N):
	TabInt[i] = int(input())
print("Hasil dibalik:")
for i in range(N):
	print(TabInt[N-i-1])