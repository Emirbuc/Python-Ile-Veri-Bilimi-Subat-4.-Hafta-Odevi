import time
from datetime import datetime

def log_system():
    while True:
        with open("log.txt", "a", encoding="utf-8") as file:
            log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Sistem çalıştı: {log_time}\n")
        time.sleep(10)

def view_logs():
    with open("log.txt", "r", encoding="utf-8") as file:
        print(file.read())

# Bu fonksiyonu arka planda çalıştırabilirsiniz.
# view_logs() komutuyla logları görüntüleyebilirsiniz.
