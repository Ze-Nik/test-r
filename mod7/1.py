import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://mfd.ru/currency/?currency=USD&from=01.07.2023&till=08.07.2023')
soap = BeautifulSoup(page.text, 'html.parser')

infs = soap.find_all(class_="mfd-table mfd-currency-table")
for inf in infs:
    rows = inf.findAll('td')
del rows[2::3]
t = [row.text for row in rows]
p = []
for i in range(len(t)):
    t[i] = t[i].replace("с ", "")
    if i % 2 == 1:
        p.append(t[i])
del t[1::2]
t = list(reversed(t))
p = list(reversed(p))
for i in range(len(t)):
    t[i] = int(t[i][:2])
for i in range(len(p)):
    p[i] = float(p[i])
print(t, p)
plt.plot(t, p)
plt.show()