import os.path

class Mahasiswa(object):
	nim = None
	nama = None
	
def buat_mahasiswa(nim, nama):
	mahasiswa = Mahasiswa()
	mahasiswa.nim = nim
	mahasiswa.nama = nama
	
	return mahasiswa
	
def load_mahasiswa():
	daftar_mahasiswa = []
	
	if not os.path.exists('mahasiswa.txt'):
		return daftar_mahasiswa
		
	with open('mahasiswa.txt', 'r') as f:
		baris = (f.read().split('\n'))
		
		for tiap_baris in baris:
			if tiap_baris == '':
				continue
				
			mahasiswa_split = tiap_baris.split(',')
			daftar_mahasiswa.append(buat_mahasiswa(mahasiswa_split[0], mahasiswa_split[1]))
	return daftar_mahasiswa
	
def simpan_mahasiswa(daftar_mahasiswa):
	text = ''
	
	for mahasiswa in daftar_mahasiswa:
		text += "{},{}\n".format(mahasiswa.nim, mahasiswa.nama)
		
	with open('mahasiswa.txt', 'w') as f:
		f.write(text)
 	
def tampilkan_mahasiswa():
	print('Daftar Mahasiswa')
	print('=======================')		
	print('No\tNim\tNama')
	print('=======================')
	daftar_mahasiswa = load_mahasiswa()
	
	for x in range(len(daftar_mahasiswa)):
		print("{}\t{}\t{}".format(x+1, daftar_mahasiswa[x].nim, daftar_mahasiswa[x].nama))
	print()
	
def tambahkan_mahasiswa():
	nim = input('Masukan Nim: ')
	nama = input('Masukan Nama: ')
	mahasiswa = buat_mahasiswa(nim, nama)
	daftar_mahasiswa = load_mahasiswa()
	daftar_mahasiswa.append(mahasiswa)
	simpan_mahasiswa(daftar_mahasiswa)
#saya coba untuk menambahkan namanya	
def cari_mahasiswa():
	nim = input('Masukan NIM yang di cari: ')
	
	daftar_mahasiswa = load_mahasiswa()
	
	for index in range(len(daftar_mahasiswa)):
		mahasiswa = daftar_mahasiswa[index]
		
		if mahasiswa.nim == nim:
			print('mahasiswa dengan NIM {} dan bernama {} di temukan!'.format(nim, mahasiswa.nama))
			return index
	
	print('mahasiswa dengan NIM {} tidak di temukan'.format(nim))
	return -1
	
def ubah_mahasiswa():
	index = cari_mahasiswa()
	
	if index == -1:
		return
		
	daftar_mahasiswa = load_mahasiswa()
	mahasiswa = daftar_mahasiswa[index]
	print('Silahkan ubah data mahasiswa')
	mahasiswa.nama = input('Masukan nama yang baru: ')
	simpan_mahasiswa(daftar_mahasiswa)
	print()
	
def hapus_mahasiswa():
	index = cari_mahasiswa()
	
	if index == -1:
		return
		
	daftar_mahasiswa = load_mahasiswa()
	del daftar_mahasiswa[index]
	simpan_mahasiswa(daftar_mahasiswa)
	print()
#hanya coba agar lebih menarik	
while True:
	print(' =========================')
	print('| 1. Tampilkan Mahasiswa  |')
	print('| 2. Tambahkan Mahasiswa  |')
	print('| 3. Cari Mahasiswa       |')
	print('| 4. Ubah Mahasiswa       |')
	print('| 5. Hapus Mahasiswa      |')
	print('| 6. Keluar               |')
	print(' =========================')
	pilih_menu = int(input('silahkan pilih menu: '))
	print()
	
	if pilih_menu == 1:
		tampilkan_mahasiswa()
	elif pilih_menu == 2:
		tambahkan_mahasiswa()
	elif pilih_menu == 3:
		cari_mahasiswa()
	elif pilih_menu == 4:
		ubah_mahasiswa()
	elif pilih_menu == 5:
		hapus_mahasiswa()
	elif pilih_menu == 6:
		break
	


