d = 8
p = ''
while (len(p) <= 8) or (p.isupper() == True) or (p.islower() == True):
    p = input()
    if len(p) <= 8:
        print('Недопустимая длина, попробуйте еще раз')
    if (p.isupper() == True) or (p.islower() == True):
        print("Пароль должен содержать как прописные, так и заглавные буквы")

