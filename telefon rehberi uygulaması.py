def add_contact():
    name = input("Adı girin: ")
    number = input("Telefon numarasını girin: ")
    with open("rehber.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{number}\n")

def search_contact():
    name = input("Aradığınız kişiyi girin: ")
    with open("rehber.txt", "r", encoding="utf-8") as file:
        for line in file:
            contact = line.strip().split(",")
            if contact[0] == name:
                print(f"Telefon numarası: {contact[1]}")
                return
        print("Kişi bulunamadı.")

def list_contacts():
    with open("rehber.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

while True:
    action = input("Komut (ekle/ara/listele): ").lower()
    if action == "ekle":
        add_contact()
    elif action == "ara":
        search_contact()
    elif action == "listele":
        list_contacts()
    else:
        print("Geçersiz komut!")
