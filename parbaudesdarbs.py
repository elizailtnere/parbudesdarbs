from augliundarzeni import Darzs
import tkinter as tk
from tkinter import ttk

darza_produkti = []

root = tk.Tk()
root.title("Dārza uzskaite")
root.geometry('300x300')

frame = ttk.Frame(root)
options = {'padx': 5, 'pady': 5}


nosaukums_label = ttk.Label(frame, text='Auga nosaukums:')
nosaukums_label.grid(column=0, row=0, sticky='W', **options)

skaits_label = ttk.Label(frame, text='Novākto produktu skaits:')
skaits_label.grid(column=0, row=1, sticky='W', **options)

veids_label = ttk.Label(frame, text='Auglis vai dārzenis:')
veids_label.grid(column=0, row=2, sticky='W', **options)



nosaukums = tk.StringVar()
nosaukums_entry = ttk.Entry(frame, textvariable=nosaukums)
nosaukums_entry.grid(column=1, row=0, **options)
nosaukums_entry.focus()

skaits = tk.StringVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=1, **options)
skaits_entry.focus()

veids = tk.IntVar()
veids_entry = ttk.Entry(frame, textvariable=veids)
veids_entry.grid(column=1, row=2, **options)
veids_entry.focus()

def uzskaitit_button_clicked ():
    produkta_nosaukums = nosaukums.get()
    produkta_skaits = skaits.get()
    produkta_veids = veids.get()
    darza_produkti.append(Darzs(produkta_nosaukums, produkta_skaits, produkta_veids))
    result_label.config(text=darza_produkti[-1].info())
    

uzskaitit_button = ttk.Button(frame, text='Uzskaitīt')
uzskaitit_button.grid(column=2, row=0, sticky='W', **options)
uzskaitit_button.configure(command=uzskaitit_button_clicked)

result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

frame.grid(padx=10, pady=10)

