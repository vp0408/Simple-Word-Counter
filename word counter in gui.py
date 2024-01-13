import tkinter as tk
from tkinter import messagebox
def count_words(sentence):
    words = sentence.split()
    return len(words)
def calculate_word_count():
    user_input = entry.get()
    try:
        if not user_input.strip():
            raise ValueError("Input cannot be empty.")
        word_count = count_words(user_input)
        result_label.config(text=f"Word count: {word_count}")
    except ValueError as ve:
        messagebox.showerror("Error", f"{ve}")
# The below code is for the user interface , a simple gui based one.
app = tk.Tk()
app.title("Word Counter")
app.config(bg="black")
# Create and place the input entry widget
entry_label = tk.Label(app, text="Enter a sentence or paragraph:", font=("TIMES NEW ROMAN",20),justify='left',fg="Yellow",bg="black")
entry_label.pack(pady=10)
entry = tk.Entry(app, width=50)
entry.pack(pady=10)
# Create and place the button to calculate word count
calculate_button = tk.Button(app, text="Calculate Word Count",font=("Times new roman",16),fg="black",bg="yellow", command=calculate_word_count)
calculate_button.pack(pady=10)
# Create and place the label to display the word count result
result_label = tk.Label(app, text="",fg="black",bg="yellow")
result_label.pack(pady=10)
# Start the main event loop
app.mainloop()
