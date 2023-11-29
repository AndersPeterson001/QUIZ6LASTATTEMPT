# main.py
# Import necessary modules and functions
import tkinter as tk
from app.functions import add_numbers, subtract_numbers, divide_numbers, multiply_numbers

def main():
    # Inner function to handle calculation logic
    def calculate():
        try:
            # Retrieve and convert numbers from input fields; extract the last name from the full name
            a = float(entry_number1.get())
            b = float(entry_number2.get())
            last_name = entry_name.get().split()[-1]
        except ValueError:
            # Handle error for invalid inputs
            label_result.config(text="Please enter valid numbers and a full name.")
            return

        # Mapping of operation names to function calls
        operations = {
            'add': add_numbers,
            'subtract': subtract_numbers,
            'divide': divide_numbers,
            'multiply': multiply_numbers
        }

        results = []
        # Perform each operation and append results to the list
        for op_name, op_func in operations.items():
            try:
                result = op_func(a, b)
                operation_symbol = '+' if op_name == 'add' else '-' if op_name == 'subtract' else '/' if op_name == 'divide' else '*'
                results.append(f"{a} {operation_symbol} {b} = {result}")
            except Exception as e:
                results.append(f"Error with {op_name}: {e}")

        # Write results to a file named after the user's last name
        content = f"This is {last_name.capitalize()}'s answer.\n" + "\n".join(results)
        filename = f"{last_name.lower()}.txt"
        with open(filename, 'w') as file:
            file.write(content)

        # Display the file path where results are saved
        label_result.config(text=f"Results saved in: {filename}")

    # Initialize the main window of the application
    root = tk.Tk()
    root.title("Math Operations GUI")

    # Create and place GUI widgets
    tk.Label(root, text="Enter your full name:").pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    tk.Label(root, text="Enter number 1:").pack()
    entry_number1 = tk.Entry(root)
    entry_number1.pack()

    tk.Label(root, text="Enter number 2:").pack()
    entry_number2 = tk.Entry(root)
    entry_number2.pack()

    button_calculate = tk.Button(root, text="Calculate", command=calculate)
    button_calculate.pack()

    label_result = tk.Label(root, text="")
    label_result.pack()

    # Start the GUI event loop
    root.mainloop()

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
