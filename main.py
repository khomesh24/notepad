from tkinter import *
from tkinter import messagebox,filedialog,simpledialog

def savefun():
    textbox_content =str(textbox.get("1.0","end-1c"))
    fsave = filedialog.asksaveasfile("w",defaultextension ='.txt')
    fsave.write(textbox_content)
    print("save")
    fsave.close()

def openfun():
    fopen = filedialog.askopenfile()
    textbox.insert("1.0",fopen.read())
    print("open")
    fopen.close()


if __name__ == '__main__':

    main = Tk()
    main.geometry("500x500")
    main.title("Notepad")

    #save button
    savebtn = Button(main , text= "Save" , command = savefun)
    savebtn.place(x=100 , y = 10)

    #open button
    openbtn = Button(main , text= "Open" , command = openfun)
    openbtn.place(x=10 , y = 10)

    textbox = Text(main , padx = 5 , pady = 5 , height = 450 , width  = 450)
    textbox.place(x = 0 , y = 40)



    main.mainloop()