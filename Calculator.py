from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.resizable(0, 0)

e = Entry(root, width=30)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Button Functions
first = None
operator = None

def button_click(num):
	curr = e.get()
	e.delete(0, END)
	e.insert(0, str(curr) + str(num))

def buttonClear():
	e.delete(0, END)
	global first
	first = None

def buttonNeg():
	curr = e.get()
	e.delete(0, END)
	e.insert(0, str(-float(curr)))

def buttonPercent():
	curr = e.get()
	e.delete(0, END)
	e.insert(0, str(float(curr)/100))

def buttonAdd():
	global first
	global operator
	if first != None:
		buttonEqual()
	curr = e.get()
	first = float(curr)
	operator = "+"
	e.delete(0, END)

def buttonSub():
	global first
	global operator
	if first != None:
		buttonEqual()
	curr = e.get()
	first = float(curr)
	operator = "-"
	e.delete(0, END)


def buttonMul():
	global first
	global operator
	if first != None:
		buttonEqual()
	curr = e.get()
	first = float(curr)
	operator = "x"
	e.delete(0, END)

def buttonDiv():
	global first
	global operator
	if first != None:
		buttonEqual()
	curr = e.get()
	first = float(curr)
	operator = "÷"
	e.delete(0, END)


def buttonEqual():
	second = e.get()
	e.delete(0, END)
	global first
	global operator
	if operator == "+":
		e.insert(0, str(float(first) + float(second)))
	elif operator == "-":
		e.insert(0, str(float(first) - float(second)))
	elif operator == "x":
		e.insert(0, str(float(first) * float(second)))
	elif operator == "÷":
		e.insert(0, str(float(first) / float(second)))




# Define Buttons

button1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1), highlightbackground='light grey')
button2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2), highlightbackground='light grey')
button3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3), highlightbackground='light grey')
button4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4), highlightbackground='light grey')
button5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5), highlightbackground='light grey')
button6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6), highlightbackground='light grey')
button7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7), highlightbackground='light grey')
button8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8), highlightbackground='light grey')
button9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9), highlightbackground='light grey')
button0 = Button(root, text="0", padx=68, pady=20, command=lambda: button_click(0), highlightbackground='light grey')
button_add = Button(root, text="+", padx=30, pady=20, command=buttonAdd, highlightbackground='orange')
button_equal = Button(root, text="=", padx=30, pady=20, command=buttonEqual, highlightbackground='orange')
button_clear = Button(root, text="AC", padx=26, pady=20, command=buttonClear, highlightbackground='grey')
button_negative = Button(root, text="+/-", padx=26, pady=20, command=buttonNeg, highlightbackground='grey')
button_percentage = Button(root, text="%", padx=28.5, pady=20, command=buttonPercent, highlightbackground='grey')
button_divide = Button(root, text="÷", padx=30, pady=20, command=buttonDiv, highlightbackground='orange')
button_multiply = Button(root, text="x", padx=31, pady=20, command=buttonMul, highlightbackground='orange')
button_subtract = Button(root, text="-", padx=31, pady=20, command=buttonSub, highlightbackground='orange')
button_decimal = Button(root, text=".", padx=33, pady=20, command=lambda: button_click("."), highlightbackground='light grey')


# Button positions

button_clear.grid(row=1, column=0)
button_negative.grid(row=1, column=1)
button_percentage.grid(row=1, column=2)
button_divide.grid(row=1, column=3)


button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)


button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)


button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button_add.grid(row=4, column=3)


button0.grid(row=5, columnspan=2, column=0)
button_decimal.grid(row=5, column=2)
button_equal.grid(row=5, column=3)




root.mainloop()