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

    def button_click(self, value):
        pass

if __name__ == "__main__":
    app = Calc()
    app.mainloop()