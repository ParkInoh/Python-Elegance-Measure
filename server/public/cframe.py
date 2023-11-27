from tkinter import*
class Calc(Frame):
    def enter(self, label):
        entry = self.entry
        if label == "C":
            entry.delete(0, END)
            entry.insert(0, '0')
        elif label == "=":
            eget = entry.get()
            if eget.isdigit() == FALSE:
                global temp
                for i, c in enumerate(eget):
                    if c.isdigit() == FALSE:
                        temp = eget[i:]
                        break
                result = eval(eget)
            else:
                result = eval(eget + temp)
            ans = str(result)
            entry.delete(0, END)
            entry.insert(END, ans)
        elif entry.get() == "0":
            entry.delete(0, END)
            entry.insert(END, label)
        else:
            entry.insert(END, label)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.entry = Entry(self, width=12, justify=RIGHT)
        self.entry.insert(0, '0')
        self.entry.grid(row=0, column=0, columnspan=5)
        text_list = ['123', '456', '789', '0*C', '+-=']
        for r, text in enumerate(text_list):
            for c, t in enumerate(text):
                btn = Button(self, text=t, width=3, command=(lambda char=t: self.enter(char)))
                btn.grid(row=r+1, column=c)

def my_eval(line):
    return eval(line)

if __name__ == "__main__":

    win = Tk()
    win.title('Calc')
    calc = Calc(win)
    calc.pack()
    win.mainloop()

    # arith = input()
    # print(my_eval(arith))
