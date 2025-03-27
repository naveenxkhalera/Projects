
# Create a class for the calculator
class Calculator:
    # Initialize the calculator
    def __init__(self):
        # Create a new tkinter window
        self.window = tk.Tk()
        # Set the title of the window
        self.window.title("Calculator")
        # Create an entry field for the calculator
        self.entry = tk.Entry(self.window, width=35, borderwidth=5)
        # Place the entry field in the window
        self.entry.grid(row=0, column=0, columnspan=4)
        # Create the buttons for the calculator
        self.create_buttons()

    # Method to create the buttons for the calculator
    def create_buttons(self):
        # List of buttons to be created
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        # Initialize the row and column values
        row_val = 1
        col_val = 0
        # Loop through the buttons and create them
        for button in buttons:
            # Create a button with the given text and command
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            # Increment the column value
            col_val += 1
            # If the column value is greater than 3, reset it to 0 and increment the row value
            if col_val > 3:
                col_val = 0
                row_val += 1
        # Create a clear button
        tk.Button(self.window, text="Clear", width=22, command=self.clear_entry).grid(row=row_val, column=0, columnspan=4)

    # Method to handle button clicks
    def click_button(self, button):
        # If the button is the equals button, evaluate the expression in the entry field
        if button == '=':
            try:
                # Evaluate the expression and insert the result into the entry field
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                # If an error occurs, show an error message
                messagebox.showerror("Error", str(e))
        else:
            # If the button is not the equals button, insert the button's text into the entry field
            self.entry.insert(tk.END, button)

    # Method to clear the entry field
    def clear_entry(self):
        # Delete all text from the entry field
        self.entry.delete(0, tk.END)

    # Method to run the calculator
    def run(self):
        # Start the tkinter event loop
        self.window.mainloop()

# Create a new calculator and run it
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()