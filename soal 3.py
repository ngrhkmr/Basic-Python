#Asignment 1 soal 3

up = input("Masukkan nilai ujian praktek (range 0-100): ")
ut =  input("Masukkan nilai ujian teori (range (0-100)): " )

ujian_praktek= float (up) 
ujian_teori= float (ut) 

if ujian_praktek >=70 and ujian_teori >=70:
    print("Selamat, anda lulus!")
elif ujian_teori >=70 and ujian_praktek <70:
    print("Anda harus mengulang ujian praktek")
elif ujian_teori <70 and ujian_praktek >=70:
    print("Anda harus mengulang ujian teori")
else: print("Anda harus mengulang ujian teori dan praktek")

