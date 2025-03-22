import subprocess
import time
import os

# Kode warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
RESET = "\033[0m"

def loading_animation():
    putar = ['|', '/', '-', '\\']
    for i in range(20):  # Ubah jumlah iterasi untuk durasi animasi
        print(KUNING + "\rMemuat " + putar[i % len(putar)] + RESET, end="")
        time.sleep(0.1)  # Ubah kecepatan animasi
    print("\r") # Membuat baris baru setelah animasi selesai

def sambutan():
    print(BIRU + "Selamat datang pengunjung situs OmCyber!" + RESET)
    loading_animation()
    nama = input(HIJAU + "Siapa nama Anda? " + RESET)
    loading_animation()
    print(HIJAU + f"Hi {nama}, ada yang bisa saya bantu?" + RESET)

def menu():
    while True:
        print(BIRU + "\nMenu:" + RESET)
        print(MERAH + "1. Baca tutorial Termux" + RESET)
        print(MERAH + "2. Pergi ke YouTube penulis" + RESET)
        print(MERAH + "3. Exit" + RESET)

        pilihan = input(HIJAU + "Masukkan pilihan Anda (1/2/3): " + RESET)

        if pilihan == "1":
            loading_animation()
            subprocess.run(["xdg-open", "https://www.omcyber.net/"])
            os.system("clear")
        elif pilihan == "2":
            loading_animation()
            subprocess.run(["xdg-open", "https://www.youtube.com/"])
            os.system("clear")
        elif pilihan == "3":
            print(KUNING + "Sampai jumpa kembali!" + RESET)
            break
        else:
            print(MERAH + "Pilihan tidak valid. Silakan coba lagi." + RESET)

if __name__ == "__main__":
    os.system("clear")
    sambutan()
    menu()
