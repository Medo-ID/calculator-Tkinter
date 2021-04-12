from tkinter import *

tk = Tk()
tk.title('Calculator')

e = Entry(tk, width=40, borderwidth=10, font='Times 14')
e.grid(row=0, column=0, columnspan=4)


def click_btn(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def add_btn():
    first_number = e.get()
    global f_num
    global operation
    operation = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def sub_btn():
    first_number = e.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def mul_btn():
    first_number = e.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def div_btn():
    first_number = e.get()
    global f_num
    global operation
    operation = "division"
    f_num = int(first_number)
    e.delete(0, END)


def clear_btn():
    e.delete(0, END)


def equal_btn():
    second_number = e.get()
    e.delete(0, END)

    if operation == "addition":
        e.insert(0, f_num + int(second_number))
    elif operation == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif operation == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif operation == "division":
        e.insert(0, f_num / int(second_number))


b9 = Button(tk, text='9', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(9))
b9.grid(row=1, column=0)

b8 = Button(tk, text='8', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(8))
b8.grid(row=1, column=1)

b7 = Button(tk, text='7', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(7))
b7.grid(row=1, column=2)

b6 = Button(tk, text='6', width=9, height=4, font='Helvetica 14 ', bg='#B2B2B2', fg='black', command=lambda: click_btn(6))
b6.grid(row=2, column=0)

b5 = Button(tk, text='5', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(5))
b5.grid(row=2, column=1)

b4 = Button(tk, text='4', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(4))
b4.grid(row=2, column=2)

b3 = Button(tk, text='3', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(3))
b3.grid(row=3, column=0)

b2 = Button(tk, text='2', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(2))
b2.grid(row=3, column=1)

b1 = Button(tk, text='1', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(1))
b1.grid(row=3, column=2)

b0 = Button(tk, text='0', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=lambda: click_btn(0))
b0.grid(row=4, column=0)

b_add = Button(tk, text='+', width=9, height=4, font='Helvetica 14', bg='#10C54A', fg='black', command=add_btn)
b_add.grid(row=4, column=3)

b_sub = Button(tk, text='−', width=9, height=4, font='Helvetica 14', bg='#10C54A', fg='black', command=sub_btn)
b_sub.grid(row=3, column=3)

b_mul = Button(tk, text='×', width=9, height=4, font='Helvetica 14', bg='#10C54A', fg='black', command=mul_btn)
b_mul.grid(row=2, column=3)

b_div = Button(tk, text='÷', width=9, height=4, font='Helvetica 14', bg='#10C54A', fg='black', command=div_btn)
b_div.grid(row=1, column=3)

b_clear = Button(tk, text='clear', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=clear_btn)
b_clear.grid(row=4, column=1)

b_equal = Button(tk, text='=', width=9, height=4, font='Helvetica 14', bg='#B2B2B2', fg='black', command=equal_btn)
b_equal.grid(row=4, column=2)

tk.mainloop()