with open("ogrenciler.txt", "a", encoding="utf-8") as file:
    while True:
        name = input("Öğrenci ismi girin (bitti ile çıkın): ")
        if name.lower() == "bitti":
            break
        file.write(name + "\n")

def yazdir():
    with open("ogrenciler.txt", "r", encoding="utf-8") as file:
        print(file.read())

yazdir()
