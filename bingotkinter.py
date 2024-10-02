import tkinter as tk
from functools import partial
from tkinter import messagebox
import random

#จอหลัก
app = tk.Tk()
app.title("Bingo Game")
app.geometry("735x400")
app.resizable(0,0)
btn = tk.Button(app,text="Create a Board",width=20,height=3)
btn["command"] = lambda btn=btn: bingoboard(btn)
btn.place(x=290,y=200)
btn = tk.Button(app,text="Number Randomizer",width=20,height=3)
btn["command"] = lambda btn=btn: numrandom(btn)
btn.place(x=290,y=270)

#เงื่อนไขการชนะ
numlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
possiblelist = []
t1 = []
t2 = []
row = 0
col = 0
for i in range(5):
    col = i
    for j in range(5):
        t1.append(numlist[row])
        t2.append(numlist[col])
        row = row + 1
        col = col + 5
    possiblelist.append(t1)
    possiblelist.append(t2)
    t1 = []
    t2 = []
possiblelist.append([0,6,12,18,24])
possiblelist.append([4,8,12,16,20])
#-------------------------------------------#

#กระดานbinggo
def bingoboard(button):
    app1 = tk.Tk()
    app1.geometry("400x430")
    app1.resizable(0,0)
    app1.title("Bingo Board")
    clickedlst = []
    a = 0
    listofk = []
    random.shuffle(numlist)

#Bingo check
    def Onclick(inlist,app_var,stupidnum):
        if stupidnum in lst:
            #ถ้าหมายเลขตรงให้เปลี่ยนเป็นสีที่ปุ่ม
            listofk[inlist].configure(bg = "#944b31")
            if inlist not in clickedlst:
                clickedlst.append(inlist)
            cnt = 0
            for i in possiblelist:
                for j in i:
                    for k in clickedlst:
                        if(k == j):
                            cnt += 1
                        if(cnt == 5): 
                            messagebox.showwarning("Congratulations!","BINGOOOOOOOOOOOOO!")
                            break
                cnt = 0
#ิgenarate กระดาน
    for i in range(5):
        for j in range(5):
            path  = partial(Onclick,a,app1,numlist[a])
            listofk.append(tk.Button(app1,text=numlist[a], width= 10, height= int(10/2),command=path,))
            listofk[a].grid(row = i, column = j)
            a = a+1
    app1.mainloop()     

#def สุ่มเลข
lst = [] 
def numrandom(button): 
    def generate_number():
        Boo = True
        while(Boo):
            x = random.randint(0,24)
            if x not in lst :
                lst.append(x)
                label.config(text=f"The number is {x}")
                Boo = False
                if len(lst) == 25 :
                    label.config(text=f"The number is {x}\nEND")
            #เเสดงเลขที่สุ่มมาได้
            label1 = tk.Label(app2, text=lst).place(x=35, y=100)

#windowหน้าสุ่มเลข
    app2 = tk.Tk()
    app2.geometry("400x150")
    app2.resizable(0,0)
    app2.title("Number Random")
    label = tk.Label(app2, text="Random")
    label.pack(padx=10, pady=10)
    button = tk.Button(app2, text="สุ่มเลข", command=generate_number)
    button.pack(padx=10, pady=10)
    app2.mainloop()
tk.mainloop()