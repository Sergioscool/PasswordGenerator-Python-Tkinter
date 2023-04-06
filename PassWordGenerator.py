from tkinter import*
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import pyperclip

window = ThemedTk(theme='plastik')
window.title("PassWordGenerator")
window.geometry('500x100')
window.configure(themebg="ubuntu")
lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
medium= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

password = ""
def copy():
    txt=txtpassword.get()
    pyperclip.copy(txt)
def Generate():
    global list
    global password
    global combo
    password = ""
    length = combo.get()
    radiobutton.get()
    list = 0
    if radiobutton.get() == 'Low':
        list = lower
    elif radiobutton.get() == "Medium":
        list = medium
    elif radiobutton.get() == "Strong":
        list = upper
    for i in range(int(length)):
        charact = random.choice(list)
        password += charact
    txtpassword.delete(0, END)
    txtpassword.insert(0,password)

def Encrypt():
    global list , txtpassword
    Key = 25
    encryption = ""
    passgogogo = txtpassword.get()
    index2 = 0
    for i in range(0, len(passgogogo)):
        char = passgogogo[i]
        for i2 in range(0,len(list)):
            if char == list[i2]:
                if i > 0:
                    for i3 in range(0, len(list)):
                        if passgogogo[i-1] == list[i3]:
                            index2 = i3
                else:
                    index2 = 0
                index = ((i2 + Key)+ index2) % len(list)
                encryption = encryption + list [index]
    txtencrypt.delete(0 , END)
    txtencrypt.insert(0, encryption)

passwordLabel = ttk.Label(window, text="Password", font=("Classic", 15), cursor="spraycan")
passwordLabel.place(x=5, y=5)


lengthLabel = ttk.Label(window, text="Length", font=("Classic", 15), cursor="spraycan")
lengthLabel.place(x=5, y=35)


EncryptLabel = ttk.Label(window, text="Encrypt", font=("Classic", 15), cursor="spraycan")
EncryptLabel.place(x=5, y=65)


txtpassword=Entry(window,fg="black",bg="white",width=15,font=("Aqua",15))
txtpassword.place(x=120,y=5)

butcopy= ttk.Button(window, text="Copy", cursor="exchange",command=copy)
butcopy.place(x=300, y=5,width=80,height=26)

butcopy2 = ttk.Button(window, text="Copy", cursor="exchange",command=copy)
butcopy2.place(x=300, y=65,width=80,height=26)

butGenerate= ttk.Button(window, text="Generate", cursor="exchange", command = Generate)
butGenerate.place(x=400, y=5,width=80,height=26)

combo = ttk.Combobox(window)

combo['values'] = (4,6,8,10,12)

combo.current(2)

combo.place(x=120,y=35,width=170)

radiobutton = StringVar()
radiobutton1 = Radiobutton(window,text="Low",value="Low",variable=radiobutton)
radiobutton1.place(x=300,y=35)
radiobutton2 = Radiobutton(window,text="Medium",value="Medium",variable=radiobutton)
radiobutton2.place(x=347,y=35)
radiobutton3 = Radiobutton(window,text="Strong",value="Strong",variable=radiobutton)
radiobutton3.place(x=415,y=35)

txtencrypt=Entry(window,fg="black",bg="white",width=15,font=("Aqua",15))
txtencrypt.place(x=120,y=65)

butencrypt= ttk.Button(window, text="Encrypt", cursor="exchange",command=Encrypt)
butencrypt.place(x=400, y=65,width=80,height=26)
window.mainloop()