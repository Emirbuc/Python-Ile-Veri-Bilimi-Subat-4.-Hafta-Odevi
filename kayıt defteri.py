import os

while True:
    action = input("Komut girin (ekle/goruntule/sil): ").lower()
    if action == "ekle":
        note = input("Notunuzu girin: ")
        with open("gunluk.txt", "a", encoding="utf-8") as file:
            file.write(note + "\n")
    elif action == "goruntule":
        with open("gunluk.txt", "r", encoding="utf-8") as file:
            print(file.read())
    elif action == "sil":
        os.remove("gunluk.txt")
        print("Dosya silindi.")
    else:
        print("Geçersiz komut!")
