siswa = [
    {'nim':'A01001', 'name':'Agung Sanjaya', 'jurusan': 'IPA', 'nilai':64},
    {'nim':'A01002', 'name':'Budi Handuk', 'jurusan': 'IPA', 'nilai':73},
    {'nim':'A01003', 'name':'Cici Handika', 'jurusan': 'IPA', 'nilai':58},
]

def menampilkanSiswa():
    print('siswa\n')
    print('Index\t | Nim \t| Name \t| Jurusan \t| Nilai')
    for i in range (len(siswa)):
        print('{}\t| {}\t| {}\t {}\t|{}'.format(i,siswa[i]['nim'],siswa[i]['name'],siswa[i]['jurusan'],siswa[i]['nilai'])) 

def menambahkanSiswa():
    nim = input("Silahkan Masukan NIM Siswa:  ")
    name = input("Silahkan Masukan Nama Siswa:  ")
    jurusan = input("Silahkan Masukan Jurusan Siswa:  ")
    nilai = int(input('Silahkan Masukan Nilai Siswa : '))

    if nim in siswa:
        print("Siswa dengan No NIM ini sudah terdaftar!")
    else:siswa[nim] = {"name siswa" : name, "jurusan siswa" : jurusan, "nilai siswa" : nilai}
    print("Data Siswa telah Tersimpan!")


def updateSiswa():
    nim = input("Silahkan Masukan NIM Siswa yang mau di Update:  ")
    if nim in siswa:
            name = input("Silahkan Masukan Nama Siswa yang mau di Update:  ")
            jurusan = input("Silahkan Masukan Jurusan Siswa:   ")
            siswa[nim] = {"name siswa" : name, "jurusan siswa" : jurusan, "nilai siswa" : nilai}
            print("Data Siswa telah Tersimpan!")
    else:
        print("Data Siswa tidak ditemukan!")
    
def deleteSiswa():
    nim = input("Silahkan Masukan Nama Siswa yang mau di Hapus:  ")
    if nim in siswa:
        del siswa[nim]
        print("Data Siswa telah Terhapus!")
    else:
        print("Data Siswa tidak ditemukan!")

def checkNilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"
    
def checkNilaidanGrade(nim):
    for name in siswa:
        if name["nim"] == nim:
            checkNilaidanGrade = checkNilai(name["nilai"])
            return f"NIM: {siswa['nim']} \nNama:{siswa['name']} \nJurusan:{siswa['jurusan']} \Nilai:{siswa['nilai']}"
        return "NIM tidak ditemukan dalam daftar Nilai!"
    nim_input = input("Masukan NIM:   ")
    print(checkNilaidanGrade(nim_input))

     
while True :
    pilihanMenu = input('''
        Selamat Datang di SMUN 88 Jakarta

        List Menu :
        1. Menampilkan Data Siswa
        2. Menambah Data Siswa
        3. Mengupdate Data Siswa
        4. Menghapus Data Siswa
        5. Mengecek Nilai Siswa
        6. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanSiswa()
    elif(pilihanMenu == '2') :
        menambahkanSiswa()
    elif(pilihanMenu == '3') :
        updateSiswa()
    elif(pilihanMenu == '4') :
        deleteSiswa()
    elif(pilihanMenu == '5') :
        checkNilaidanGrade()
    elif(pilihanMenu == '6') :
        print('Terima kasih! Program Selesai.')
        break
        
    else:
        print('Pilihan tidak sesuai, Silahkan pilih lagi!\n')





