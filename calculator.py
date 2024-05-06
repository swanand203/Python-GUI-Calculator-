import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x520")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=20)
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3),
            ("sqrt", 6, 0), ("pow", 6, 1), ("x^y", 6, 2), ("clear", 6, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, text):
        if text == "clear":
            self.result_var.set("")
        elif text == "=":
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

        # Trigonometric functions
        if text == "sin":
            self.result_var.set(math.sin(math.radians(float(self.result_var.get()))))
        elif text == "cos":
            self.result_var.set(math.cos(math.radians(float(self.result_var.get()))))
        elif text == "tan":
            self.result_var.set(math.tan(math.radians(float(self.result_var.get()))))

        # Logarithmic functions
        elif text == "log":
            self.result_var.set(math.log10(float(self.result_var.get())))

        # Square root
        elif text == "sqrt":
            self.result_var.set(math.sqrt(float(self.result_var.get())))

        # Power
        elif text == "pow":
            self.result_var.set(float(self.result_var.get()) ** 2)

        # Exponential functions
        elif text == "x^y":
            self.result_var.set(math.exp(float(self.result_var.get())))

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
