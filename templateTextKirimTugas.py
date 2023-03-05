import time
import pyperclip
import os

clear = lambda: os.system('cls')
intro_val = 0
nama = ""
npm = ""

current_time_hour = int(time.strftime("%H"))

if (current_time_hour >= 20): # Malam
    waktu = "malam"
elif (current_time_hour >= 16): # Sore
    waktu = "Sore"
elif (current_time_hour >= 10): # Siang
    waktu = "Siang"
else:
    waktu = "Pagi"
    
def intro_func():
    
    global nama
    global npm, intro_val
    
    nama_answ = input(
        """
            TEMPLATE PESAN TUGAS
            
Masukkan Nama Anda: """
    )
    
    npm_answ = input("Masukkan NPM Anda: ")
    
    nama = nama_answ
    npm = npm_answ
    
    clear()
    
    intro_val = 1
    
def main_func(waktu):
    
    if (intro_val != 1):
        intro_func()
    else:
        pass
    
    print(
        """
            TEMPLATE PESAN TUGAS
        
Silahkan Pilih Mata Kuliah:

1. Pemodelan dan Simulasi       5. Keamanan Informasi 
2. Jaringan Komputer            6. Sistem Operasi
3. Pemrograman Web              7. Sistem Informasi
4. Sosioteknologi Informasi     8. Analisa Numerik
                9. Etika Profesi
        """
        )
    mata_kuliah = int(input())
    
    if (mata_kuliah == 1):
        mata_kuliah = "Pemodelan dan Simulasi"
    elif (mata_kuliah == 2):
        mata_kuliah = "Jaringan Komputer"
    elif (mata_kuliah == 3):
        mata_kuliah = "Pemrograman Web"
    elif (mata_kuliah == 4):
        mata_kuliah = "Sosioteknologi Informasi"
    elif (mata_kuliah == 5):
        mata_kuliah = "Keamanan Informasi"
    elif (mata_kuliah == 6):
        mata_kuliah = "Sistem Operasi"
    elif (mata_kuliah == 7):
        mata_kuliah = "Sistem Informasi"
    elif (mata_kuliah == 8):
        mata_kuliah = "Analisa Numberik"
    elif (mata_kuliah == 9):
        mata_kuliah = "Etika Profesi"
    elif (mata_kuliah == 0):
        pass
        
    text = ("""Assalamualaikum Wr.Wb
Selamat {}

Sebelumnya perkenalkan nama saya {} mahasiswa Universitas Siliwangi dari prodi Informatika fakultas Teknik dengan NPM {} kelas D, disini Saya izin untuk mengumpulkan tugas dari mata kuliah {} yaitu [ISI SENDIRI], file tugas akan dilampirkan pada email ini.

Sekian terima kasih
Wassalamualaikum Wr.WB"""
    .format(waktu, nama, npm, mata_kuliah)
    )
    
    pyperclip.copy(text)
    
    clear()
    print("""
            TEMPLATE PESAN TUGAS
            
"{}"
        
Template Berhasil Di-copy pada Clipboard!""".format(text))
    input("")
    
main_func(waktu)