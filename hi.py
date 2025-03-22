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
    print(KUNING + "Memuat..." + RESET, end="")
    for _ in range(3):
        print(KUNING + "." + RESET, end="", flush=True)
        time.sleep(0.5)
    print("\n")

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
            subprocess.run(["xdg-open", "https://omcyber.com/cara-menggunakan-termux/"])
            os.system("clear")
        elif pilihan == "2":
            loading_animation()
            subprocess.run(["xdg-open", "https://www.youtube.com/@AriefV"])
            os.system("clear")
        elif pilihan == "3":
            print(KUNING + "Sampai jumpa kembali!" + RESET)
            break
        else:
            print(MERAH + "Pilihan tidak valid. Silakan coba lagi." + RESET)

if __name__ == "__main__":
    sambutan()
    menu()
