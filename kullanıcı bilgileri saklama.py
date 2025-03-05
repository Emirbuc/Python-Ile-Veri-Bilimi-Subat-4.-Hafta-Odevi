import json

def save_user():
    name = input("Adınızı girin: ")
    surname = input("Soyadınızı girin: ")
    age = input("Yaşınızı girin: ")

    user_data = {"name": name, "surname": surname, "age": age}
    with open("kullanicilar.json", "a", encoding="utf-8") as file:
        json.dump(user_data, file, ensure_ascii=False)
        file.write("\n")

def list_users():
    with open("kullanicilar.json", "r", encoding="utf-8") as file:
        for line in file:
            print(json.loads(line))

save_user()
list_users()
