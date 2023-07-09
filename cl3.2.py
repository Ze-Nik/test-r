import json


class Model():
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        s = dir(Model)
        a = {}
        for i in range(len(s)):
            a[str(s[i])] = str(getattr(Model, s[i]))
        with open("s.json", "w") as f:
            json.dump(a, f)


k = Model()
k.save()
