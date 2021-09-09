import json, requests
from tkinter import *
import locale          
from tkinter import ttk       

locale.setlocale(locale.LC_ALL, 'deu_DEU')
root = Tk()
root.title("UPDATE COVID")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Update Harian')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text ='Total Vaksinasi')

test1 = Label(tab1)
test2 = Label(tab2)
up_vak1 = Label(tab1)
up_vak2 = Label(tab1)
tot_vak1 = Label(tab2)
tot_vak2 = Label(tab2)
last_update = Label(root)

def COVID():
    def update():
        updata = requests.get("https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json")
        return updata.json()['vaksinasi']['penambahan']
        root.after(30000,COVID)
    def total():
        updata = requests.get("https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json")
        return updata.json()['vaksinasi']['total']
        root.after(30000,COVID)
    data = update()
    tot = total()
    test1.config(text="UPDATE VAKSIN COVID", font=("Courier",40), fg="blue")
    test2.config(text="TOTAL VAKSIN COVID", font=("Courier",40), fg="blue")
    up_vak1.config(text="VAKSINASI 1 : +" + "{0:n}".format(data['jumlah_vaksinasi_1']), font=("Courier",40), fg="blue")
    up_vak2.config(text="VAKSINASI 2 : +" + "{0:n}".format(data['jumlah_vaksinasi_2']), font=("Courier",40), fg="green")
    tot_vak1.config(text="VAKSINASI 1 : " + "{0:n}".format(tot['jumlah_vaksinasi_1']), font=("Courier",40), fg="blue")
    tot_vak2.config(text="VAKSINASI 2 : " + "{0:n}".format(tot['jumlah_vaksinasi_2']), font=("Courier",40), fg="green")
    last_update.config(text="UPDATE TIME : " + data['created'], font=("Courier",20))
    test1.pack()
    test2.pack()
    up_vak1.pack()
    up_vak2.pack()
    tot_vak1.pack()
    tot_vak2.pack()
    last_update.pack()
    tabControl.pack(expand = 1, fill ="both")
    root.after(30000,COVID)

COVID()
root.mainloop()