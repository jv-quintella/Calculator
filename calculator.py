import customtkinter as ctk
import math
from fractions import Fraction

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else: 
        return "Math Error"

def sqrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Math Error"

def square(a):
    return a * a

def percent(a, base=None):
    if base is not None:
        return (a * base) / 100
    else:
        return a / 100

def fraction(a, b=None):
    try:
        if b is not None:
            result = Fraction(a, b)
        else:
            result = Fraction(a)
        return str(result.limit_denominator())
    except ValueError:
        return "Error"

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class Calc(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("320x500")
        self.resizable(False, False)

        self.display = ctk.CTkEntry(self, font=("Segoe UI", 40), justify="right", height=80, border_width=0)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 20), sticky="ew")
        self.display.insert(0, "0")

        self.current_operator = None
        self.stored_value = None
        self.new_input = True

        buttons = [
            ('%', 'CE', 'C', '⌫'),
            ('1/x', 'x²', '√', '÷'),
            ('7', '8', '9', '×'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('+/-', '0', '.', '=')
        ]

        for row_idx, row in enumerate(buttons, start=1):
            self.grid_rowconfigure(row_idx, weight=1)
            
            for col_idx, text in enumerate(row):
                self.grid_columnconfigure(col_idx, weight=1)

                if text == '=':
                    bg_color = "#005A9E" 
                    text_color = "white"
                elif text in ['÷', '×', '-', '+']:
                    bg_color = ("#F3F3F3", "#333333") 
                    text_color = ("black", "white")
                elif row_idx <= 2: 
                    bg_color = ("#F9F9F9", "#323232")
                    text_color = ("black", "white")
                else: 
                    bg_color = ("#FFFFFF", "#3B3B3B")
                    text_color = ("black", "white")

                btn = ctk.CTkButton(
                    self, 
                    text=text, 
                    font=("Segoe UI", 20),
                    fg_color=bg_color,
                    text_color=text_color,
                    hover_color=("#D4D4D4", "#202020"), 
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky="nsew")

    def button_click(self, value):
        current_text = self.display.get()

        if current_text == "Error":
            self.display.delete(0, 'end')
            self.display.insert(0, "0")
            current_text = "0"
            self.new_input = True

        if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            if self.new_input:
                self.display.delete(0, 'end')
                if value == '.':
                    self.display.insert(0, '0.')
                else:
                    self.display.insert(0, value)
                self.new_input = False
            else:
                if value == '.' and '.' in current_text:
                    return
                if current_text == "0" and value != ".":
                    self.display.delete(0, 'end')
                self.display.insert('end', value)

        elif value == 'C':
            self.display.delete(0, 'end')
            self.display.insert(0, '0')
            self.stored_value = None
            self.current_operator = None
            self.new_input = True

        elif value == 'CE':
            self.display.delete(0, 'end')
            self.display.insert(0, '0')
            self.new_input = True

        elif value == '⌫':
            if not self.new_input:
                new_text = current_text[:-1]
                self.display.delete(0, 'end')
                if new_text == "" or new_text == "-":
                    self.display.insert(0, '0')
                    self.new_input = True
                else:
                    self.display.insert(0, new_text)

        elif value in ['+', '-', '×', '÷']:
            try:
                self.stored_value = float(current_text)
            except ValueError:
                self.stored_value = 0.0
            self.current_operator = value
            self.new_input = True

        elif value == '=':
            if self.stored_value is not None and self.current_operator is not None:
                try:
                    current_val = float(current_text)
                    if self.current_operator == '+':
                        res = add(self.stored_value, current_val)
                    elif self.current_operator == '-':
                        res = sub(self.stored_value, current_val)
                    elif self.current_operator == '×':
                        res = prod(self.stored_value, current_val)
                    elif self.current_operator == '÷':
                        res = div(self.stored_value, current_val)
                    
                    self.display.delete(0, 'end')
                    
                    if isinstance(res, float) and res.is_integer():
                        res = int(res)
                        
                    self.display.insert(0, str(res))
                    self.stored_value = None
                    self.current_operator = None
                    self.new_input = True
                except ValueError:
                    self.display.delete(0, 'end')
                    self.display.insert(0, "Error")
                    self.new_input = True

        elif value == '√':
            try:
                res = sqrt(float(current_text))
                if isinstance(res, float) and res.is_integer():
                    res = int(res)
                self.display.delete(0, 'end')
                self.display.insert(0, str(res))
            except ValueError:
                self.display.delete(0, 'end')
                self.display.insert(0, "Error")
            self.new_input = True
            
        elif value == 'x²':
            try:
                res = square(float(current_text))
                if isinstance(res, float) and res.is_integer():
                    res = int(res)
                self.display.delete(0, 'end')
                self.display.insert(0, str(res))
            except ValueError:
                self.display.delete(0, 'end')
                self.display.insert(0, "Error")
            self.new_input = True
            
        elif value == '1/x':
            try:
                res = fraction(float(current_text))
                self.display.delete(0, 'end')
                self.display.insert(0, str(res))
            except ValueError:
                self.display.delete(0, 'end')
                self.display.insert(0, "Error")
            self.new_input = True
            
        elif value == '%':
            try:
                if self.stored_value is not None:
                    res = percent(float(current_text), base=self.stored_value)
                else:
                    res = percent(float(current_text))
                
                if isinstance(res, float) and res.is_integer():
                    res = int(res)
                    
                self.display.delete(0, 'end')
                self.display.insert(0, str(res))
            except ValueError:
                self.display.delete(0, 'end')
                self.display.insert(0, "Error")
            self.new_input = True
            
        elif value == '+/-':
            if current_text != "0" and current_text != "0.":
                if current_text.startswith("-"):
                    self.display.delete(0, 'end')
                    self.display.insert(0, current_text[1:])
                else:
                    self.display.insert(0, "-" + current_text)

if __name__ == "__main__":
    app = Calc()
    app.mainloop()