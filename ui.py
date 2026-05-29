import customtkinter as ctk

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
        print(f"Button clicked: {value}")

if __name__ == "__main__":
    app = Calc()
    app.mainloop()