from cilveks import Produkti
import tkinter as tk
from tkinter import ttk, END


visi_produkti = []


root = tk.Tk()
root.title("Produktu uzskaite")
root.geometry("700x400")

frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

nosaukums_label = ttk.Label(frame, text='Nosaukums')
nosaukums_label.grid(column=0, row=0, sticky='E', **options)

veids_label = ttk.Label(frame, text='Veids')
veids_label.grid(column=0, row=2, sticky='E', **options)

skaits_label = ttk.Label(frame, text='Skaits')
skaits_label.grid(column=0, row=3, sticky='E', **options)

nosaukums = tk.StringVar()
nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

veids = tk.StringVar()
veids_entry = ttk.Entry(frame, textvariable=veids)
veids_entry.grid(column=1, row=2, **options)

skaits = tk.IntVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=3, **options)


def nomainit_sarakstu():
    listbox.delete(0,END)
    for cilveks in visi_produkti:
        listbox.insert("end","{},{},{},{}".format(cilveks.nosaukums,cilveks.veids,cilveks.skirne,cilveks.skaits))

def skirne_ievadit():
    skirne = tk.StringVar()
    skirne_entry = ttk.Entry(frame, textvariable=skirne )
    skirne_entry.grid(column=3, row=0, **options)
    skirne_entry.focus()
    nomainit_sarakstu()
  

skirne_button = ttk.Button(frame, text='Ievadīt šķirni')
skirne_button.grid(column=2, row=0, sticky='W', **options)
skirne_button.configure (command=skirne_ievadit)


def uzskaite_button_clicked():
    produkta_nosaukums = nosaukums.get()
    produkta_veids = veids.get()
    produkta_skaits = skaits.get()
    visi_produkti.append(Produkti(produkta_nosaukums, produkta_veids, produkta_skaits))
    result_label.config(text=visi_produkti[-1].info())
    nomainit_sarakstu()
  

uzskaite_button = ttk.Button(frame, text='Uzskaitīt')
uzskaite_button.grid(column=1, row=4, sticky='W', **options)
uzskaite_button.configure(command=uzskaite_button_clicked)
  

saturs = tk.Variable(value=tuple(visi_produkti))

listbox = tk.Listbox(
    root,
    listvariable=saturs,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.grid(row=5, columnspan=4, **options)

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=4, **options)

frame.grid(padx=10, pady=10)


root.mainloop()