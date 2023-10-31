
if __name__ == "__main__":
	nilai = int(input("masukan nilai: "))
	
	if nilai <= 30:
		print('E')
	elif nilai <= 55:
		print('D')
	elif nilai <= 70:
		print('C')
	elif nilai <= 85:
		print('B')
	else:
		print('A')
		
	print('selesai')
