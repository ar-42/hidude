import webbrowser

def sambutan():
    print("Selamat datang pengunjung situs OmCyber!")
    nama = input("Siapa nama Anda? ")
    print(f"Hi {nama}, ada yang bisa saya bantu?")

def menu():
    while True:
        print("\nMenu:")
        print("1. Baca tutorial Termux")
        print("2. Pergi ke YouTube penulis")
        print("3. Exit")

        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == "1":
            webbrowser.open("https://www.omcyber.net/")
        elif pilihan == "2":
            webbrowser.open("https://www.youtube.com/")
        elif pilihan == "3":
            print("Sampai jumpa kembali!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    sambutan()
    menu()
