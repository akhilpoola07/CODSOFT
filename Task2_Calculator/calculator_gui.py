import tkinter as tk
from tkinter import messagebox


ALLOWED_CHARS = set("0123456789.+-*/() ")


def is_valid_expression(expression: str) -> bool:
    return bool(expression) and all(char in ALLOWED_CHARS for char in expression)


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x420")
        self.root.resizable(False, False)

        self.screen = tk.StringVar()
        self.build_ui()

    def build_ui(self) -> None:
        title = tk.Label(
            self.root,
            text="Simple Calculator",
            font=("Arial", 18, "bold"),
            fg="#1f3c88",
        )
        title.pack(pady=12)

        entry = tk.Entry(
            self.root,
            textvariable=self.screen,
            font=("Arial", 20),
            justify="right",
            bd=6,
        )
        entry.pack(fill="x", padx=14, pady=(0, 14), ipady=10)

        button_rows = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["(", ")", "=", ""],
        ]

        for row in button_rows:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both", padx=12, pady=4)

            for label in row:
                if not label:
                    spacer = tk.Label(frame)
                    spacer.pack(side="left", expand=True, fill="both", padx=4)
                    continue

                button = tk.Button(
                    frame,
                    text=label,
                    font=("Arial", 14, "bold"),
                    command=lambda value=label: self.on_button_click(value),
                )
                button.pack(side="left", expand=True, fill="both", padx=4)

    def on_button_click(self, value: str) -> None:
        if value == "C":
            self.screen.set("")
            return

        if value == "=":
            expression = self.screen.get().strip()
            if not is_valid_expression(expression):
                messagebox.showerror("Invalid Input", "Please enter a valid arithmetic expression.")
                self.screen.set("")
                return

            try:
                result = eval(expression, {"__builtins__": {}}, {})
            except ZeroDivisionError:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                self.screen.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid expression.")
                self.screen.set("")
            else:
                self.screen.set(str(result))
            return

        self.screen.set(self.screen.get() + value)


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
