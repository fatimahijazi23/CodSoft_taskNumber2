import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="white")

        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(pady=20)

        font_settings = ("Arial", 16)
        button_settings = {"bg": "pink", "activebackground": "lightpink"}
        calculate_button_settings = {"bg": "lightgreen", "activebackground": "palegreen"}

        self.num1_label = tk.Label(self.frame, text="Number 1:", font=font_settings, bg="white")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(self.frame, font=font_settings, width=10)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(self.frame, text="Number 2:", font=font_settings, bg="white")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(self.frame, font=font_settings, width=10)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.operation_label = tk.Label(self.frame, text="Choose Operation:", font=font_settings, bg="white")
        self.operation_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.operation = None

        self.add_button = tk.Button(self.frame, text="+", font=font_settings, command=lambda: self.set_operation('+'), width=5, **button_settings)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)
        self.subtract_button = tk.Button(self.frame, text="-", font=font_settings, command=lambda: self.set_operation('-'), width=5, **button_settings)
        self.subtract_button.grid(row=3, column=1, padx=10, pady=10)
        self.multiply_button = tk.Button(self.frame, text="*", font=font_settings, command=lambda: self.set_operation('*'), width=5, **button_settings)
        self.multiply_button.grid(row=4, column=0, padx=10, pady=10)
        self.divide_button = tk.Button(self.frame, text="/", font=font_settings, command=lambda: self.set_operation('/'), width=5, **button_settings)
        self.divide_button.grid(row=4, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(self.frame, text="Calculate", font=font_settings, command=self.calculate, width=10, **calculate_button_settings)
        self.calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.frame, text="Result:", font=font_settings, bg="white")
        self.result_label.grid(row=6, column=0, padx=10, pady=10)
        self.result_value = tk.Label(self.frame, text="", font=font_settings, bg="white")
        self.result_value.grid(row=6, column=1, padx=10, pady=10)

    def set_operation(self, operation):
        self.operation = operation

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if self.operation == '+':
                result = num1 + num2
            elif self.operation == '-':
                result = num1 - num2
            elif self.operation == '*':
                result = num1 * num2
            elif self.operation == '/':
                result = num1 / num2
            else:
                messagebox.showerror("Input Error", "Please select a valid operation.")
                return

            self.result_value.config(text=str(result))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
