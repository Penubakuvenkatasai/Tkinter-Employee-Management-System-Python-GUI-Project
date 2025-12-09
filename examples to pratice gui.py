from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("my windows")
root.configure(bg="white")
f=Frame(root,width=200,height=200,bg="red")
f.grid(row=0,column=0)
f1=Frame(root,width=200,height=200,bg="white")
f.grid(row=0,column=2)
l = Label(root, text="Employee_name", bg="blue", fg="white", font=('Times New Roman', 20))
l.grid(row=0,column=2,pady=10)
# employee id 
l1 = Label(root, text="Employee_Id", bg="red", fg="white", font=('Arial', 15))
l1.grid(row=1, column=0, padx=10, pady=10)
e1 = Entry(root)
e1.grid(row=1, column=1)

# employee phone
l2 = Label(root, text="Employee_Phone", bg="red", fg="white", font=('Arial', 15))
l2.grid(row=2, column=0, padx=10, pady=10)
e2 = Entry(root)
e2.grid(row=2, column=1)

# employee email
l3= Label(root, text="Employee_Email", bg="red", fg="white", font=('Arial', 15))
l3.grid(row=3, column=0, padx=10, pady=10)
e3 = Entry(root)
e3.grid(row=3, column=1)

# Button functions
def save_button():
    print("saved")

def open_button():
    print("opened")

def update_button():
    print("updateed")

def delete_button():
    print("deleted")

# Operation buttons
b1 = Button(root, text="save", command=save_button, width=10)
b1.grid(row=4, column=0, pady=5)

b2 = Button(root, text="open", command=open_button, width=10)
b2.grid(row=4, column=1, pady=5)

b3 = Button(root, text="update", command=update_button, width=10)
b3.grid(row=5, column=0, pady=5)

b4 = Button(root, text="Delete", command=delete_button, width=10)
b4.grid(row=5, column=1, pady=5)

root.mainloop()


















