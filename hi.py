import subprocess
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    print("Memuat...")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def sambutan():
    print("Selamat datang pengunjung situs OmCyber!")
    loading_animation()
    nama = input("Siapa nama Anda? ")
    loading_animation()
    print(f"Hi {nama}, ada yang bisa saya bantu?")

def menu():
    while True:
        print("\nMenu:")
        print("1. Baca tutorial Termux")
        print("2. Pergi ke YouTube penulis")
        print("3. Exit")

        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == "1":
            loading_animation()
            subprocess.run(["xdg-open", "https://www.omcyber.net/"])
            clear_screen()
        elif pilihan == "2":
            loading_animation()
            subprocess.run(["xdg-open", "https://www.youtube.com/"])
            clear_screen()
        elif pilihan == "3":
            print("Sampai jumpa kembali!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    sambutan()
    menu()
