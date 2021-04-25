from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
from tkinter import messagebox

root = Tk()
root.title('ToDoList')
root.iconbitmap()
root.geometry('330x360')
root.resizable(False, False)
root.configure(bg='#D3EEEA')

#Define font
my_font = Font(family='Papyrus', size=20, weight='bold')

#Create frame
my_frame = Frame(root)
my_frame.pack(pady=5, padx=5, side=LEFT, expand=True)

#Create listbox
my_list = Listbox(my_frame,font=my_font, width=11, height=10, bg='#ffd6ad',
                  bd=0,  fg='#392f5a',highlightthickness=0, selectbackground='#ffc285',
                  activestyle='none')

my_list.pack(side=TOP, fill=BOTH, expand=True)

#Create dummy list
file_name = 'ToDoList.dat'
input_file = open(file_name, 'rb')
stuff = pickle.load(input_file)

#Add dummy list to list box
for item in stuff:
    my_list.insert(END, item)

#Create scrollbar
my_scrollbar = Scrollbar(root)
my_scrollbar.pack(side=LEFT, fill=BOTH)

#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#create add box
my_entry = Entry(my_frame, font=('Papyrus',24),width=11, bg='#fff8f0')
my_entry.pack(pady=1, side=BOTTOM, expand=True)

#Create a button frame
button_frame = Frame(root, bg='#D3EEEA')
button_frame.pack(pady=1)

#Functions
def delete():
    my_list.delete(ANCHOR)

def add():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross():
    #cross off
    my_list.itemconfig(my_list.curselection(),fg='#fff8f0')
    #get rid off selection bar
    my_list.selection_clear(0, END)

def uncross():
    # cross off
    my_list.itemconfig(my_list.curselection(), fg='#392f5a')
    # get rid off selection bar
    my_list.selection_clear(0, END)

def deleteCross():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, 'fg') == '#fff8f0':
            my_list.delete(my_list.index(count))
        else:
            count += 1

def save_list():
    global file_name
    file_name = 'ToDoList.dat'
    fname = file_name
    if fname == 'ToDoList.dat':
        f = open(fname, 'r')
        f.close()

        #Delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, 'fg') == '#fff8f0':
                my_list.delete(my_list.index(count))
            else:
                count += 1
        #grab all the stuff from the list
        stuff = my_list.get(0, END)

        #Open the file
        output_file = open(file_name, 'wb')

        #Actually add the stuff to the file
        pickle.dump(stuff,output_file)

def clear():
    my_list.delete(0, END)

#Quit and save
def ask_quit():
    save_list()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", ask_quit)

#Add buttons
add_button = Button(button_frame, text='Add', activeforeground='#ff8811', command=add)
delete_button = Button(button_frame, text='Delete', activeforeground='#ff8811', command=delete)
delete_crossed_button = Button(button_frame, text='Delete Crossed', activeforeground='#ff8811', command=deleteCross)
cross_off_button = Button(button_frame, text='Cross', activeforeground='#ff8811', command=cross)
uncross_button = Button(button_frame, text='Uncross', activeforeground='#ff8811', command=uncross)
clear_button = Button(button_frame, text='Clear', activeforeground='#ff8811', command=clear)

add_button.grid(row=0,column=0,padx=10, pady=10, sticky=W)
delete_button.grid(row=1,column=0, padx=10, sticky=W)
delete_crossed_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
cross_off_button.grid(row=3,column=0, padx=10, sticky=W)
uncross_button.grid(row=4,column=0, padx=10, pady=10, sticky=W)
clear_button.grid(row=5,column=0, padx=10, pady=1, sticky=W)

root.mainloop()
