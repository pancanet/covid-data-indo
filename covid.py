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
tabControl.add(tab2, text ='Total covid')

test1 = Label(tab1)
test2 = Label(tab2)
up_pos = Label(tab1)
up_men = Label(tab1)
up_sem = Label(tab1)
up_act = Label(tab1)
tot_pos = Label(tab2)
tot_men = Label(tab2)
tot_sem = Label(tab2)
tot_act = Label(tab2)
last_update = Label(root)

def COVID():
    def update():
        updata = requests.get("https://data.covid19.go.id/public/api/update.json")
        return updata.json()['update']['penambahan']
        root.after(30000,COVID)
    def total():
        updata = requests.get("https://data.covid19.go.id/public/api/update.json")
        return updata.json()['update']['total']
        root.after(30000,COVID)
    data = update()
    tot = total()    
    test1.config(text="UPDATE HARIAN COVID", font=("Courier",40), fg="blue")
    test2.config(text="TOTAL COVID", font=("Courier",40), fg="blue")
    up_pos.config(text="POSITIF : +" + "{0:n}".format(data['jumlah_positif']), font=("Courier",40), fg="blue")
    up_sem.config(text="SEMBUH : +" + "{0:n}".format(data['jumlah_sembuh']), font=("Courier",40), fg="green")
    up_men.config(text="MENINGGAL : +" + "{0:n}".format(data['jumlah_meninggal']), font=("Courier",40), fg="red")
    if(data['jumlah_dirawat']>0):        
        up_act.config(text="KASUS AKTIF : +" + "{0:n}".format(data['jumlah_dirawat']), font=("Courier",40), fg="red")
    else:
        up_act.config(text="KASUS AKTIF : " + "{0:n}".format(data['jumlah_dirawat']), font=("Courier",40), fg="green")
    tot_pos.config(text="POSITIF : " + "{0:n}".format(tot['jumlah_positif']), font=("Courier",40), fg="blue")
    tot_sem.config(text="SEMBUH : " + "{0:n}".format(tot['jumlah_sembuh']), font=("Courier",40), fg="green")
    tot_men.config(text="MENINGGAL : " + "{0:n}".format(tot['jumlah_meninggal']), font=("Courier",40), fg="red")
    tot_act.config(text="KASUS AKTIF : " + "{0:n}".format(tot['jumlah_dirawat']), font=("Courier",40))
    last_update.config(text="UPDATE TIME : " + data['created'], font=("Courier",20))
    up_pos.pack()
    up_sem.pack()
    up_men.pack()
    up_act.pack()
    tot_pos.pack()
    tot_sem.pack()
    tot_men.pack()
    tot_act.pack()
    last_update.pack()
    tabControl.pack(expand = 1, fill ="both")
    root.after(30000,COVID)

COVID()
root.mainloop()