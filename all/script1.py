#Прочитать файл.
#Найти все строки со словом ERROR (или Failed login).
#Достать из этих строк IP-адреса или логины, чтобы понять, кого пытались взломать.
#Найти подозрительные повторения: если с одного IP или на один логин было больше 3 ошибок за раз — вывести предупреждение "DANGER: Обнаружена попытка подбора пароля!".
ip_errors = {}
with open ("log.txt", "r", encoding="utf-8") as file:
    log = file.read()

    for line in log.split("\n"):

        if "ERROR" in line or "Failed" in line:
            print(f"Обнаружена ошибка {line.strip()}")

            ip = line.split()[-1]

            ip_errors[ip] = ip_errors.get(ip, 0) + 1

print(f"С адреса {ip_errors} атака!")
print("\n______РЕЗУЛЬТАТ АНАЛИЗА______")
for ip in ip_errors:
    count = ip_errors[ip]
    if count >= 3:
        print(f"С адреса {ip} идет атака. Кол-во ошибок: {ip_errors[ip]}")