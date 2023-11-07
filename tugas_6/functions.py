		

def luas_segitiga_siku():
	bidang_datar = ('segitiga siku')
	
	alas = int(input('masukan alas: '))
	tinggi = int(input('masukan tinggi: '))
	luas = 0.5 * alas * tinggi
	return bidang_datar, luas
	
def luas_persegi():
	bidang_datar = 'persegi'
	
	sisi = int(input('masukan sisi: '))
	luas = sisi **2
	return bidang_datar, luas
	
def luas_lingkaran():
	bidang_datar = 'lingkaran'
	
	r = int(input('masukan jari jari: '))
	pi = 3.14
	luas = pi*r*r
	return bidang_datar, luas
	
if __name__ == "__main__":
	while True:
		print("1. luas segitiga siku")
		print("2. luas persegi")
		print("3. luas lingkaran")
		print("4. keluar")
		pilih_menu = int(input("pilih menu: "))
		
		if pilih_menu == 1:
			hasil = luas_segitiga_siku()
		elif pilih_menu == 2:
			hasil = luas_persegi()
		elif pilih_menu == 3:
			hasil = luas_lingkaran()
		elif pilih_menu == 4:
			break
		
 
		print("luas {} adalah {}". format(hasil[0], hasil[1]))		
		
	
	
