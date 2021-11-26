
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=42)

l = Label(f2, text="Welcome to sublime text", font="helvetica 16 bold", fg="red")
l.pack()

BUTTONS
frame = Frame(root, borderwidth=5, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

def hello():
    print("aur btao")

def name():
    print("naam btao")    

b1 = Button(frame, fg="red", text="print now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="print now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="print now")
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="print now")
b4.pack(side=LEFT, padx=23)