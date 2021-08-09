# David Barnes CIS 345 T-Th 12:00 P.M. Assignment 7
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.geometry('411x396')
win.title('Tic Tac Toe')
win.config(background='green')

counter = 0


def link_click_event(event):
    global counter
    if event == shape_one and counter % 2 == 0:
        shape_one.set('X')
        button_one['state'] = DISABLED
    elif event == shape_one and counter % 2 == 1:
        shape_one.set('O')
        button_one['state'] = DISABLED
    elif event == shape_two and counter % 2 == 0:
        shape_two.set('X')
        button_two['state'] = DISABLED
    elif event == shape_two and counter % 2 == 1:
        shape_two.set('O')
        button_two['state'] = DISABLED
    elif event == shape_three and counter % 2 == 0:
        shape_three.set('X')
        button_three['state'] = DISABLED
    elif event == shape_three and counter % 2 == 1:
        shape_three.set('O')
        button_three['state'] = DISABLED
    elif event == shape_four and counter % 2 == 0:
        shape_four.set('X')
        button_four['state'] = DISABLED
    elif event == shape_four and counter % 2 == 1:
        shape_four.set('O')
        button_four['state'] = DISABLED
    elif event == shape_five and counter % 2 == 0:
        shape_five.set('X')
        button_five['state'] = DISABLED
    elif event == shape_five and counter % 2 == 1:
        shape_five.set('O')
        button_five['state'] = DISABLED
    elif event == shape_six and counter % 2 == 0:
        shape_six.set('X')
        button_six['state'] = DISABLED
    elif event == shape_six and counter % 2 == 1:
        shape_six.set('O')
        button_six['state'] = DISABLED
    elif event == shape_seven and counter % 2 == 0:
        shape_seven.set('X')
        button_seven['state'] = DISABLED
    elif event == shape_seven and counter % 2 == 1:
        shape_seven.set('O')
        button_seven['state'] = DISABLED
    elif event == shape_eight and counter % 2 == 0:
        shape_eight.set('X')
        button_eight['state'] = DISABLED
    elif event == shape_eight and counter % 2 == 1:
        shape_eight.set('O')
        button_eight['state'] = DISABLED
    elif event == shape_nine and counter % 2 == 0:
        shape_nine.set('X')
        button_nine['state'] = DISABLED
    elif event == shape_nine and counter % 2 == 1:
        shape_nine.set('O')
        button_nine['state'] = DISABLED
    counter += 1
    check_for_winner()


def check_for_winner():
    if (shape_one.get() == 'X' and shape_two.get() == 'X' and shape_three.get() == 'X') or \
            (shape_one.get() == 'X' and shape_four.get() == 'X' and shape_seven.get() == 'X') or \
            (shape_one.get() == 'X' and shape_five.get() == 'X' and shape_nine.get() == 'X') or \
            (shape_two.get() == 'X' and shape_five.get() == 'X' and shape_eight.get() == 'X') or \
            (shape_three.get() == 'X' and shape_six.get() == 'X' and shape_nine.get() == 'X') or \
            (shape_three.get() == 'X' and shape_five.get() == 'X' and shape_seven.get() == 'X') or \
            (shape_four.get() == 'X' and shape_five.get() == 'X' and shape_six.get() == 'X') or \
            (shape_seven.get() == 'X' and shape_eight.get() == 'X' and shape_nine.get() == 'X'):
        messagebox.showinfo(title='Victory', message='Player 1 wins!')
    elif (shape_one.get() == 'O' and shape_two.get() == 'O' and shape_three.get() == 'O') or \
            (shape_one.get() == 'O' and shape_four.get() == 'O' and shape_seven.get() == 'O') or \
            (shape_one.get() == 'O' and shape_five.get() == 'O' and shape_nine.get() == 'O') or \
            (shape_two.get() == 'O' and shape_five.get() == 'O' and shape_eight.get() == 'O') or \
            (shape_three.get() == 'O' and shape_six.get() == 'O' and shape_nine.get() == 'O') or \
            (shape_three.get() == 'O' and shape_five.get() == 'O' and shape_seven.get() == 'O') or \
            (shape_four.get() == 'O' and shape_five.get() == 'O' and shape_six.get() == 'O') or \
            (shape_seven.get() == 'O' and shape_eight.get() == 'O' and shape_nine.get() == 'O'):
        messagebox.showinfo(title='Victory', message='Player 2 wins!')
    elif counter == 9:
        messagebox.showinfo(title='Draw', message='Cats Game')
    else:
        return 'break'

    clear_board()


def clear_board():
    global counter
    shape_one.set('')
    button_one['state'] = NORMAL
    shape_two.set('')
    button_two['state'] = NORMAL
    shape_three.set('')
    button_three['state'] = NORMAL
    shape_four.set('')
    button_four['state'] = NORMAL
    shape_five.set('')
    button_five['state'] = NORMAL
    shape_six.set('')
    button_six['state'] = NORMAL
    shape_seven.set('')
    button_seven['state'] = NORMAL
    shape_eight.set('')
    button_eight['state'] = NORMAL
    shape_nine.set('')
    button_nine['state'] = NORMAL
    counter = 0


# Row 1 buttons

shape_one = StringVar()
button_one = Button(win, textvariable=shape_one, width=3, font=0, command=lambda: link_click_event(shape_one))
button_one.grid(row=1, column=0, ipadx=50, ipady=50)

shape_two = StringVar()
button_two = Button(win, textvariable=shape_two, width=3, font=0, command=lambda: link_click_event(shape_two))
button_two.grid(row=1, column=1, ipadx=50, ipady=50)

shape_three = StringVar()
button_three = Button(win, textvariable=shape_three, width=3, font=0, command=lambda: link_click_event(shape_three))
button_three.grid(row=1, column=2, ipadx=50, ipady=50)

# Row 2 buttons

shape_four = StringVar()
button_four = Button(win, textvariable=shape_four, width=3, font=0, command=lambda: link_click_event(shape_four))
button_four.grid(row=2, column=0, ipadx=50, ipady=50)

shape_five = StringVar()
button_five = Button(win, textvariable=shape_five, width=3, font=0, command=lambda: link_click_event(shape_five))
button_five.grid(row=2, column=1, ipadx=50, ipady=50)

shape_six = StringVar()
button_six = Button(win, textvariable=shape_six, width=3, font=0, command=lambda: link_click_event(shape_six))
button_six.grid(row=2, column=2, ipadx=50, ipady=50)

# Row 3 buttons

shape_seven = StringVar()
button_seven = Button(win, textvariable=shape_seven, width=3, font=0, command=lambda: link_click_event(shape_seven))
button_seven.grid(row=3, column=0, ipadx=50, ipady=50)

shape_eight = StringVar()
button_eight = Button(win, textvariable=shape_eight, width=3, font=0, command=lambda: link_click_event(shape_eight))
button_eight.grid(row=3, column=1, ipadx=50, ipady=50)

shape_nine = StringVar()
button_nine = Button(win, textvariable=shape_nine, width=3, font=0, command=lambda: link_click_event(shape_nine))
button_nine.grid(row=3, column=2, ipadx=50, ipady=50)

win.mainloop()
