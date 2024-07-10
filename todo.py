import tkinter as tk
import pickle
from tkinter import filedialog

window=tk.Tk()
window.geometry("400x300")
frame=tk.Frame(window)
frame.pack()
list_box=tk.Listbox(frame,font=('Times',12,'normal'),width=25,height=5,highlightthickness='0',activestyle='none')
list_box.pack(ipadx=50,side=tk.LEFT,fill=tk.BOTH)
#create dummy list
#stuff=["take a nap","study for 1hr","walk the dog","play a guitar"]
#add dummy list to list box
#for item in stuff:
#    list_box.insert(tk.END,item)
#create scrollbar
scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
#add srollbar
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)
#create entry button to ass items in the list
entry=tk.Entry(window)
entry.pack(ipadx=60,pady=20)
#create a button frame
btn_frame=tk.Frame(window)
btn_frame.pack(pady=20)

#functions
def delete():
    list_box.delete(tk.ANCHOR)

def add():
    list_box.insert(tk.END,entry.get())
    entry.delete(0,tk.END)

def cross_off():
    #cross of the item
    list_box.itemconfig(list_box.curselection(),fg='#dedede')
    #clear the selection bar
    list_box.selection_clear(0,tk.END)
def uncross_off():
    #cross of the item
    list_box.itemconfig(list_box.curselection(),fg='#000000')
    #clear the selection bar
    list_box.selection_clear(0,tk.END)
def del_cross_off():
    count=0
    while count < list_box.size():
        if(list_box.itemcget(count,"fg")=='#dedede'):
            list_box.delete(list_box.index(count))
        else:
            count+=1

def save_fil():
    file_name=filedialog.asksaveasfilename(initialdir="C:\\Users\\dnrao\\OneDrive\\Desktop\\C\\data",
                                       title="SAVE FILE",
                                       filetypes=[("text files","*.txt"),("all files","*.*")])
    if file_name:
        if file_name.endswith(".txt"):
            pass
        else:
            file_name=f'{file_name}.txt'
        count=0
        #delete the crossed off items before saving
        while count < list_box.size():
            if(list_box.itemcget(count,"fg")=='#dedede'):
                list_box.delete(list_box.index(count))
            else:
                count+=1
    #writes the data from list_box to the saving file
    stuff=list_box.get(0,tk.END)
    #open the file
    output_file=open(file_name,"wb")
    pickle.dump(stuff,output_file)
    
def open_fil():
    file_name=filedialog.askopenfilename(initialdir="C:\\Users\\dnrao\\OneDrive\\Desktop\\C\\data",
                                       title="SAVE FILE",
                                       filetypes=[("text files","*.txt"),("all files","*.*")])
    if file_name:
        #delete the currently running data
        list_box.delete(0,tk.END)
        #dump the data from saving file to list_box
        #open the file
        input_file=open(file_name,'rb')
        # load the data
        stuff=pickle.load(input_file)
        for item in stuff:
            list_box.insert(tk.END,item)
def drop_fil():
    list_box.delete(0,tk.END)

#create menus
my_menu=tk.Menu(window)
window.config(menu=my_menu)
#add items to the menu
file_menu=tk.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="file",menu=file_menu)
#add drop down items
file_menu.add_command(label="Save",command=save_fil)
file_menu.add_command(label="Open",command=open_fil)
file_menu.add_separator()
file_menu.add_command(label="Drop",command=drop_fil)
#create buttons
btn_del=tk.Button(btn_frame,text="DELETE",command=delete)
btn_add=tk.Button(btn_frame,text="ADD",command=add)
btn_cross=tk.Button(btn_frame,text="CROSS OFF",command=cross_off)
btn_uncross=tk.Button(btn_frame,text="UNCROSS OFF",command=uncross_off)
btn_cross_del=tk.Button(btn_frame,text="DELETE CROSS OFF",command=del_cross_off)

btn_del.grid(row=0,column=0)
btn_add.grid(row=0,column=1,padx=5)
btn_cross.grid(row=0,column=2,padx=5)
btn_uncross.grid(row=0,column=3,padx=5)
btn_cross_del.grid(row=0,column=4)
window.mainloop()