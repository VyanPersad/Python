from tkinter import *
#We nned to import the backend code to ensure that it can be run when called.
from bookStore_backend import Database

#Instead of linking the class to the db directly it is passed from here to the class.
database = Database("books.db")


def get_selected_row(event):
    global selected_tuple
    #This output is tuple so we have to select only the first element of the tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    #return(selected_tuple)


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    #The element(s) found will be used to populate a list and then inserted
    #to the list box
    for element_found in database.search(title_text.get(), auth_text.get(),
                                         year_text.get(), isbn_text.get()):
        list1.insert(END, element_found)


def add_entry():
    database.insert(title_text.get(), auth_text.get(), year_text.get(),
                    isbn_text.get())
    list1.delete(0, END)
    list1.insert(
        END,
        (title_text.get(), auth_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(selected_tuple[0], title_text.get(), auth_text.get(),
                    year_text.get(), isbn_text.get())


window = Tk()
#Sets the window title.
window.wm_title("BookStore")

#Labels for prog.
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#Entry/input boxes
#This line gets the input as string
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

auth_text = StringVar()
e2 = Entry(window, textvariable=auth_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
#This line specifies the start point of the list1 element, then the
#height and width span of the list1 element.
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
#This one attaches a scrollbar to the list1 element
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#This allows for the element in the listbox to be selcted
#It triggers the get_selected_row method
#For tkinter you don't need to use brackets
list1.bind('<<ListboxSelect>>', get_selected_row)

#Every button has a coomand that triggers a method, no need for brackets.
view_all = Button(window, text="View All", width=12, command=view_command)
view_all.grid(row=2, column=3)

Search = Button(window, text="Search", width=12, command=search_command)
Search.grid(row=3, column=3)

add = Button(window, text="Add Entry", width=12, command=add_entry)
add.grid(row=4, column=3)

update = Button(window, text="Update Entry", width=12, command=update_command)
update.grid(row=5, column=3)

delete = Button(window, text="Delete", width=12, command=delete_command)
delete.grid(row=6, column=3)

close = Button(window, text="Close", width=12, command=window.destroy)
close.grid(row=7, column=3)

window.mainloop()