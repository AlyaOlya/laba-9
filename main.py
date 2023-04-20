import csv
import os
from PIL import Image

def z1():
    i = 'C:/Users/olya/PycharmProjects/pythonProject1/1'

    if not os.path.exists('C:/Users/olya/PycharmProjects/pythonProject1/2list'):
        os.mkdir('C:/Users/olya/PycharmProjects/pythonProject1/2list')

    for f in os.listdir(i):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            im = Image.open(os.path.join(i,f))
            im = im.resize((250, 250))
            im.save(os.path.join('C:/Users/olya/PycharmProjects/pythonProject1/2list', f))
def z2():
    with open("data.csv") as f:
        t_readed = csv.reader(f, delimiter = ",")

        c = 0
        print("Нужно купить")

        for row in t_readed:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            c += 1


z1()