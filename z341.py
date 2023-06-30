import json
def register(log, pas):

    with open("reg.json", "r") as f:
        logpass = json.load(f)
    if log in logpass.keys():
        print("логин занят")
    else:
        logpass[str(log)] = str(pas)
        with open("reg.json", "w") as f:
            json.dump(logpass, f)
def login(log,pas):
    with open("reg.json", "r") as f:
        logpass = json.load(f)
    if not log in logpass.keys():
        print("неверный логин")
    else:
        if not pas in logpass:
            print("неверный пароль")
        else:
            print("успешный вход")

while True:
    q1 = input("рег или вх")
    if q1 == "рег":
        log = input("Введите логин: ")
        pas = input("Введите пароль: ")
        register(log,pas)
    elif q1 == "вх":
        log = input("Введите логин: ")
        pas = input("Введите пароль: ")
        login(log,pas)
    else:
        break
