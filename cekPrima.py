x = int(input())

hitungFaktor = 0; #variabel untuk menyimpan jumlah pembagi dari x

for i in range(1,x+1): #pengulangan dari 1 sampai x. 
	if(x%i == 0):	#jika i habis membagi x artinya i faktor dari x
		hitungFaktor = hitungFaktor + 1 # tambahkan jumlah pembagi dari x karena i merupakan faktor dari x

if(hitungFaktor == 2):
	print("Bilangan" + x + "bersifat prima.")
else:
	print("Bilangan" + x + "tidak prima.")

#karena bilangan prima hanya punya dua faktor.
