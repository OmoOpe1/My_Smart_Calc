from tkinter import *

root = Tk()
root.title('Smart Calculator')
root.config(bg='purple')
root.geometry('680x486+100+100')
entryField = Entry(root, font=('Verdana', 20, 'bold'), bg='purple', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage)
logoLabel.grid(row=0, column=0)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", 
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!"]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='purple', fg='white', font=('Verdana', 18, 'bold'), activebackground='purple')
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()