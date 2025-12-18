from tkinter import Tk, Entry, Button, Frame, END
import time
import re

class Calculator2:
    #Creat a window
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("416x760")
        self.root.resizable(False, False)
        self.root.configure(bg="#121111")
        self.root.wm_attributes("-alpha", 0.88880)

        # Input display
        self.display = Entry(
            self.root,
            bg="#1c1b1b",
            fg="white",
            font=("Arial", 45),
            border=0,
            justify="right"
        )
        self.display.pack(fill="x", padx=10, pady=20, ipady=20)

        self.press_time = 0
        self.buttons()
        self.root.mainloop()

    #ALL BUTTONS
    def buttons(self):
        frame = Frame(self.root, bg="#1c1b1b")
        frame.pack(expand=True, fill="both")
        btn_font = ("Arial", 26, "bold")
        btn_padx = 5
        btn_pady = 5
        btn_width = 4
        btn_height = 2

        btn7 = Button(frame, text="7", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("7"))
        btn7.grid(row=0, column=0, padx=btn_padx, pady=btn_pady)

        btn8 = Button(frame, text="8", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("8"))
        btn8.grid(row=0, column=1, padx=btn_padx, pady=btn_pady)

        btn9 = Button(frame, text="9", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("9"))
        btn9.grid(row=0, column=2, padx=btn_padx, pady=btn_pady)

        btn_div = Button(frame, text="/", bg="#966142", fg="black", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("/"))
        btn_div.grid(row=0, column=3, padx=btn_padx, pady=btn_pady)

        btn4 = Button(frame, text="4", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("4"))
        btn4.grid(row=1, column=0, padx=btn_padx, pady=btn_pady)

        btn5 = Button(frame, text="5", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("5"))
        btn5.grid(row=1, column=1, padx=btn_padx, pady=btn_pady)

        btn6 = Button(frame, text="6", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("6"))
        btn6.grid(row=1, column=2, padx=btn_padx, pady=btn_pady)

        btn_mult = Button(frame, text="*", bg="#966142", fg="black", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("*"))
        btn_mult.grid(row=1, column=3, padx=btn_padx, pady=btn_pady)

        btn1 = Button(frame, text="1", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("1"))
        btn1.grid(row=2, column=0, padx=btn_padx, pady=btn_pady)

        btn2 = Button(frame, text="2", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("2"))
        btn2.grid(row=2, column=1, padx=btn_padx, pady=btn_pady)

        btn3 = Button(frame, text="3", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("3"))
        btn3.grid(row=2, column=2, padx=btn_padx, pady=btn_pady)

        btn_minus = Button(frame, text="-", bg="#966142", fg="black", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("-"))
        btn_minus.grid(row=2, column=3, padx=btn_padx, pady=btn_pady)

        # --------------------------->
        btnC = Button(frame, text="C", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height)
        btnC.grid(row=3, column=0, padx=btn_padx, pady=btn_pady)
        btnC.bind("<ButtonPress>", self.start_press)
        btnC.bind("<ButtonRelease>", self.end_press)
        self.press_time = 0

        btn0 = Button(frame, text="0", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("0"))
        btn0.grid(row=3, column=1, padx=btn_padx, pady=btn_pady)

        btn_dot = Button(frame, text=".", bg="#3b3b3b", fg="white", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("."))
        btn_dot.grid(row=3, column=2, padx=btn_padx, pady=btn_pady)

        btn_plus = Button(frame, text="+", bg="#966142", fg="black", font=btn_font, width=btn_width, height=btn_height, command=lambda: self.add_digit("+"))
        btn_plus.grid(row=3, column=3, padx=btn_padx, pady=btn_pady)

        btn_eq = Button(frame, text="=", bg="#966142", fg="black", font=btn_font, width=btn_width*4, height=btn_height, command=self.calculate)
        btn_eq.grid(row=4, column=0, columnspan=4, padx=btn_padx, pady=btn_pady, sticky="nsew")

    # Cleaning logic
    def end_press(self, event):
        elapsed = time.time() - self.press_time
        if elapsed >= 0.5:  # if pressed for more than 0.5 seconds → delete everything
            self.display.delete(0, END)
        else:  # short click → delete last character
            current_text = self.display.get()
            if current_text:
                self.display.delete(len(current_text) - 1, END)

    def start_press(self, event):
        self.press_time = time.time()

    def add_digit(self, digit): #Logic of adding a number
        current = self.display.get() #What is entered reads
        self.display.delete(0, END)
        self.display.insert(0,current + digit)

    def calculate(self):
        expr = self.display.get()

        #Remove spaces
        expr = expr.replace(" ", "")

        #Check: empty string
        if not expr:
            self.display.delete(0, END)
            self.display.insert(0, "")
            return

        #Check: must not end with an operator
        if expr[-1] in "+-*/.":
            self.display.delete(0, END)
            self.display.insert(0, "Error")
            return

        #Checking for duplicate operators (+-, **, //, ++)

        if re.search(r"[\+\-\*/]{2,}", expr):
            self.display.delete(0, END)
            self.display.insert(0, "Error")
            return

        # Division by zero check
        if "/0" in expr:
            self.display.delete(0, END)
            self.display.insert(0, "Error")
            return

        #Do the math
        try:
            result = eval(expr)
            self.display.delete(0, END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, END)
            self.display.insert(0, "Error")



Calculator2()