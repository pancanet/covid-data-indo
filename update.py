import json, requests
from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, 'deu_DEU')
root = Tk()
root.title("UPDATE COVID")
test = Label(root)
up_pos = Label(root)
up_men = Label(root)
up_sem = Label(root)
last_update = Label(root)

def COVID():
    def update():
        updata = requests.get("https://data.covid19.go.id/public/api/update.json")
        return updata.json()['update']['penambahan']
        root.after(5000,COVID)
    data = update()
    test.config(text="UPDATE COVID", font=("Courier",40), fg="blue")
    up_pos.config(text="POSITIF : " + "{0:n}".format(data['jumlah_positif']), font=("Courier",40), fg="blue")
    up_sem.config(text="SEMBUH : " + "{0:n}".format(data['jumlah_sembuh']), font=("Courier",40), fg="green")
    up_men.config(text="MENINGGAL : " + "{0:n}".format(data['jumlah_meninggal']), font=("Courier",40), fg="red")
    last_update.config(text="UPDATE TIME : " + data['created'], font=("Courier",40))
    test.pack()
    up_pos.pack()
    up_sem.pack()
    up_men.pack()
    last_update.pack()
    root.after(5000,COVID)

COVID()
root.mainloop()
