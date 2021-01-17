#define list
nama_pelanggan =["Nafi","Joko"]
telepon_pelanggan =["08123456789","08987654321"]


#display semalat datang
print("Selamat Datang! ")

#display menu
def show_menu() :
    print("\n")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

 #menu 1 tampil data   
def tampil_data() :
    print("Daftar kontak")
    jumlah_kontak=len(nama_pelanggan)
    for i in range(jumlah_kontak):
        print("Nama: {} \nNo Telepon: {}".format(nama_pelanggan[i], telepon_pelanggan[i]))
    return show_menu()

#menu 2 tambah data
def tambah_data():
    entry=int(input("Jumlah data customer yang akan dimasukkan: "))
    for i in range(entry):
        nama= str(input ("masukkan nama customer: "))
        telepon =str( input ("masukkan nomor HP: "))
        nama_pelanggan.append(nama)
        telepon_pelanggan.append(telepon)
    print("kontak berhasil dimasukkan")
    return show_menu()
    
show_menu()
while 1:
    milih_menu=int(input("Pilih menu (1/2/3) ")) 

    if milih_menu == 1 :
        tampil_data()
    elif milih_menu == 2 :
        tambah_data()
#menu 3 keluar
    elif milih_menu == 3 :
        print("Program selesai, sampai jumpa! ") 
        break
#menu 4 selain 1 2 3
    else :
        print("Menu tidak tersedia" )