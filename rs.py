from tkinter import *
import json, requests



window = Tk() # create window
# window.configure(bg='lightgrey')
window.title("DATA RS")
window.geometry("1080x600")

lbl1 = Label(window, text="Nama RS:", fg='black', font=("Helvetica", 16, "bold"))
lbl2 = Label(window, text="Informasi RS:", fg='black', font=("Helvetica", 16,"bold"))
lbl1.grid(row=0, column=0, sticky=W)
lbl2.grid(row=0, column=1, sticky=W)

frm = Frame(window)
frm.grid(row=1, column=0, sticky=N+S)
window.rowconfigure(1, weight=1)
window.columnconfigure(1, weight=1)

scrollbar = Scrollbar(frm,width=20, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

listNodes = Listbox(frm, width=50, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
listNodes.pack(expand=True, fill=Y)

scrollbar.config(command=listNodes.yview)

listSelection = Listbox(window, height=9, font=("Helvetica", 12))
listSelection.grid(row=1, column=1, sticky=E+W+N)

updata = requests.get("https://data.covid19.go.id/public/api/rs.json")
jason = updata.json()

for x in range(len(jason)):
    listNodes.insert(x,jason[x]['nama'])

# for x in "ABCD":
#     listNodes.insert(END, x)

# for x in "ABCD":
#     listSelection.insert(END, x + ": ?")

def onselect(event):
    w = event.widget
    index = w.index(w.curselection())
    # index = int(w.curselection()[0])
    # value = w.get(index)
    info = jason[index]
    listSelection.delete(0, END)
    listSelection.insert(END, "Nama RS" + "            : " + info['nama'])
    listSelection.insert(END, "Kode RS" + "             : " + info['kode_rs'])
    listSelection.insert(END, "Tempat tidur       : " + str(info['tempat_tidur']))
    listSelection.insert(END, "Nomor Telepon  : " + str(info['telepon']))
    listSelection.insert(END, "Longitude           : " + str(info['lokasi']['lon']))
    listSelection.insert(END, "Latitude              : " + str(info['lokasi']['lat']))
    listSelection.insert(END, "alamat                : " + info['alamat'])
    listSelection.insert(END, "Tipe RS              : " + info['tipe'])
    listSelection.insert(END, "Wilayah RS        : " + info['wilayah'])

listNodes.bind('<<ListboxSelect>>', onselect)

window.mainloop()