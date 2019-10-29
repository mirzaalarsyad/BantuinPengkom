# Author : M Mirza Fathan Al Arsyad - IF ITB
def f(x):
	return (x*x) - (2*x) + 5
def Tulis(a, b):
	for i in range(a, b+1):
		print("f(" + str(i) + ") = " + str(f(i)))
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))
Tulis(A, B)