class StringVar:
    string = '123'
    def set(self):
        self.string = str(input("введите изменение в строке: "))
    def get(self):
        print(self.string)

def vyb(v):
    if v == 'set':
        s.set()
        v = ''
        return vyb(v)
    elif v == 'get':
        s.get()
        v = ''
        return vyb(v)
    elif v == '':
        v = input("set or get? ")
        return vyb(v)
    else:
        return


s = StringVar()
v = input("set or get? ")
vyb(v)

